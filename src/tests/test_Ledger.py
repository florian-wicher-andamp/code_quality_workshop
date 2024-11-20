from _pytest.python_api import raises

from src.Account import Account
from src.InsufficientFundsError import InsufficientFundsError
from src.MoneyAmount import MoneyAmount
from src.tests.CurrencyStub import EuroStub

EUR = EuroStub()

def accounts():
    return Account("Test1", MoneyAmount(100, EUR)), Account("Test2", MoneyAmount(50, EUR))

fiftyEuros = MoneyAmount(50, EUR)

def setup_function():
    global sender, receiver
    sender, receiver = accounts()

def test_recording_a_transaction_adds_it_to_ledger():
    ledger = Ledger()
    ledger.record_transaction(Transaction(sender.name, receiver.name, fiftyEuros))
    assert len(ledger.transactions) == 1

def test_transaction_details_are_recorded_correctly():
    ledger = Ledger()
    ledger.record_transaction(Transaction(sender.name, receiver.name, MoneyAmount(50, EUR)))
    assert ledger.transactions[0] == Transaction(sender.name, receiver.name, MoneyAmount(50, EUR))


def test_transfer_is_recorded_in_ledger_of_sending_account():
    sender.transfer(fiftyEuros, receiver)
    assert sender.ledger.transactions[0] == Transaction(sender.name, receiver.name, fiftyEuros)

def test_transfer_is_recorded_in_ledger_of_receiving_account():
    transferAmount = MoneyAmount(70, EUR)
    sender.transfer(transferAmount, receiver)
    assert receiver.ledger.transactions[0] == Transaction(receiver.name, sender.name, transferAmount)

def test_transaction_is_not_recorded_if_insufficient_funds():
    raises(InsufficientFundsError, sender.transfer, MoneyAmount(150, EUR), receiver)
    assert len(sender.ledger.transactions) == 0
    assert len(receiver.ledger.transactions) == 0

def test_get_transactions_returns_all_transactions():
    sender.transfer(MoneyAmount(70, EUR), receiver)
    sender.transfer(MoneyAmount(30, EUR), receiver)
    assert sender.ledger.transactions == [
        Transaction(sender.name, receiver.name, MoneyAmount(70, EUR)),
        Transaction(sender.name, receiver.name, MoneyAmount(30, EUR))
    ]


def test_str_returns_nice_string_representation():
    ledger = Ledger()
    sender, receiver = accounts()
    ledger.record_transaction(Transaction(sender.name, receiver.name, MoneyAmount(50, EUR)))
    ledger.record_transaction(Transaction(sender.name, receiver.name, MoneyAmount(10, EUR)))
    assert (str(ledger) ==
            "Test1 -[50 EUR]-> Test2\n" +
            "Test1 -[10 EUR]-> Test2")
