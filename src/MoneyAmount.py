from src.Currency import Currency


class MoneyAmount:

    def __init__(self, decimal_amount: float = None, currency: Currency = None, amount_in_cents: int = None):
        if currency is None:
            raise ValueError("Please provide currency")
        if amount_in_cents is not None and decimal_amount is not None:
            raise ValueError("Please provide either amount or amount_in_cents, not both.")
        if amount_in_cents is None and decimal_amount is None:
            raise ValueError("Please provide either amount or amount_in_cents.")

        if decimal_amount is not None:
            amount_in_cents = int(decimal_amount * 100)

        if amount_in_cents < 0:
            raise ValueError("Amount cannot be negative.")
        amount_str = str(decimal_amount)
        if "." in amount_str:
            decimals = amount_str.split(".")[1]
            if len(decimals) > 2:
                raise ValueError(f"Amount cannot have more than two decimal places: {decimal_amount}")

        self.currency = currency
        self.amount_in_cents = amount_in_cents

    def __repr__(self):
        if self.amount_in_cents % 100 != 0:
            return f"{self.amount_in_cents / 100:.2f} {self.currency}"
        else:
            return f"{self.amount_in_cents / 100:.0f} {self.currency}"

    def __add__(self, other: 'MoneyAmount'):
        return MoneyAmount(amount_in_cents=self.amount_in_cents + other.convert_to(self.currency).amount_in_cents,
                           currency=self.currency)

    def __sub__(self, other: 'MoneyAmount'):
        return MoneyAmount(amount_in_cents=self.amount_in_cents - other.convert_to(self.currency).amount_in_cents,
                           currency=self.currency)

    def __gt__(self, other: 'MoneyAmount'):
        return self.amount_in_cents > other.convert_to(self.currency).amount_in_cents

    def __eq__(self, other):
        return self.amount_in_cents == other.amount_in_cents and self.currency == other.currency

    def convert_to(self, target_currency: Currency):
        result_in_dollar_cents = self.amount_in_cents * self.currency.dollar_exchange_rate
        result_in_target_currency_cents = result_in_dollar_cents * 1 / target_currency.dollar_exchange_rate
        return MoneyAmount(amount_in_cents=result_in_target_currency_cents, currency=target_currency)
