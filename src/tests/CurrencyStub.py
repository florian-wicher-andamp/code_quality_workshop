class CurrencyStub:

    def __init__(self, code, dollar_exchange_rate):
        self.dollar_exchange_rate = dollar_exchange_rate
        self.code = code

    def __str__(self):
        return self.code



_EuroStub = CurrencyStub("EUR", 1.1)
def EuroStub():
    return _EuroStub

_DollarStub = CurrencyStub("USD", 1.0)
def DollarStub():
    return _DollarStub