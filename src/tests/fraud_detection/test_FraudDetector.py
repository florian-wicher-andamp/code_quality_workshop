from unittest.mock import MagicMock

from src.MoneyAmount import MoneyAmount
from src.Transaction import Transaction
from src.fraud_detection.FraudDetector import FraudDetector
from src.tests.CurrencyStub import EuroStub
from src.tests.fraud_detection.data import demo_account1, demo_account2

EUR = EuroStub()

def everything_suspicious_rule():
    rule = MagicMock()
    rule.is_suspicious.return_value = True
    return rule

def nothing_suspicious_rule():
    rule = MagicMock()
    rule.is_suspicious.return_value = False
    return rule

demo_txn = Transaction(demo_account1(), demo_account2(), MoneyAmount(100, EUR))

def test_if_rule_fails_the_txn_is_suspicious():
    detector = FraudDetector([everything_suspicious_rule()])
    assert detector.is_suspicious(demo_txn)

def test_if_one_of_many_rules_fails_then_txn_is_suspicious():
    detector = FraudDetector([(everything_suspicious_rule()), (nothing_suspicious_rule())])
    assert detector.is_suspicious(demo_txn)

def test_if_all_rules_pass_then_txn_is_not_suspicious():
    detector = FraudDetector([nothing_suspicious_rule(), nothing_suspicious_rule()])
    assert not detector.is_suspicious(demo_txn)