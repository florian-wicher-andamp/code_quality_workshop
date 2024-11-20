from src.MoneyAmount import MoneyAmount


class Transaction:
    def __init__(self, from_account_name: str, to_account_name: str, amount: MoneyAmount):
        self.from_account_name = from_account_name
        self.to_account_name = to_account_name
        self.amount = amount

    def __repr__(self):
        return f"{self.from_account_name} -[{self.amount}]-> {self.to_account_name}"

    def __eq__(self, other):
        return self.from_account_name == other.from_account_name and self.to_account_name == other.to_account_name and self.amount == other.amount