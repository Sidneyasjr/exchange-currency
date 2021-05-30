from fastapi.testclient import TestClient

from api.db_currencies import db_currencies
from api.exchange import Exchange
from api.main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/moedas")
    assert response.status_code == 200
    assert response.json() == db_currencies


def test_read_exchange_currency():
    response = client.get("/conversor/?currency_from=BRL&currency_to=EUR&amount=5000")
    currency_from = Exchange.find_currency("BRL")
    currency_to = Exchange.find_currency("EUR")
    result = Exchange.exchange(currency_from.code, currency_to.code, 5000)
    assert response.status_code == 200
    assert response.json() == {
        "valor": 5000,
        "de": {"codigo": currency_from.code, "nome": currency_from.name,
               "cotacao": Exchange.exchange(currency_from.code, currency_to.code, 1)},
        "para": {"codigo": currency_to.code, "nome": currency_to.name,
                 "cotacao": Exchange.exchange(currency_to.code, currency_from.code, 1)},
        "resultado": result
    }


def test_not_found_currency():
    response = client.get("/conversor/?currency_from=BTC&currency_to=BRR&amount=10")
    assert response.json() == {"Status": 404, "Mensagem": f"Moeda BRR não encontrada"}
