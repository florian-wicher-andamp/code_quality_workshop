

class MoneyAmount:

    def __init__(self, decimal_amount: float = None, amount_in_cents: int = None):
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

        self.amount_in_cents = amount_in_cents

    def __repr__(self):
        if self.amount_in_cents % 100 != 0:
            return f"{self.amount_in_cents / 100:.2f}"
        else:
            return f"{self.amount_in_cents / 100:.0f}"

    def __add__(self, other: 'MoneyAmount'):
        return MoneyAmount(amount_in_cents=self.amount_in_cents + other.amount_in_cents)

    def __sub__(self, other: 'MoneyAmount'):
        return MoneyAmount(amount_in_cents=self.amount_in_cents - other.amount_in_cents)

    def __gt__(self, other: 'MoneyAmount'):
        return self.amount_in_cents > other.amount_in_cents

    def __eq__(self, other):
        return self.amount_in_cents == other.amount_in_cents

