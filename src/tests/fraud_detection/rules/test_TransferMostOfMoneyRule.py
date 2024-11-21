from src.Transaction import Transaction
from src.fraud_detection.rules.TransferringMostOfBalanceIsSuspiciousRule import \
    TransferringMostOfBalanceIsSuspiciousRule
from src.tests.fraud_detection.data import demo_accounts


def test_txn_suspicious_if_more_than_two_thirds_of_balance_is_sent():
    rule = TransferringMostOfBalanceIsSuspiciousRule()
    account1, account2 = demo_accounts()
    more_than_two_thirds_of_account1s_fortune = (account1.balance * (2 / 3)) + 1
    assert rule.is_suspicious(Transaction(account1, account2, more_than_two_thirds_of_account1s_fortune))

def test_txn_not_suspicious_if_less_than_two_thirds_of_balance_is_sent():
    rule = TransferringMostOfBalanceIsSuspiciousRule()
    account1, account2 = demo_accounts()
    less_than_two_thirds_of_account1s_fortune = account1.balance * (2 / 3) - 1
    assert not rule.is_suspicious(Transaction(account1, account2, less_than_two_thirds_of_account1s_fortune))