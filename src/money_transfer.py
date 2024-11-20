accounts = {}

def create_account(account_name:str, amount:float):
    if amount < 0:
        raise ValueError("Initial balance cannot be negative.")
    account = {
        'balance': amount
    }
    accounts[account_name] = account
    print(f"Account '{account_name}' created with balance {amount}.")
    return account


def transfer_money(from_account_name:str, amount:float, to_account_name:str):
    if amount <= 0:
        raise ValueError("Transfer amount must be greater than zero.")

    from_account = accounts[from_account_name]
    to_account = accounts[to_account_name]

    if from_account is None:
        raise ValueError(f"Account '{from_account_name}' not found.")
    if to_account is None:
        raise ValueError(f"Account '{to_account_name}' not found.")
    if from_account['balance'] < amount:
        raise ValueError(f"Insufficient funds in '{from_account_name}'.")

    from_account['balance'] -= amount
    to_account['balance'] += amount
    print(f"Transferred {amount} from '{from_account_name}' to '{to_account_name}'.")

def show_account(account_name:str):
    account = accounts.get(account_name)
    if account:
        print(f"Account '{account_name}': Balance = {account['balance']}")
    else:
        print(f"Account '{account_name}' not found.")

if __name__ == "__main__":
    create_account("Alice", 100)
    create_account("Bob", 0)

    transfer_money("Alice", 50, "Bob")

    show_account("Alice")
    show_account("Bob")
