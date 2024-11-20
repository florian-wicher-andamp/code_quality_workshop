from src.Account import Account
from src.MoneyAmount import MoneyAmount

if __name__ == "__main__":
    alice = Account("Alice", MoneyAmount(100))
    bob = Account("Bob", MoneyAmount(0))

    print(alice, bob)

    alice.transfer(MoneyAmount(50), bob)

    print(alice, bob)