from datetime import timedelta

from src.fraud_detection.rules.FraudRule import FraudRule
from src.fraud_detection.rules.TransferringMostOfBalanceIsSuspiciousRule import \
    TransferringMostOfBalanceIsSuspiciousRule

instance = None
def fraud_detector():
    global instance
    if instance is None:
        instance = FraudDetector([
            TransferringMostOfBalanceIsSuspiciousRule(),
        ])
    return instance


class FraudDetector:
    def __init__(self, rules: [FraudRule]):
        self.rules = rules

    from src.Transaction import Transaction
    def is_suspicious(self, transaction: Transaction) -> bool:
        return any(rule.is_suspicious(transaction) for rule in self.rules)