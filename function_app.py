import logging
from xml.dom import NotFoundErr

import azure.functions as func
from azure.functions import AuthLevel

from src.Account import Account
from src.Currency import Euro
from src.MoneyAmount import MoneyAmount
from src.fraud_detection.SuspiciousTransactionError import SuspiciousTransactionError

app = func.FunctionApp(http_auth_level=AuthLevel.ANONYMOUS)

accounts = [
    Account("account1", MoneyAmount(100, Euro())),
    Account("account2", MoneyAmount(50, Euro()))
]


def find_account(name):
    try:
        return [account for account in accounts if account.name == name][0]
    except IndexError:
        raise NotFoundErr(f"Account {name} not found")


@app.route(route="transfer", methods=["POST"])
def transfer(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        from_account_id = req_body.get('from_account')
        to_account_id = req_body.get('to_account')
        amount = req_body.get('amount')
        currency = req_body.get('currency')

        try:
            result = handle_transfer(from_account_id, to_account_id, amount, currency)
        except NotFoundErr as e:
            return func.HttpResponse(str(e), status_code=400)

        return func.HttpResponse(result, status_code=200)
    except SuspiciousTransactionError as e:
        return func.HttpResponse(str(e), status_code=400)
    except Exception as e:
        logging.error(f"Error during transfer: {e}")
        return func.HttpResponse("Error during transfer", status_code=500)


def handle_transfer(from_account_id, to_account_id, amount, currency):
    from_account = find_account(from_account_id)
    to_account = find_account(to_account_id)
    if not from_account or not to_account:
        return func.HttpResponse("Account not found", status_code=404)

    money_amount = MoneyAmount(amount, Euro())
    from_account.transfer(money_amount, to_account)

    return f"Transferred {amount} {currency} from {from_account_id} to {to_account_id}"


@app.route(route="account", methods=["GET"])
def get_account(req: func.HttpRequest) -> func.HttpResponse:
    account_id = req.params.get('id')
    if not account_id:
        return func.HttpResponse("Account ID is required", status_code=400)

    try:
        account = handle_get_account(account_id)
    except NotFoundErr as e:
        return func.HttpResponse(str(e), status_code=404)
    return func.HttpResponse(account, status_code=200)


def handle_get_account(name) -> str:
    account = find_account(name)
    if not account:
        raise NotFoundErr(f"Account {name} not found")

    return f"Account {name} balance: {account.balance}"
