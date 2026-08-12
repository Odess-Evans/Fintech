import json
from pathlib import Path

from account import Account
from bank_ledger import BankLedger


DATA_FILE = Path(__file__).resolve().parent / "bank_data.json"


def load_data():

    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):

    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def main():

    data = load_data()

    print("BANKING SYSTEM")
    print("--------------")

    print("\nCREATE ACCOUNT")

    account_number_1 = input("Enter first account number: ")
    account_holder_1 = input("Enter first account holder name: ")
    balance_1 = float(input("Enter first account opening balance: "))

    account_number_2 = input("Enter second account number: ")
    account_holder_2 = input("Enter second account holder name: ")
    balance_2 = float(input("Enter second account opening balance: "))

    account1 = Account(
        account_number_1,
        account_holder_1,
        balance_1
    )

    account2 = Account(
        account_number_2,
        account_holder_2,
        balance_2
    )

    ledger = BankLedger()

    print("\nDEPOSIT")

    deposit_amount = float(
        input(
            f"Enter deposit amount for "
            f"{account1.get_account_holder()}: "
        )
    )

    account1.deposit(deposit_amount)

    print(
        f"{account1.get_account_holder()} balance:",
        account1.get_balance()
    )

    print("\nWITHDRAWAL")

    withdrawal_amount = float(
        input(
            f"Enter withdrawal amount for "
            f"{account2.get_account_holder()}: "
        )
    )

    account2.withdraw(withdrawal_amount)

    print(
        f"{account2.get_account_holder()} balance:",
        account2.get_balance()
    )

    print("\nTRANSFER")

    print(
        f"1. {account1.get_account_holder()} -> "
        f"{account2.get_account_holder()}"
    )

    print(
        f"2. {account2.get_account_holder()} -> "
        f"{account1.get_account_holder()}"
    )

    transfer_choice = input("Choose transfer direction: ")

    transfer_amount = float(
        input("Enter transfer amount: ")
    )

    if transfer_choice == "1":
        transaction = ledger.transfer(
            account1,
            account2,
            transfer_amount
        )
    elif transfer_choice == "2":

        transaction = ledger.transfer(
            account2,
            account1,
            transfer_amount
        )
    else:
        print("Invalid transfer choice.")
        return

    print("\nTRANSACTION DETAILS")
    print("-------------------")

    print("Transaction ID:", transaction.tx_id)
    print("Sender:", transaction.sender)
    print("Receiver:", transaction.receiver)
    print("Amount:", transaction.amount)
    print("Timestamp:", transaction.timestamp)
    print("Status:", transaction.status)

    print("\nFINAL BALANCES")
    print("--------------")

    print(
        account1.get_account_holder(),
        ":",
        account1.get_balance()
    )

    print(
        account2.get_account_holder(),
        ":",
        account2.get_balance()
    )

    # Save account information
    data["accounts"] = [
        {
            "account_number": account1.get_account_number(),
            "account_holder": account1.get_account_holder(),
            "balance": account1.get_balance()
        },
        {
            "account_number": account2.get_account_number(),
            "account_holder": account2.get_account_holder(),
            "balance": account2.get_balance()
        }
    ]

    # Save transaction
    data["transactions"].insert(0, {
        "tx_id": transaction.tx_id,
        "sender": transaction.sender,
        "receiver": transaction.receiver,
        "amount": transaction.amount
        "timestamp": str(transaction.timestamp),
        "status": transaction.status
    })

    save_data(data)
    print("\nData saved successfully.")


if __name__ == "__main__":
    main()