from unittest.mock import MagicMock

import pytest

from src.Account import Account
from src.InsufficientFundsError import InsufficientFundsError
from src.MoneyAmount import MoneyAmount
from src.tests.CurrencyStub import EuroStub

EUR = EuroStub()

def test_deposit_increases_balance():
    account = Account("Test", MoneyAmount(100, EUR))
    account.deposit(MoneyAmount(50, EUR))
    assert account.balance == MoneyAmount(150, EUR)


def test_withdraw_decreases_balance():
    account = Account("Test", MoneyAmount(100, EUR))
    account.withdraw(MoneyAmount(50, EUR))
    assert account.balance == MoneyAmount(50, EUR)


def test_withdraw_raises_error_on_insufficient_funds():
    account = Account("Test", MoneyAmount(100, EUR))
    with pytest.raises(InsufficientFundsError):
        account.withdraw(MoneyAmount(150, EUR))


def test_transfer_moves_funds_between_accounts_using_stubs():
    account1 = Account("Test1", MoneyAmount(100, EUR))
    account2 = Account("Test2", MoneyAmount(50, EUR))

    account1.transfer(MoneyAmount(50, EUR), account2)

    assert account1.balance == MoneyAmount(50, EUR)
    assert account2.balance == MoneyAmount(100, EUR)


def test_balance_property_returns_correct_value():
    amount = MoneyAmount(100, EUR)
    account = Account("Test", amount)
    assert account.balance == amount


def test_transfer_moves_funds_between_accounts_using_mocks():
    EUR = MagicMock()
    EUR.dollar_exchange_rate = 1.1

    account1 = Account("Test1", MoneyAmount(100, EUR))
    account2 = Account("Test2", MoneyAmount(50, EUR))

    account1.transfer(MoneyAmount(50, EUR), account2)

    assert account1.balance == MoneyAmount(50, EUR)
    assert account2.balance == MoneyAmount(100, EUR)


def test_repr_returns_correct_string():
    unicorn_sheckels = MagicMock()
    unicorn_sheckels.__str__.return_value = "🦄💰"

    account = Account("Test", MoneyAmount(100, unicorn_sheckels))
    assert repr(account) == "Account Test"
