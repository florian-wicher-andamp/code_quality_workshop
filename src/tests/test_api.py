from xml.dom import NotFoundErr

import pytest

import function_app
from function_app import handle_transfer, find_account, handle_get_account
from src.Account import Account
from src.Currency import Euro
from src.InsufficientFundsError import InsufficientFundsError
from src.MoneyAmount import MoneyAmount



def setup_function():
    function_app.accounts = [
        Account("account1", MoneyAmount(100, Euro())),
        Account("account2", MoneyAmount(50, Euro()))
    ]


def test_transfer_successful():
    result = handle_transfer("account1", "account2", 50, "EUR")
    assert result == "Transferred 50 EUR from account1 to account2"
    assert find_account("account1").balance == MoneyAmount(50, Euro())
    assert find_account("account2").balance == MoneyAmount(100, Euro())

def test_transfer_insufficient_funds():
    with pytest.raises(InsufficientFundsError) as insufficient_funds:
        handle_transfer("account1", "account2", 150, "EUR")
    assert str(insufficient_funds.value) == "Insufficient funds."

def test_transfer_account_not_found_returns_error():
    with pytest.raises(NotFoundErr) as not_found:
        handle_transfer("account1", "account3", 50, "EUR")
    assert str(not_found.value) == "Account account3 not found"

def test_get_account_successful():
    assert handle_get_account("account1") == "Account account1 balance: 100 EUR"

def test_get_account_not_found():
    with pytest.raises(NotFoundErr) as not_found:
        handle_get_account("account3")
    assert str(not_found.value) == "Account account3 not found"