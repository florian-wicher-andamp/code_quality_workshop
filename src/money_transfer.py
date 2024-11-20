exchange_rates = {
    "USD": 1.0,
    "EUR": 0.9,
}

accounts = {}


def create_account(account_name: str, amount: float, currency: str):
    if amount < 0:
        raise ValueError("Initial balance cannot be negative.")
    if currency not in exchange_rates:
        raise ValueError(f"Unsupported currency: {currency}")
    account = {
        'balance': amount,
        'currency': currency
    }
    accounts[account_name] = account
    print(f"Account '{account_name}' created with balance {amount} {currency}.")
    return account


def transfer_money(from_account_name: str, amount: float, currency: str, to_account_name: str):
    if amount <= 0:
        raise ValueError("Transfer amount must be greater than zero.")
    if currency not in exchange_rates:
        raise ValueError(f"Unsupported currency: {currency}")

    from_account = accounts[from_account_name]
    to_account = accounts[to_account_name]

    if from_account is None:
        raise ValueError(f"Account '{from_account_name}' not found.")
    if to_account is None:
        raise ValueError(f"Account '{to_account_name}' not found.")
    if from_account['balance'] < amount:
        raise ValueError(f"Insufficient funds in '{from_account_name}'.")

    from_account['balance'] -= convert_currency(amount, currency, from_account['currency'])
    to_account['balance'] += convert_currency(amount, currency, to_account['currency'])
    print(f"Transferred {amount} {currency} from '{from_account_name}' to '{to_account_name}'")

def convert_currency(amount: float, from_currency: str, to_currency: str):
    global exchange_rates
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print(f"Unsupported currency conversion from {from_currency} to {to_currency}.")
        return None

    base_amount = amount / exchange_rates[from_currency]
    target_amount = base_amount * exchange_rates[to_currency]
    return target_amount

def show_account(account_name:str):
    account = accounts.get(account_name)
    if account:
        print(f"Account '{account_name}': Balance = {account['balance']} {account['currency']}")
    else:
        print(f"Account '{account_name}' not found.")


if __name__ == "__main__":
    create_account("Alice", 100, "USD")
    create_account("Bob", 0, "EUR")

    transfer_money("Alice", 50, "USD", "Bob")

    show_account("Alice")
    show_account("Bob")
