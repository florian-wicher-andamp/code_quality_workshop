import requests


class Currency:

    def __init__(self, code):
        self.dollar_exchange_rate = requests.get(f"https://open.er-api.com/v6/latest/USD").json()["rates"][code]
        self.code = code

    def __str__(self):
        return self.code


_Euro = None
def Euro():
    global _Euro
    if _Euro is None:
        _Euro = Currency("EUR")
    return _Euro

_Dollar = None
def Dollar():
    global _Dollar
    if _Dollar is None:
        _Dollar = Currency("USD")
    return _Dollar