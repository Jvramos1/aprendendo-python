import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']['bid']
cotacao_euro = cotacoes['EURBRL']['bid']
cotacao_btc = cotacoes['BTCBRL']['bid']
#print(cotacoes)
print('-=-='*9)
print('A cotação do dolar hj está R$ {}.'.format(cotacao_dolar))
print('A cotação do euro hj está R$ {}.'.format(cotacao_euro))
print('A cotação do bitcoin hj está R$ {}.'.format(cotacao_btc))
print('-=-='*10)
