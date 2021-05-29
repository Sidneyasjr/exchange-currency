from currencies import base_model


def exist_currency(currency):
    for c in base_model:
        if c.code == currency:
            return True
    return False


def exchange_rate(currency):
    value = 0
    for c in base_model:
        if c.code == currency:
            value = float(c.exchange)
    return value


def exchange(currency_from, currency_to, amount):
    c1 = exchange_rate(currency_from)
    c2 = exchange_rate(currency_to)
    return round(((amount * c1) / c2), 2)

