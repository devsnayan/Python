from abc import ABC, abstractmethod
from Transaction import Transaction


class BankAccount(ABC):

    def __init__(self, account_number, customer, balance=0):
        self.account_number = account_number
        self.customer = customer

        # Encapsulation
        self.__balance = balance

        self.transactions = []

    def deposit(self, amount):

        if amount <= 0:
            print("Amount must be greater than 0.")
            return False

        self.__balance += amount

        transaction = Transaction(
            "Deposit",
            amount
        )

        self.transactions.append(transaction)

        print(f"{amount} deposited successfully.")

        return True

    def withdraw(self, amount):

        if amount <= 0:
            print("Amount must be greater than 0.")
            return False

        if amount > self.__balance:
            print("Insufficient balance.")
            return False

        self.__balance -= amount

        transaction = Transaction(
            "Withdrawal",
            amount
        )

        self.transactions.append(transaction)

        print(f"{amount} withdrawn successfully.")

        return True

    def get_balance(self):
        return self.__balance

    def show_account(self):

        print("\n--- Account Information ---")
        print(f"Account Number : {self.account_number}")
        print(f"Customer       : {self.customer.name}")
        print(f"Account Type   : {self.account_type}")
        print(f"Balance        : {self.__balance}")

    def show_transactions(self):

        print("\n--- Transaction History ---")

        if not self.transactions:
            print("No transactions found.")
            return

        for transaction in self.transactions:
            transaction.display()

    @abstractmethod
    def calculate_interest(self):
        pass


class SavingsAccount(BankAccount):

    def __init__(
        self,
        account_number,
        customer,
        balance=0,
        interest_rate=5
    ):
        super().__init__(
            account_number,
            customer,
            balance
        )

        self.account_type = "Savings"
        self.interest_rate = interest_rate

    def calculate_interest(self):

        return (
            self.get_balance()
            * self.interest_rate
            / 100
        )

    def withdraw(self, amount):

        minimum_balance = 500

        if self.get_balance() - amount < minimum_balance:
            print(
                f"Savings account must maintain "
                f"{minimum_balance} minimum balance."
            )
            return False

        return super().withdraw(amount)


class CurrentAccount(BankAccount):

    def __init__(
        self,
        account_number,
        customer,
        balance=0
    ):
        super().__init__(
            account_number,
            customer,
            balance
        )

        self.account_type = "Current"

    def calculate_interest(self):

        return 0