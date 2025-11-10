
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Carrega as variáveis de ambiente (onde sua OPENAI_API_KEY deve estar)
load_dotenv()


class ChatbotEmpresarial:
    def __init__(self, db_connection: str = "sqlite:///chat_history.db"):

        # 1. Inicializa o modelo de linguagem
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.2)

        # 2. Define o template do prompt
        prompt = ChatPromptTemplate.from_messages([
            ("system", '''Você é um consultor empresarial especializado em gestão, inovação, marketing, finanças, operações e desenvolvimento estratégico.

                Seu papel é analisar informações fornecidas pelo usuário.

                    Sempre siga estas diretrizes:

                    Faça perguntas relevantes para entender melhor o contexto, caso necessário.

                    Estruture suas respostas de forma objetiva: Faça diagnósticos

                    Adapte suas perguntas do diagnóstico ao porte da empresa (startup, pequena, média ou grande) e ao setor de atuação.

                    Mantenha um tom profissional, acessível'''),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{human_input}")
        ])

        # 3. Monta a cadeia de execução principal
        llm_chain = (
            RunnablePassthrough.assign(
                history=self.memory_window
            )
            | prompt
            | self.llm
            | StrOutputParser()
        )

        # 4. Envolve a cadeia com o gerenciador de histórico de mensagens
        self.conversational_chain = RunnableWithMessageHistory(
            llm_chain,
            self.get_session_history,
            input_messages_key="human_input",
            history_messages_key="history",
        )

        # Guarda a string de conexão para ser usada pelo método de histórico
        self.db_connection = db_connection

    # Retornar historico de conversa

    def get_session_history(self, session_id: str) -> SQLChatMessageHistory:

        return SQLChatMessageHistory(session_id, connection_string=self.db_connection)

    @staticmethod
    def memory_window(data: dict):
        k = 10
        messages = data.get("history", [])
        return messages[-k:]

    def conversar(self, human_input: str, session_id: str):
        # O objeto de configuração é necessário para passar o session_id
        config = {"configurable": {"session_id": session_id}}
        return self.conversational_chain.invoke({"human_input": human_input}, config=config)
