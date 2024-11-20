from src.InsufficientFundsError import InsufficientFundsError
from src.MoneyAmount import MoneyAmount


class Account:
    def __init__(self, name, balance: MoneyAmount):
        assert name.isalnum()

        self.name = name
        self._balance = balance

    def deposit(self, amount: MoneyAmount):
        self._balance += amount
        print(f"Deposited {amount} into '{self.name}'.")

    def withdraw(self, amount: MoneyAmount):
        if amount > self._balance:
            raise InsufficientFundsError()
        self._balance -= amount
        print(f"Withdrew {amount} from '{self.name}'.")

    def transfer(self, amount: MoneyAmount, other: 'Account'):
        self.withdraw(amount)
        other.deposit(amount)

    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        return 'Account ' + self.name

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}."