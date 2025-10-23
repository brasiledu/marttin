# MARTTIN AI v2.0 — Consultor de IA Multi‑Agente

![MARTTIN AI](https://img.shields.io/badge/MARTTIN-AI%20Consultor%20Multi%E2%80%91Agente-0f172a)
![Django](https://img.shields.io/badge/Django-5.x-0f5)
![LangGraph](https://img.shields.io/badge/LangGraph-0.2%2B-6b7280)
![LangChain](https://img.shields.io/badge/LangChain-0.2%2B-3b82f6)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB)
![License](https://img.shields.io/badge/License-Private-red)

## Visão Geral

O MARTTIN AI v2.0 evolui para um consultor empresarial multi‑agente, orquestrado com LangGraph, integrando:

- RAG híbrido (denso + BM25) sobre Qdrant Cloud
- API do IBGE (IPCA) para dados de inflação
- Analisador de Planilhas (CSV/XLS/XLSX) com Pandas + LLM
- Orquestração com LangGraph (roteador + estrategista)
- Interface Django (UI de chat e endpoints) e CLI opcional
- Memória breve de conversa e configuração via variáveis de ambiente

## Principais Componentes

- Agente Roteador (Groq): decide quais ferramentas acionar e agrega passos intermediários
- Agente Estrategista (Groq): sintetiza resposta final a partir do contexto (RAG/IPCA/Planilha)
- Ferramentas:
  - RAG (Qdrant): ingestão de PDFs e recuperação híbrida (MiniLM‑L6‑v2 + FastEmbedSparse/BM25)
  - IPCA (IBGE): consulta a séries históricas de inflação oficial
  - Analisador de Planilhas: valida caminho/formatos, sumariza shape/dtypes/describe/head e produz insights
- LangGraph: estado do agente e fluxo com atualização de dados de pesquisa/API/planilha
- Django: serviço `ai_service.py` integra o grafo ao `chat_api` e UI de chat

## Requisitos

- Python 3.10+ (recomendado 3.11)
- Dependências Python (requirements.txt)
- Conta/endpoint no Qdrant Cloud (RAG)
- Chave de API Groq

## Configuração Rápida

1) Clonar e criar ambiente

```bash
git clone <repository-url>
cd marttin
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2) Variáveis de ambiente (.env na raiz)

```env
# GROQ
GROQ_API_KEY=sk_groq_xxx

# Qdrant (Cloud)
QDRANT_URL=https://<cluster-id>.cloud.qdrant.io
QDRANT_API_KEY=xyz
# Opcional: QDRANT_COLLECTION=marttin_docs
```

3) Migrar banco e subir Django

```bash
cd marttin
python manage.py migrate
python manage.py runserver
```

Acesse: http://localhost:8000

## Ingestão de Documentos (RAG)

Antes de usar a busca semântica, faça a ingestão (a coleção será criada no Qdrant):

```bash
# No diretório do repositório
python Agents-ia/agents/agent_rag.py --ingest --pdf "Agents-ia/documentos_marketing/livro.pdf"
```

Observação: até a ingestão ocorrer, o retriever pode retornar aviso de coleção inexistente (404) — não é erro crítico.

## CLI Opcional (Perguntas + arquivo)

O grafo pode ser usado no terminal para perguntas diretas, com caminho opcional para planilhas:

```bash
python Agents-ia/agents/main.py --question "Como a inflação recente afeta o setor de varejo?" \
  --file "/caminho/para/minha_planilha.xlsx"
```

## Endpoints Django

- GET /chat/ — UI do chat
- POST /api/chat/ — Envia mensagem ao consultor de IA
- GET /marketing-analysis/ — Página de análise de marketing
- GET /content-ideas/ — Geração de conteúdo

## Estrutura Relevante

```
Agents-ia/
  agents/
    agent_roteador.py         # Router (Groq, tools calling)
    agent_estrategista.py     # Estratégia/síntese final
    agent_rag.py              # Ingestão + recuperação Qdrant
    agent_api.py              # IBGE IPCA
    agente_dados.py           # Analisador de Planilhas (CSV/XLS/XLSX)
    tools_registry.py         # Registro das ferramentas
    main.py                   # Grafo LangGraph + CLI
marttin/agent/
  ai_service.py               # Ponte Django -> LangGraph
  views.py                    # chat_api usa o grafo (autenticados)
  templates/agent/chat.html   # UI de chat
```

## Desenvolvimento

- Compatível com LangChain 0.2+ e LangGraph
- Evita APIs deprecadas (usa `create_tool_calling_agent` e fallback `llm.bind_tools`)
- Tools definidos via `langchain_core.tools.Tool`
- Pandas + openpyxl para análise de planilhas

## Testes

```bash
python manage.py test
```

Sugestões:
- testes de integração para caminhos RAG/IPCA/Planilha + síntese do estrategista
- testes para endpoints Django (chat_api, etc.)

## Changelog (v2.0)

- Novo consultor multi‑agente com LangGraph (router + estrategista)
- RAG híbrido no Qdrant, ingestão de PDFs e recuperação robusta
- Ferramenta IPCA/IBGE integrada
- Analisador de Planilhas (CSV/XLS/XLSX) com validação e mensagens de erro claras
- UI de chat integrada ao grafo via serviço Django
- CLI opcional (pergunta + arquivo)
- Requirements consolidados para LangChain 0.2+
- Substituição de emojis por Bootstrap Icons
- Preparação para extrair CSS/JS inline para arquivos estáticos

## Segurança

- CSRF habilitado nos endpoints Django
- Variáveis sensíveis em .env (não versionado)

## Licença

Projeto privado. Todos os direitos reservados.
