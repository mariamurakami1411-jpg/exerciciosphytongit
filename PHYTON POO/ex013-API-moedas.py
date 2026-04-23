import requests
import pprint

link_api= 'https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL'
req= requests.get(link_api)

req_dados= req.json()

btc= req_dados['BTCBRL']['bid']
euro=req_dados['EURBRL']['bid']
dolar=req_dados['USDBRL']['bid']

print(f'{btc}')
print(f'{euro}')
print(f'{dolar}')