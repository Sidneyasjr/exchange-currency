import json
import requests
from api.model import Currency

response = requests.get("https://economia.awesomeapi.com.br/last/USD,BRL-USD,EUR-USD,BTC-USD,ETH-USD")

content = json.loads(response.content)

db_currencies = [
    Currency(id=1, code="USD", name="Dólar Americano", exchange=1.0),
    Currency(id=2, code="BRL", name="Real Brasileiro", exchange=content['BRLUSD']['ask']),
    Currency(id=3, code="EUR", name="Euro", exchange=content['EURUSD']['ask']),
    Currency(id=4, code="BTC", name="Bitcoin", exchange=content['BTCUSD']['ask']),
    Currency(id=5, code="ETH", name="Ethereum", exchange=content['ETHUSD']['ask']),
]
