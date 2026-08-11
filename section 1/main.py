import json
from pathlib import Path
from datetime import datetime


from risk_and_fraud.transaction_risk import evaluate_risk, check_velocity
from lending.loan_eligibility import calculate_loan
from account_services.account_sanitizer import sanitize_account_number


# BASE_DIR = Path(__file__).resolve().parent
# TRANSACTION_FILE = BASE_DIR / "risk_and_fraud" / "transactions.json"


# def load_transactions():
#     with open(TRANSACTION_FILE, "r") as file:
#         data = json.load(file)

#     return data["transactions"]


# def save_transaction(transaction):
#     with open(TRANSACTION_FILE, "r") as file:
#         data = json.load(file)

#     data["transactions"].append(transaction)

#     with open(TRANSACTION_FILE, "w") as file:
#         json.dump(data, file, indent=4)


# customer = input("Enter recipient name: ").strip()
# amount = float(input("Enter transaction amount: $"))
# country_code = input("Enter country code: ").strip().upper()
# transactions = load_transactions()

# is_first_time = True

# for transaction in transactions:
#     if transaction["name"].lower() == customer.lower():
#         is_first_time = False
#         break

# risk = evaluate_risk(
#     amount,
#     country_code,
#     is_first_time
# )

# velocity_risk = check_velocity(
#     transactions,
#     customer
# )

# if velocity_risk:
#     risk = True

# if risk:
#     print("Transaction flagged as suspicious.")
# else:
#     print("Transaction approved.")

# new_transaction = {
#     "name": customer,
#     "amount": f"${amount}",
#     "country_code": country_code,
#     "timestamp": datetime.now().isoformat(),
#     "suspicious": risk
# }

# save_transaction(new_transaction)








# LOAN ELIGIBILITY
# print("LOAN ELIGIBILITY CALCULATOR")

# credit_score = int(input("Enter credit score: "))
# annual_income = float(input("Enter annual income: "))
# debt_ratio = float(input("Enter debt ratio: "))

# status, interest_rate = calculate_loan(
#     credit_score,
#     annual_income,
#     debt_ratio
# )

# print("Loan Status:", status)

# if status == "Approved":
#     print("Interest Rate:", interest_rate, "%")
# else:
#     print("Interest Rate: Not applicable")










# account_sanitizer
print("ACCOUNT NUMBER SANITIZER")

account_number = input("Enter account number: ")

sanitized_number = sanitize_account_number(account_number)

if sanitized_number is not None:
    print("Sanitized account number:", sanitized_number)
else:
    print("Invalid account number. Account number must contain exactly 10 digits.")
