import os
import pandas as pd
from langchain_core.tools import Tool
from langchain_groq import ChatGroq


class AgenteDados:
    """Agente de análise de dados simplificado baseado em Pandas + LLM (sem langchain_experimental)."""

    def __init__(self):
        self.llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)
        self.df = None
        print("📊 Instância do Agente de Dados criada.")

    def carregar_dataframe(self, dataframe: pd.DataFrame):
        self.df = dataframe
        print("DataFrame carregado na memória do Agente de Dados.")

    def _construir_contexto(self, max_rows: int = 5, include_describe: bool = True) -> str:
        if self.df is None:
            return "Sem dados carregados."
        df = self.df
        info = []
        info.append(f"Dimensões: {df.shape[0]} linhas x {df.shape[1]} colunas")
        info.append("Colunas e tipos:")
        info.append(str(df.dtypes))
        info.append("\nAmostra (topo):")
        info.append(df.head(max_rows).to_string(index=False))
        # Estatísticas apenas para colunas numéricas para reduzir tamanho
        if include_describe:
            try:
                desc = df.describe(include=["number"]).transpose()
                info.append("\nEstatísticas (numéricas):")
                info.append(desc.to_string())
            except Exception:
                pass
        return "\n".join(info)

    def analisar(self, pergunta: str) -> str:
        if self.df is None:
            return "Agente não foi criado. Por favor, carregue os dados primeiro."
        contexto = self._construir_contexto()
        prompt = (
            "Você é um analista de dados. Responda à pergunta do usuário usando SOMENTE o contexto fornecido do DataFrame. "
            "Se a resposta exigir cálculo simples, explique e apresente o resultado. Se não for possível responder, diga claramente.\n\n"
            f"Pergunta do usuário:\n{pergunta}\n\n"
            f"Contexto dos dados (Pandas):\n{contexto}\n"
        )
        msg = self.llm.invoke(prompt)
        return getattr(msg, "content", str(msg)) or "Não foi possível obter uma resposta."


# Função "ponte" usada pelo roteador

def analisar_planilha(entrada_string: str) -> str:
    """
    Recebe uma string no formato 'caminho/arquivo;pergunta' e retorna a análise.
    Suporta CSV e Excel (.xlsx/.xls), com validações e mensagens claras.
    """
    caminho_arquivo = None
    try:
        if not entrada_string or ';' not in entrada_string:
            return "Erro: entrada inválida. Use o formato 'caminho/arquivo;pergunta'."

        caminho_arquivo, pergunta = entrada_string.split(';', 1)
        caminho_arquivo = caminho_arquivo.strip()
        pergunta = (pergunta or '').strip()

        if not caminho_arquivo:
            return "Erro: caminho do arquivo não informado."
        if not pergunta:
            return "Erro: pergunta sobre o arquivo não informada."
        if not os.path.exists(caminho_arquivo):
            return f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado. Verifique o caminho."
        if not os.path.isfile(caminho_arquivo):
            return f"Erro: O caminho '{caminho_arquivo}' não é um arquivo válido."

        ext = os.path.splitext(caminho_arquivo)[1].lower()
        if ext not in {'.csv', '.xlsx', '.xls'}:
            return "Erro: formato de arquivo não suportado. Use CSV, XLSX ou XLS."

        print(f"Analisando planilha: '{caminho_arquivo}' com a pergunta: '{pergunta}'")

        # Carrega o arquivo em um DataFrame do Pandas
        if ext == '.csv':
            try:
                df = pd.read_csv(caminho_arquivo)
            except Exception:
                df = pd.read_csv(caminho_arquivo, sep=';')
        else:
            try:
                df = pd.read_excel(caminho_arquivo)
            except ImportError:
                return "Erro: pacote 'openpyxl' não instalado. Instale para ler arquivos Excel."

        if df is None or df.empty:
            return "Erro: não foi possível carregar dados do arquivo ou ele está vazio."

        analisador = AgenteDados()
        analisador.carregar_dataframe(df)
        resultado = analisador.analisar(pergunta)
        return f"Análise do arquivo '{caminho_arquivo}': {resultado}"

    except FileNotFoundError:
        return f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado. Verifique o caminho."
    except ValueError as ve:
        return f"Erro de valor: {ve}"
    except Exception as e:
        return f"Erro ao processar a análise da planilha: {e}. Verifique se a entrada está no formato 'caminho;pergunta'."


# Tool exposta ao roteador
ferramenta_analise_dados = Tool(
    name="Analisador_de_Planilhas",
    func=analisar_planilha,
    description=(
        "Essencial para quando o usuário precisa de análises sobre dados em arquivos específicos (CSV, Excel). "
        "Use esta ferramenta sempre que precisar realizar analises de dados contidos no arquivo (CSV, Excel). "
        "A entrada DEVE ser uma string contendo o caminho do arquivo e a pergunta, separados por um ponto e vírgula ';'."
    )
)
