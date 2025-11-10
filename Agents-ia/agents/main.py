from typing import List, TypedDict, Annotated
from langchain_core.messages import BaseMessage
import operator

# LangGraph
from langgraph.graph import StateGraph, END

# Variáveis de ambiente
from dotenv import load_dotenv

# Componentes do nosso sistema
from agent_roteador import criar_agente_roteador
from agent_estrategista import criar_cadeia_estrategista

load_dotenv()

# 1. Defina o estado do seu grafo (com o novo campo)


class AgentState(TypedDict):
    input: str
    chat_history: Annotated[List[BaseMessage], operator.add]
    # Resultados das ferramentas
    dados_pesquisa: str
    dados_api: str
    dados_planilha: str
    # Resposta final
    resposta_final: str

# 2. Defina os nós do grafo (agentes)


def node_roteador(state: AgentState) -> AgentState:
    """Invoca o roteador para executar uma ferramenta e atualiza o estado."""
    print("--- NÓ ROTEADOR ---")
    roteador = criar_agente_roteador()
    resultado_roteador = roteador.invoke({"input": state["input"]})

    if 'intermediate_steps' in resultado_roteador and resultado_roteador['intermediate_steps']:
        passo_intermediario = resultado_roteador['intermediate_steps'][0]
        nome_ferramenta = passo_intermediario[0].tool
        resultado_ferramenta = str(passo_intermediario[1])

        print(f"Ferramenta executada: {nome_ferramenta}")
        print(f"Resultado: {resultado_ferramenta}")

        # --- LÓGICA DE ATUALIZAÇÃO DO ESTADO ---
        if nome_ferramenta == "ferramenta_pesquisa":
            state['dados_pesquisa'] = resultado_ferramenta
        elif nome_ferramenta == "Consultor de Inflação IPCA":
            state['dados_api'] = resultado_ferramenta
        elif nome_ferramenta == "Analisador_de_Planilhas":
            state['dados_planilha'] = resultado_ferramenta

    return state


def node_estrategista(state: AgentState) -> AgentState:
    """Invoca o estrategista para gerar a resposta final com base no estado."""
    print("--- NÓ ESTRATEGISTA ---")
    estrategista = criar_cadeia_estrategista()

    consulta_cliente = state.get("input", "")
    dados_pesquisa = state.get(
        "dados_pesquisa", "Nenhuma pesquisa sobre o tema foi realizada.")
    dados_api = state.get(
        "dados_api", "Nenhum dado de mercado externo foi coletado.")
    dados_planilha = state.get(
        "dados_planilha", "Nenhuma planilha foi fornecida para análise.")

    solucao_final = estrategista.invoke({
        "consulta_cliente": consulta_cliente,
        "dados_pesquisa": dados_pesquisa,
        "dados_api": dados_api,
        "dados_planilha": dados_planilha
    })
    state['resposta_final'] = solucao_final.content
    return state


# 3. Construa o grafo e exponha um factory para uso programático

def get_graph_app():
    workflow = StateGraph(AgentState)
    workflow.add_node("roteador", node_roteador)
    workflow.add_node("estrategista", node_estrategista)
    workflow.set_entry_point("roteador")
    workflow.add_edge("roteador", "estrategista")
    workflow.add_edge("estrategista", END)
    return workflow.compile()


# CLI interativo apenas quando executado diretamente
if __name__ == "__main__":
    app = get_graph_app()

    print("Bem-vindo ao Consultor de IA!")
    consulta_texto = input("Qual é o seu principal objetivo ou pergunta hoje? ")
    caminho_arquivo = input(
        "Você gostaria de anexar um arquivo de dados (CSV/Excel) para análise? Se sim, digite o caminho do arquivo. Se não, apenas pressione Enter: ")

    entrada_para_roteador = consulta_texto

    if caminho_arquivo:
        pergunta_sobre_arquivo = input(
            f"Qual pergunta você gostaria de fazer sobre o arquivo '{caminho_arquivo}'? ")
        entrada_para_roteador += (
            f"\n\nAdicionalmente, use a ferramenta Analisador_de_Planilhas com a seguinte entrada: "
            f"'{caminho_arquivo};{pergunta_sobre_arquivo}'"
        )

    print("\nIniciando fluxo de execução...")
    final_state = app.invoke({
        "input": entrada_para_roteador,
        "chat_history": [],
        "dados_pesquisa": "",
        "dados_api": "",
        "dados_planilha": ""
    })

    print("\n\n======================")
    print("--- RESPOSTA FINAL ---")
    print(final_state['resposta_final'])
    print("======================")
