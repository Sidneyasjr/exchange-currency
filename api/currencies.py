import json
import requests
from model import Current

response = requests.get("https://economia.awesomeapi.com.br/last/BRL-USD,EUR-USD,BTC-USD,ETH-USD")

content = json.loads(response.content)

currencies = {"USD": 1, "BRL": content['BRLUSD']['ask'], "EUR": content['EURUSD']['ask'],
              "BTC": content['BTCUSD']['ask'], "ETH": content['ETHUSD']['ask']}

base_model = [
    Current(id=1, code="USD", exchange=1.0),
    Current(id=2, code="BRL", exchange=content['BRLUSD']['ask']),
    Current(id=3, code="EUR", exchange=content['EURUSD']['ask']),
    Current(id=4, code="BTC", exchange=content['BTCUSD']['ask']),
    Current(id=5, code="ETH", exchange=content['ETHUSD']['ask']),
]