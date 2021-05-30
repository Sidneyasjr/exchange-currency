import json
import requests
from api.model import Currency

response = requests.get("https://economia.awesomeapi.com.br/last/BRL-USD,EUR-USD,BTC-USD,ETH-USD")

content = json.loads(response.content)

currencies = {"USD": 1, "BRL": content['BRLUSD']['ask'], "EUR": content['EURUSD']['ask'],
              "BTC": content['BTCUSD']['ask'], "ETH": content['ETHUSD']['ask']}

data_base = [
    Currency(id=1, code="USD", exchange=1.0),
    Currency(id=2, code="BRL", exchange=content['BRLUSD']['ask']),
    Currency(id=3, code="EUR", exchange=content['EURUSD']['ask']),
    Currency(id=4, code="BTC", exchange=content['BTCUSD']['ask']),
    Currency(id=5, code="ETH", exchange=content['ETHUSD']['ask']),
]
