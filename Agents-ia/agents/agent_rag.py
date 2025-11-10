from langchain_huggingface import HuggingFaceEmbeddings
from qdrant_client.http.models import Distance, VectorParams, SparseVectorParams
from qdrant_client import QdrantClient, models
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.tools import Tool
from langchain_qdrant import QdrantVectorStore, FastEmbedSparse, RetrievalMode
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# --- AJUSTE 1: Chamar load_dotenv() no início ---
load_dotenv()

# LangChain, Qdrant e HuggingFace


# --- 1. CONFIGURAÇÃO CONSISTENTE ---
# Modelo de embedding open-source a ser usado em todo o script
MODELO_EMBEDDING = "sentence-transformers/all-MiniLM-L6-v2"
TAMANHO_VETOR = 384  # Tamanho do vetor para o modelo 'all-MiniLM-L6-v2'

# Resolver diretórios de forma robusta
CURRENT_DIR = Path(__file__).resolve().parent  # Agents-ia/agents
BASE_AGENTS_DIR = CURRENT_DIR.parent  # Agents-ia

# Configuração do Qdrant, PDF, e credenciais do .env
RAG_COLLECTION_NAME = "documentos_marketing"
PDF_PATH_PARA_INGESTAO = str(BASE_AGENTS_DIR / "documentos_marketing" / "livro.pdf")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")


# --- 2. LÓGICA DE INGESTÃO DE DADOS ---
def executar_ingestao():
    """Cria a coleção no Qdrant Cloud e a popula com os dados do PDF."""
    print("--- INICIANDO PROCESSO DE INGESTÃO DE DADOS NA NUVEM ---")

    if not QDRANT_URL or not QDRANT_API_KEY:
        print("❌ ERRO: Variáveis de ambiente QDRANT_URL ou QDRANT_API_KEY não encontradas.")
        print("   Verifique seu arquivo .env.")
        return

    try:
        client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

        print(
            f"Carregando modelo de embedding '{MODELO_EMBEDDING}'... Pode demorar na primeira vez.")
        dense_embeddings = HuggingFaceEmbeddings(model_name=MODELO_EMBEDDING)
        sparse_embeddings = FastEmbedSparse(model_name="Qdrant/bm25")

        print(f"Criando/Recriando a coleção: '{RAG_COLLECTION_NAME}'")
        client.recreate_collection(
            collection_name=RAG_COLLECTION_NAME,
            vectors_config={"dense": VectorParams(
                size=TAMANHO_VETOR, distance=Distance.COSINE)},
            sparse_vectors_config={"sparse": SparseVectorParams(
                index=models.SparseIndexParams(on_disk=False))},
        )

        print(f"Carregando PDF de: '{PDF_PATH_PARA_INGESTAO}'")
        loader = PyPDFLoader(PDF_PATH_PARA_INGESTAO, extract_images=False)
        documents = loader.load_and_split(
            text_splitter=RecursiveCharacterTextSplitter(
                chunk_size=1000, chunk_overlap=200)
        )
        print(f"PDF dividido em {len(documents)} trechos.")

        print("Iniciando a adição de documentos ao Qdrant Cloud...")
        QdrantVectorStore.from_documents(
            documents,
            embedding=dense_embeddings,
            sparse_embedding=sparse_embeddings,
            url=QDRANT_URL,
            api_key=QDRANT_API_KEY,
            collection_name=RAG_COLLECTION_NAME,
            vector_name="dense",
            sparse_vector_name="sparse"
        )
        print("--- ✅ INGESTÃO NA NUVEM CONCLUÍDA COM SUCESSO! ---")

    except FileNotFoundError:
        print(
            f"\n--- ❌ ERRO: Arquivo PDF não encontrado! Verifique o caminho: '{PDF_PATH_PARA_INGESTAO}'")
    except Exception as e:
        print(f"\n--- ❌ ERRO DURANTE A INGESTÃO: {e}")


# --- 3. LÓGICA DE PESQUISA (PARA USO EM TEMPO REAL) ---
try:
    if QDRANT_URL and QDRANT_API_KEY:
        client_query = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

        # --- AJUSTE 2: Usar o mesmo modelo de embedding da ingestão ---
        dense_embeddings_query = HuggingFaceEmbeddings(
            model_name=MODELO_EMBEDDING)
        sparse_embeddings_query = FastEmbedSparse(model_name="Qdrant/bm25")

        qdrant_retriever = QdrantVectorStore(
            client=client_query,
            collection_name=RAG_COLLECTION_NAME,
            embedding=dense_embeddings_query,
            sparse_embedding=sparse_embeddings_query,
            retrieval_mode=RetrievalMode.HYBRID,
            vector_name="dense",
            sparse_vector_name="sparse"
        )
        print("✅ Conectado ao banco de dados RAG na nuvem.")
    else:
        qdrant_retriever = None
        print("⚠️ AVISO: Credenciais do Qdrant Cloud não encontradas no .env.")

except Exception as e:
    qdrant_retriever = None
    print(
        f"⚠️ AVISO: Não foi possível conectar ao banco RAG na nuvem. Erro: {e}")


# --- O RESTO DO SCRIPT (4 e 5) ESTÁ CORRETO ---
def pesquisar_conteudo(query: str) -> str:
    """Pesquisa na base de conhecimento e retorna os trechos mais relevantes."""
    if not qdrant_retriever:
        return "Erro: A ferramenta de pesquisa não está disponível."
    found_docs = qdrant_retriever.similarity_search(query, k=3)
    if not found_docs:
        return "Nenhuma informação relevante foi encontrada."
    contexto = "\n\n---\n\n".join([doc.page_content for doc in found_docs])
    return f"De acordo com a base de conhecimento, aqui estão os trechos mais relevantes sobre '{query}':\n\n{contexto}"


ferramenta_pesquisa = Tool(
    name="ferramenta_pesquisa",
    func=pesquisar_conteudo,
    description="Use para pesquisar em uma base de conhecimento especializada sobre estratégias de marketing e vendas."
)

if __name__ == "__main__":
    if "--ingest" in sys.argv:
        executar_ingestao()
    else:
        print("\n--- MODO DE TESTE DE PESQUISA ---")
        if qdrant_retriever:
            while True:
                query_teste = input(
                    "\nDigite sua pergunta para testar (ou 'sair'): ")
                if query_teste.lower() == 'sair':
                    break
                resultado = pesquisar_conteudo(query_teste)
                print("\n--- Resultado da Busca ---\n", resultado)
