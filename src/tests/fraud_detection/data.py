from src.Account import Account
from src.MoneyAmount import MoneyAmount
from src.tests.CurrencyStub import EuroStub

EUR = EuroStub()

def demo_accounts():
    return Account("Test1", MoneyAmount(100, EUR)), Account("Test2", MoneyAmount(50, EUR))

def demo_account1():
    return demo_accounts()[0]

def demo_account2():
    return demo_accounts()[1]