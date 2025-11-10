from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq


def criar_cadeia_estrategista():
    prompt_template = """
    Você é um consultor de negócios estrategista de alto nível. Sua missão é criar uma solução clara e acionável para o cliente com base nos dados fornecidos.

    **Consulta Original do Cliente:**
    {consulta_cliente}

    **Dados Coletados pela Pesquisa Interna:**
    {dados_pesquisa}

    **Dados de Mercado Coletados via API:**
    {dados_api}

    **Resultados da Análise de Planilha Fornecida pelo Cliente:**
    {dados_planilha}

    Com base em TODAS as informações disponíveis, forneça uma análise estratégica completa e uma recomendação para o cliente.
    Seja claro, objetivo e estruture sua resposta em seções.
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.2)

    cadeia_estrategista = prompt | llm
    return cadeia_estrategista
