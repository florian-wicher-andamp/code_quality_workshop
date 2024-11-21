from src.Account import Account
from src.MoneyAmount import MoneyAmount


# noinspection PyStatementEffect
class Transaction:
    def __init__(self, from_account: Account, to_account: Account, amount: MoneyAmount, is_suspicious=False):
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.suspicious = is_suspicious

    def __repr__(self):
        result = f"{self.from_account.name} -[{self.amount}]-> {self.to_account.name}"
        if self.suspicious:
            result + " (suspicious)"
        return result

    def __eq__(self, other):
        return (self.from_account.name == other.from_account.name and self.to_account.name == other.to_account.name
                and self.amount == other.amount)

    def reverse(self):
        return Transaction(self.to_account, self.from_account, self.amount, self.suspicious)
