from _pytest.python_api import raises

from src.InsufficientFundsError import InsufficientFundsError
from src.Ledger import Transaction, Ledger
from src.MoneyAmount import MoneyAmount
from src.tests.CurrencyStub import EuroStub
from src.tests.fraud_detection.data import demo_accounts

EUR = EuroStub()


fiftyEuros = MoneyAmount(50, EUR)

def setup_function():
    global sender, receiver
    sender, receiver = demo_accounts()

def test_recording_a_transaction_adds_it_to_ledger():
    ledger = Ledger()
    ledger.record_transaction(Transaction(sender, receiver, fiftyEuros))
    assert len(ledger.transactions) == 1

def test_transaction_details_are_recorded_correctly():
    ledger = Ledger()
    ledger.record_transaction(Transaction(sender, receiver, MoneyAmount(50, EUR)))
    assert ledger.transactions[0] == Transaction(sender, receiver, MoneyAmount(50, EUR))


def test_transfer_is_recorded_in_ledger_of_sending_account():
    sender.transfer(fiftyEuros, receiver)
    assert sender.ledger.transactions[0] == Transaction(sender, receiver, fiftyEuros)

def test_transfer_is_recorded_in_ledger_of_receiving_account():
    transfer_amount = MoneyAmount(1, EUR)
    sender.transfer(transfer_amount, receiver)
    assert receiver.ledger.transactions[0] == Transaction(receiver, sender, transfer_amount)

def test_transaction_is_not_recorded_if_insufficient_funds():
    raises(InsufficientFundsError, sender.transfer, MoneyAmount(150, EUR), receiver)
    assert len(sender.ledger.transactions) == 0
    assert len(receiver.ledger.transactions) == 0

def test_get_transactions_returns_all_transactions():
    sender.transfer(MoneyAmount(1, EUR), receiver)
    sender.transfer(MoneyAmount(2, EUR), receiver)
    assert sender.ledger.transactions == [
        Transaction(sender, receiver, MoneyAmount(1, EUR)),
        Transaction(sender, receiver, MoneyAmount(2, EUR))
    ]


def test_str_returns_nice_string_representation():
    ledger = Ledger()
    sender, receiver = demo_accounts()
    ledger.record_transaction(Transaction(sender, receiver, MoneyAmount(50, EUR)))
    ledger.record_transaction(Transaction(sender, receiver, MoneyAmount(10, EUR)))
    assert (str(ledger) ==
            "Test1 -[50 EUR]-> Test2\n" +
            "Test1 -[10 EUR]-> Test2")

def test_suspicious_txn_shows_in_ledger_representation():
    ledger = Ledger()
    txn = Transaction(sender, receiver, MoneyAmount(50, EUR), is_suspicious=True)
    ledger.record_transaction(txn)
    assert str(ledger) == "Test1 -[50 EUR]-> Test2 (suspicious)"