from types import SimpleNamespace
from typing import Any, Dict, List

try:
    from langchain.agents import create_tool_calling_agent  # LangChain 0.2+
except ImportError:  # fallback
    create_tool_calling_agent = None  # type: ignore

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from tools_registry import todas_as_ferramentas
from langchain_groq import ChatGroq


class SimpleAgentExecutor:
    """Executor simples que chama o agente para decidir a ferramenta e executa a tool, retornando intermediate_steps."""

    def __init__(self, agent, tools):
        self.agent = agent
        self.tools = {t.name: t for t in tools}

    def _extract_tool_calls(self, ai_msg) -> List[Dict[str, Any]]:
        calls = getattr(ai_msg, "tool_calls", None)
        if calls:
            return calls
        return ai_msg.additional_kwargs.get("tool_calls", []) if hasattr(ai_msg, "additional_kwargs") else []

    def invoke(self, payload: Dict[str, Any]):
        # Garantir que o prompt receba todas as variáveis esperadas
        inputs = {
            "input": payload.get("input", ""),
            "agent_scratchpad": payload.get("agent_scratchpad", []),
        }
        ai_msg = self.agent.invoke(inputs)
        tool_calls = self._extract_tool_calls(ai_msg)
        steps = []
        for call in tool_calls:
            name = getattr(call, "name", None) or (call.get("name") if isinstance(call, dict) else None)
            args = getattr(call, "args", None) or (call.get("args") if isinstance(call, dict) else None) or {}
            if isinstance(args, dict) and len(args) == 1:
                arg_val = next(iter(args.values()))
            elif isinstance(args, dict) and "input" in args:
                arg_val = args["input"]
            else:
                arg_val = args if isinstance(args, str) else str(args)

            tool = self.tools.get(name)
            if not tool:
                steps.append((SimpleNamespace(tool=name), f"Erro: ferramenta '{name}' não encontrada."))
                continue

            try:
                result = tool.func(arg_val)
            except Exception as e:
                result = f"Erro ao executar a ferramenta '{name}': {e}"

            steps.append((SimpleNamespace(tool=name), result))

        return {"intermediate_steps": steps, "output": getattr(ai_msg, "content", None)}


def criar_agente_roteador():
    """Cria e retorna o agente roteador com suas ferramentas (executor simples)."""
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "Você é o AGENTE ROTEADOR em um sistema multi-agente de consultoria de marketing. "
            "Objetivo: decidir qual ferramenta aciona, mantendo tom natural e colaborativo. Regras:\n"
            "- NÃO explique a arquitetura interna.\n"
            "- Se a pergunta mencionar 'arquivo', 'planilha', 'csv', 'excel' => considerar Analisador_de_Planilhas.\n"
            "- Se envolver 'inflação', 'IPCA', 'dados econômicos' => usar consultor_inflacao_ipca.\n"
            "- Se for sobre estratégia, conteúdo ou marketing geral => considerar pesquisa primeiro.\n"
            "- Se nenhuma ferramenta for claramente aplicável, responda pedindo clarificação e sugira opções.\n"
            "Formato da resposta para o usuário deve ser NATURAL e curta antes de delegar internamente.\n"
        )),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    if create_tool_calling_agent:
        agent = create_tool_calling_agent(llm, todas_as_ferramentas, prompt)
    else:
        agent = prompt | llm.bind_tools(todas_as_ferramentas)

    return SimpleAgentExecutor(agent, todas_as_ferramentas)
