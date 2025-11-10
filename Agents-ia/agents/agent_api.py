import requests
from langchain_core.tools import Tool


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


ferramenta_api_ipca = Tool(
    name="Consultor de Inflação IPCA",
    # Usamos lambda para garantir que a função seja chamada com o argumento
    func=lambda ano: buscar_dados_ipca(ano),
    description="Use esta ferramenta para obter o valor acumulado do IPCA (Índice de Preços ao Consumidor Amplo) para um determinado ano. Você precisa fornecer o ano como entrada."
)
