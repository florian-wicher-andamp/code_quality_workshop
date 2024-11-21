from src.Transaction import Transaction
from src.fraud_detection.rules.FraudRule import FraudRule


class TransferringMostOfBalanceIsSuspiciousRule(FraudRule):
    def is_suspicious(self, transaction: Transaction) -> bool:
        return transaction.amount > transaction.from_account.balance * (2 / 3)