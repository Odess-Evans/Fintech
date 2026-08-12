class Account:

    def __init__(self, account_number, account_holder, balance=0):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")

        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.__balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance.")

        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

    def get_account_holder(self):
        return self.__account_holder