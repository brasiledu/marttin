# filepath: /Users/eduardovinicius/Faculdade/marttin/marttin/agent/ai_service.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

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

    def run_ai_consultor(self, pergunta: str, arquivo: str | None = None, pergunta_sobre_arquivo: str | None = None):
        entrada = pergunta
        if arquivo:
            pergunta_arquivo = pergunta_sobre_arquivo or "Forneça um resumo e estatísticas principais."
            entrada += (
                f"\n\nAdicionalmente, use a ferramenta Analisador_de_Planilhas com a seguinte entrada: "
                f"'{arquivo};{pergunta_arquivo}'"
            )

        state = self.app.invoke({
            "input": entrada,
            "chat_history": [],
            "dados_pesquisa": "",
            "dados_api": "",
            "dados_planilha": ""
        })
        return {
            "resposta_final": state.get("resposta_final", ""),
            "dados_pesquisa": state.get("dados_pesquisa", ""),
            "dados_api": state.get("dados_api", ""),
            "dados_planilha": state.get("dados_planilha", ""),
        }


# Instância reutilizável
ai_service = AIService()
