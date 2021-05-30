from api.db_currencies import db_currencies

model_in_use = db_currencies


def find_currency(currency, model=model_in_use):
    for c in model:
        if c.code == currency:
            return c


def exist_currency(currency, model=model_in_use):
    for c in model:
        if c.code == currency:
            return True
    return False


def exchange_rate(currency, model=model_in_use):
    for c in model:
        if c.code == currency:
            return float(c.exchange)


def exchange(currency_from, currency_to, amount, model=model_in_use):
    c1 = exchange_rate(currency_from, model)
    c2 = exchange_rate(currency_to, model)
    return round(((amount * c1) / c2), 6)
