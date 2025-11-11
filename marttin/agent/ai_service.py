import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from typing import List, Dict
from langchain_core.messages import HumanMessage, AIMessage

# Garantir que possamos importar o pacote de agentes (Agents-ia/agents)
BASE_DIR = Path(__file__).resolve().parents[2]
AGENTS_DIR = BASE_DIR / "Agents-ia" / "agents"
if str(AGENTS_DIR) not in sys.path:
    sys.path.append(str(AGENTS_DIR))

# Carregar variáveis de ambiente
load_dotenv(BASE_DIR / ".env")

# Importações tardias após configurar path e env
from main import get_graph_app  # type: ignore


class AIService:
    def __init__(self):
        self.app = get_graph_app()
        self.chat_history: List = []

    def _to_lc_messages(self) -> List:
        msgs = []
        for m in self.chat_history:
            role = m.get("role")
            content = m.get("content", "")
            if role == "user":
                msgs.append(HumanMessage(content=content))
            else:
                msgs.append(AIMessage(content=content))
        return msgs

    def run_ai_consultor(self, pergunta: str, arquivo: str | None = None, pergunta_sobre_arquivo: str | None = None) -> Dict[str, str]:
        entrada = pergunta
        if arquivo:
            pergunta_arquivo = pergunta_sobre_arquivo or "Forneça um resumo e estatísticas principais."
            entrada += (
                f"\n\nAdicionalmente, use a ferramenta Analisador_de_Planilhas com a seguinte entrada: "
                f"'{arquivo};{pergunta_arquivo}'"
            )

        state = self.app.invoke({
            "input": entrada,
            "chat_history": self._to_lc_messages(),
            "dados_pesquisa": "",
            "dados_api": "",
            "dados_planilha": ""
        })

        resposta = state.get("resposta_final", "")
        # Atualiza histórico
        self.chat_history.append({"role": "user", "content": pergunta})
        self.chat_history.append({"role": "assistant", "content": resposta})

        # Sugestão de follow-up simples (pode ser aprimorada via LLM no futuro)
        follow_up = "Posso aprofundar em algum ponto, por exemplo público-alvo, canais ou projeção de resultados?"

        return {
            "resposta_final": resposta,
            "dados_pesquisa": state.get("dados_pesquisa", ""),
            "dados_api": state.get("dados_api", ""),
            "dados_planilha": state.get("dados_planilha", ""),
            "follow_up": follow_up,
        }


# Instância reutilizável
ai_service = AIService()
