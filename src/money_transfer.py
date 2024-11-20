accounts = {}

def create_account(account_name, amount):
    account = {
        'balance': amount
    }
    accounts[account_name] = account
    print(f"Account '{account_name}' created with balance {amount}.")
    return account


def transfer_money(from_account_name, amount, to_account_name):
    from_account = accounts[from_account_name]
    to_account = accounts[to_account_name]

    from_account['balance'] -= amount
    to_account['balance'] += amount
    print(f"Transferred {amount} from '{from_account_name}' to '{to_account_name}'.")

def show_account(account_name):
    account = accounts.get(account_name)
    print(f"Account '{account_name}': Balance = {account['balance']}")

if __name__ == "__main__":
    create_account("Alice", 100)
    create_account("Bob", 0)

    transfer_money("Alice", 50, "Bob")

    show_account("Alice")
    show_account("Bob")
