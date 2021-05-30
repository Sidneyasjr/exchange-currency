from fastapi import FastAPI
from api.currencies import data_base
from api.exchange import exist_currency, exchange

app = FastAPI()


@app.get("/currencies")
def get_all_currencies():
    return data_base


@app.get("/convert/{current_from&current_to&amount}")
def get_convert_current(currency_from: str, currency_to: str, amount: float):
    if not exist_currency(currency_from):
        return {"Status": 404, "Mensagem": f"Moeda {currency_from} não encontrada"}
    if not exist_currency(currency_to):
        return {"Status": 404, "Mensagem": f"Moeda {currency_to} não encontrada"}
    result = exchange(currency_from, currency_to, amount)
    converted = {"valor": amount, "de": currency_from, "para": currency_to, "resultado": result}
    return converted
