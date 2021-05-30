from fastapi.testclient import TestClient

from api.exchange import Exchange
from api.main import app
from api.model import Currency

client = TestClient(app)

db_fake = [
    Currency(id=1, code="USD", name="Dólar Americano", exchange=1.0),
    Currency(id=2, code="BRL", name="Real Brasileiro", exchange=0.1914),
    Currency(id=3, code="EUR", name="Euro", exchange=1.22),
]


def test_exist_currency_true():
    currency = "BRL"
    assert Exchange.exist_currency(currency, db_fake)


def test_exist_currency_false():
    currency = "BRR"
    assert not Exchange.exist_currency(currency, db_fake)


def test_find_currency():
    currency = "EUR"
    assert Exchange.find_currency(currency, db_fake) == Currency(id=3, code="EUR", name="Euro", exchange=1.22)


def test_exchange():
    currency_from = "BRL"
    currency_to = "EUR"
    amount = 500.00
    assert Exchange.exchange(currency_from, currency_to, amount, db_fake) == 78.442623


def test_exchange_from_to():
    currency_from = "BRL"
    currency_to = "EUR"
    assert Exchange.exchange(currency_from, currency_to, 1, db_fake) == 0.156885


def test_exchange_to_from():
    currency_from = "BRL"
    currency_to = "EUR"
    assert Exchange.exchange(currency_to, currency_from, 1, db_fake) == 6.374086
