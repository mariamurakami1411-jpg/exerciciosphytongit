import requests
import pprint
from rich import print

api_key= 'b20ffbd618b44dfeb71215023262104'
link='http://api.weatherapi.com/v1/current.json'

parametros= {
    'key': api_key,
    'q': 'Curitiba',
    'lang': 'pt'
}

resp= requests.get(link, params=parametros)
if resp.status_code==200:
    dados_requisicao= resp.json()
    temp= dados_requisicao['current']['temp_c']
    descr= dados_requisicao['current']['condition']['text']
    print(f'[bold white]{temp}°C[/]')
    print(f'[bold cyan]{descr}[/]')


# status codes:
# 200: deu certoa requisição
# 300: redirecionada
# 400: não conseguiu fazer a requisição
    # 401: sem chave API
# 500: erro no sistema da API