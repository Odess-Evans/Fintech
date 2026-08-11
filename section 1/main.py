import json
from pathlib import Path
from datetime import datetime

from risk_and_fraud.transaction_risk import evaluate_risk, check_velocity


BASE_DIR = Path(__file__).resolve().parent
TRANSACTION_FILE = BASE_DIR / "risk_and_fraud" / "transactions.json"


def load_transactions():
    with open(TRANSACTION_FILE, "r") as file:
        data = json.load(file)

    return data["transactions"]


def save_transaction(transaction):
    with open(TRANSACTION_FILE, "r") as file:
        data = json.load(file)

    data["transactions"].append(transaction)

    with open(TRANSACTION_FILE, "w") as file:
        json.dump(data, file, indent=4)


customer = input("Enter recipient name: ").strip()
amount = float(input("Enter transaction amount: "))
country_code = input("Enter country code: ").strip().upper()
transactions = load_transactions()

is_first_time = True

for transaction in transactions:
    if transaction["name"].lower() == customer.lower():
        is_first_time = False
        break

risk = evaluate_risk(
    amount,
    country_code,
    is_first_time
)

velocity_risk = check_velocity(
    transactions,
    customer
)

if velocity_risk:
    risk = True

if risk:
    print("Transaction flagged as suspicious.")
else:
    print("Transaction approved.")

new_transaction = {
    "name": customer,
    "amount": amount,
    "country_code": country_code,
    "timestamp": datetime.now().isoformat(),
    "suspicious": risk
}

save_transaction(new_transaction)
