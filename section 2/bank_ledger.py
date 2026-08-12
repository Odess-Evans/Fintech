from transaction import Transaction


class BankLedger:

    def __init__(self):
        self.__transactions = []

    def transfer(self, sender, receiver, amount):

        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")

        sender.withdraw(amount)
        receiver.deposit(amount)

        tx_id = len(self.__transactions) + 1

        transaction = Transaction(
            tx_id,
            sender.get_account_number(),
            receiver.get_account_number(),
            amount
        )

        transaction.complete()

        self.__transactions.append(transaction)

        return transaction

    def get_transactions(self):
        return self.__transactions.copy()

    def get_total_transactions(self):
        return len(self.__transactions)