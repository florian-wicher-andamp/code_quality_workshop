from src.InsufficientFundsError import InsufficientFundsError
from src.MoneyAmount import MoneyAmount
from src.fraud_detection.SuspiciousTransactionError import SuspiciousTransactionError


class Account:
    def __init__(self, name, balance: MoneyAmount):
        assert name.isalnum()

        self.name = name
        self._balance:MoneyAmount = balance
        from src.Ledger import Ledger
        self.ledger = Ledger()

    def deposit(self, amount: MoneyAmount):
        self._balance += amount
        print(f"Deposited {amount} into '{self.name}'.")

    def withdraw(self, amount: MoneyAmount):
        self.assert_has_sufficient_funds(amount)
        self._balance -= amount
        print(f"Withdrew {amount} from '{self.name}'.")

    def assert_has_sufficient_funds(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError()

    def transfer(self, amount: MoneyAmount, other: 'Account'):
        from src.Transaction import Transaction
        self.assert_has_sufficient_funds(amount)
        transaction = Transaction(self, other, amount)
        from src.fraud_detection.FraudDetector import fraud_detector
        suspicious = fraud_detector().is_suspicious(transaction)
        if suspicious:
            transaction.suspicious = True
        else:
            self.withdraw(amount)
            other.deposit(amount)

        self.ledger.record_transaction(transaction)
        other.ledger.record_transaction(transaction.reverse())

        if suspicious:
            raise SuspiciousTransactionError(transaction)


    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        return 'Account ' + self.name

    def __str__(self):
        return f"{self.name} has a balance of {self.balance}."