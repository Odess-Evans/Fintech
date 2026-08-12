import json
from pathlib import Path
from datetime import datetime


from risk_and_fraud.transaction_risk import evaluate_risk, check_velocity
from lending.loan_eligibility import calculate_loan
from account_services.account_sanitizer import sanitize_account_number
from cash_management.cash_flow_reconciler import reconcile_cash_flow
from foreign_exchange.fx_converter import convert_currency
from banking_reports.statement_date_formatter import format_statement_date
from compliance_and_kyc.kyc_validator import validate_kyc


# print("TRANSACTION RISK SCORING ENGINE")
# print("-------------------------------")

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
# print("---------------------------")

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
# print("ACCOUNT NUMBER SANITIZER")
# print("------------------------")

# account_number = input("Enter account number: ")

# sanitized_number = sanitize_account_number(account_number)

# if sanitized_number is not None:
#     print("Sanitized account number:", sanitized_number)
# else:
#     print("Invalid account number. Account number must contain exactly 10 digits.")












# CASH FLOW RECONCILER
# BASE_DIR = Path(__file__).resolve().parent

# CASH_FLOW_FILE = (
#     BASE_DIR / "cash_management" / "cash_flow.json"
# )


# with open(CASH_FLOW_FILE, "r") as file:
#     cash_flow = json.load(file)


# number_of_transactions = int(
#     input("How many transactions do you want to enter? ")
# )


# for i in range(number_of_transactions):

#     print(f"\nTransaction {i + 1}")

#     transaction_type = input(
#         "Enter type (credit/debit): "
#     ).strip().lower()

#     description = input(
#         "Enter description: "
#     ).strip()

#     amount = float(
#         input("Enter amount: ")
#     )

#     transaction = {
#         "type": transaction_type,
#         "description": description,
#         "amount": amount
#     }

#     cash_flow["transactions"].insert(0, transaction)


# with open(CASH_FLOW_FILE, "w") as file:
#     json.dump(cash_flow, file, indent=4)


# result = reconcile_cash_flow(cash_flow)


# print("\nDAILY CASH FLOW RECONCILER")
# print("--------------------------")

# print(
#     "Opening balance:",
#     result["opening_balance"]
# )
# print(
#     "Total credits:",
#     result["total_credits"]
# )
# print(
#     "Total debits:",
#     result["total_debits"]
# )
# print(
#     "Closing balance:",
#     result["closing_balance"]
# )
# print(
#     "Net change:",
#     result["net_change"]
# )









# # FX_CONVERTER
# amount = float(input("Enter amount in NGN: "))


# if amount <= 0:

#     print("Amount must be greater than zero.")

# else:

#     results = convert_currency(amount)

#     print("\nCURRENCY CONVERSION")
#     print("-------------------")

#     print(f"NGN {amount:,.2f}")

#     for currency, value in results.items():

#         print(f"{currency}: {value:,.2f}")









# ANOMALY DETECTOR
# from risk_and_fraud.anomaly_detector import detect_anomalies

# transactions = [
#     {
#         "tx_id": 101,
#         "amount": 50000
#     },
#     {
#         "tx_id": 102,
#         "amount": 45000
#     },
#     {
#         "tx_id": 103,
#         "amount": 55000
#     },
#     {
#         "tx_id": 104,
#         "amount": 500000
#     },
#     {
#         "tx_id": 105,
#         "amount": 40000
#     }
# ]


# anomalies = detect_anomalies(transactions)


# print("FRAUDULENT ANOMALY DETECTOR")
# print("----------------------------")

# if anomalies:

#     print("Suspicious transactions:")

#     for transaction in anomalies:
#         print(transaction)
# else:

#     print("No suspicious transactions found.")












# STATEMENT DATE FORMATTER
# timestamp = input("Enter timestamp: ")

# formatted_date = format_statement_date(timestamp)

# print("Formatted statement date:", formatted_date)











# KYC_VALIDATOR
bvn = input("Enter BVN: ").strip()
nin = input("Enter NIN: ").strip()
full_name = input("Enter full name: ").strip()
dob = input("Enter date of birth: ").strip()

user_data = {
    "bvn": bvn,
    "nin": nin,
    "full_name": full_name,
    "dob": dob
}

if validate_kyc(user_data):
    print("KYC data is valid.")
else:
    print("KYC data is invalid.")