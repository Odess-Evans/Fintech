from datetime import datetime


class Transaction:

    def __init__(self, tx_id, sender, receiver, amount):
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        self.__tx_id = tx_id
        self.__sender = sender
        self.__receiver = receiver
        self.__amount = amount
        self.__timestamp = datetime.now()
        self.__status = "Pending"

    @property
    def tx_id(self):
        return self.__tx_id

    @property
    def sender(self):
        return self.__sender

    @property
    def receiver(self):
        return self.__receiver

    @property
    def amount(self):
        return self.__amount

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def status(self):
        return self.__status

    def complete(self):
        self.__status = "Completed"

    def fail(self):
        self.__status = "Failed"