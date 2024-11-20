from src.Account import Account
from src.Currency import Dollar, Euro
from src.MoneyAmount import MoneyAmount

if __name__ == "__main__":
    alice = Account("Alice", MoneyAmount(100, Dollar()))
    bob = Account("Bob", MoneyAmount(0, Euro()))

    print(alice, bob)

    alice.transfer(MoneyAmount(50, Dollar()), bob)

    print(alice, bob)