from fastapi import FastAPI
from api.db_currencies import db_currencies
from api.exchange import exist_currency, exchange, find_currency

app = FastAPI()


@app.get("/moedas")
def get_all_currencies():
    return db_currencies


@app.get("/conversor/")
def get_exchange_currency(currency_from: str, currency_to: str, amount: float):
    if not exist_currency(currency_from):
        return {"Status": 404, "Mensagem": f"Moeda {currency_from} não encontrada"}
    if not exist_currency(currency_to):
        return {"Status": 404, "Mensagem": f"Moeda {currency_to} não encontrada"}
    currency_from = find_currency(currency_from)
    currency_to = find_currency(currency_to)
    exchange_from_to = exchange(currency_from.code, currency_to.code, 1)
    exchange_to_from = exchange(currency_to.code, currency_from.code, 1)
    result = exchange(currency_from.code, currency_to.code, amount)
    converted = {
        "valor": amount,
        "de": {"codigo": currency_from.code, "nome": currency_from.name,
               "cotacao": exchange_from_to},
        "para": {"codigo": currency_to.code, "nome": currency_to.name,
                 "cotacao": exchange_to_from},
        "resultado": result
    }
    return converted
