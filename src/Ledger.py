from src.Transaction import Transaction


class Ledger:
    def __init__(self):
        self.transactions: [Transaction] = []

    def record_transaction(self, transaction: Transaction):
        self.transactions += [transaction]

    def __str__(self):
        return "\n".join(str(transaction) for transaction in self.transactions)

    def __repr__(self):
        return f"Ledger with {len(self.transactions)} transactions"