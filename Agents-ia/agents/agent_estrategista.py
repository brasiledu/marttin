from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq


def criar_cadeia_estrategista():
    # Prompt conversacional com uso de histórico
    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "Você é um consultor de negócios estrategista SENIOR especializado em marketing e crescimento. "
            "Objetivo: gerar respostas conversacionais, contextuais e úteis. Regras:\n"
            "1. Reconheça brevemente a intenção do usuário antes de responder (1 frase).\n"
            "2. Use tom profissional, amigável e claro.\n"
            "3. Estruture a resposta em seções curtas com títulos em MAIÚSCULAS ou emojis relevantes.\n"
            "4. Não repita literalmente a pergunta; incorpore-a ao raciocínio.\n"
            "5. Traga insights acionáveis (bullets).\n"
            "6. Termine SEMPRE com uma pergunta de continuação personalizada que ajude a avançar.\n"
            "7. Se faltar dado (pesquisa/API/planilha), seja transparente e sugira o que coletar.\n"
            "8. Evite respostas genéricas como 'Com base nas informações fornecidas'. Seja específico.\n"
        )),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", (
            "Consulta do cliente: {consulta_cliente}\n\n"
            "DADOS DE PESQUISA:\n{dados_pesquisa}\n\n"
            "DADOS DE MERCADO (API):\n{dados_api}\n\n"
            "ANÁLISE DE PLANILHA:\n{dados_planilha}\n\n"
            "Gere uma resposta estratégica conversacional seguindo as regras."
        )),
    ])

    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.4)  # leve aumento de criatividade
    cadeia_estrategista = prompt | llm
    return cadeia_estrategista
