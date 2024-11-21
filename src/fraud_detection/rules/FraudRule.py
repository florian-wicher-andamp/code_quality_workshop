from abc import ABC, abstractmethod
from src.Ledger import Transaction

class FraudRule(ABC):
    @abstractmethod
    def is_suspicious(self, transaction: Transaction) -> bool:
        pass