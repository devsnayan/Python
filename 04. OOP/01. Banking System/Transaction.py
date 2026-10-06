from datetime import datetime


class Transaction:

    def __init__(self, transaction_type, amount):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def get_info(self):
        return {
            "type": self.transaction_type,
            "amount": self.amount,
            "date": self.date
        }

    def display(self):
        print(
            f"{self.date} | "
            f"{self.transaction_type} | "
            f"{self.amount}"
        )