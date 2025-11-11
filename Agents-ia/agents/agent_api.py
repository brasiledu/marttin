import requests
from langchain_core.tools import Tool
from pydantic import BaseModel, Field


class IpcaArgs(BaseModel):
    ano: str = Field(..., description="Ano no formato YYYY, ex: 2023")


def buscar_dados_ipca(ano: str) -> str:
    """Busca o acumulado do IPCA (inflação) para um ano específico na API do IBGE."""
    try:
        url = f"https://servicodados.ibge.gov.br/api/v3/agregados/1737/periodos/{ano}/variaveis/2266?localidades=N1[all]"
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro para respostas ruins (4xx ou 5xx)
        data = response.json()
        resultado = data[0]['resultados'][0]['series'][0]['serie'][ano]
        return f"O IPCA acumulado para o ano de {ano} foi de {resultado}%."
    except Exception as e:
        return f"Não foi possível buscar os dados para o ano {ano}. Erro: {e}"


ferramenta_api_ipca = Tool.from_function(
    name="consultor_inflacao_ipca",
    func=buscar_dados_ipca,
    description=(
        "Use esta ferramenta para obter o valor acumulado do IPCA (Índice de Preços ao Consumidor Amplo) "
        "para um determinado ano (YYYY)."
    ),
    args_schema=IpcaArgs,
)
