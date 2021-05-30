from api.db_currencies import db_currencies


class Exchange:
    model_in_use = db_currencies

    @staticmethod
    def find_currency(currency, model=model_in_use):
        for c in model:
            if c.code == currency:
                return c

    @staticmethod
    def exist_currency(currency, model=model_in_use):
        for c in model:
            if c.code == currency:
                return True
        return False

    @staticmethod
    def exchange(currency_from, currency_to, amount, model=model_in_use):
        def exchange_rate(currency):
            for c in model:
                if c.code == currency:
                    return float(c.exchange)
        c1 = exchange_rate(currency_from)
        c2 = exchange_rate(currency_to)
        return round(((amount * c1) / c2), 6)
