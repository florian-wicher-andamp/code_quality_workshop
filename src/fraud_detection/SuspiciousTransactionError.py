

class SuspiciousTransactionError(Exception):
    def __init__(self, transaction, message=""):
        super().__init__(f"The transaction {transaction} is suspicious and will not be processed.{message}")
        self.transaction = transaction