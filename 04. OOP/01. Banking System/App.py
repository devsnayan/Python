from Bank import Bank
from Customer import Customer
from Account import SavingsAccount, CurrentAccount

bank = Bank()


def create_customer():

    print("\n--- Create Customer ---")

    customer_id = len(bank.customers) + 1

    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")

    customer = Customer(customer_id, name, email, phone)

    bank.add_customer(customer)


def create_account():

    print("\n--- Create Account ---")

    if not bank.customers:
        print("Please create a customer first.")
        return

    customer_id = int(input("Customer ID: "))

    customer = bank.find_customer(customer_id)

    if customer is None:
        print("Customer not found.")
        return

    print("\n1. Savings Account")
    print("2. Current Account")

    choice = input("Choose account type: ")

    account_number = f"ACC-{len(bank.accounts) + 1001}"

    balance = float(input("Initial Balance: "))

    if choice == "1":

        account = SavingsAccount(account_number, customer, balance)

    elif choice == "2":

        account = CurrentAccount(account_number, customer, balance)

    else:
        print("Invalid account type.")
        return

    bank.add_account(account)


def deposit_money():

    print("\n--- Deposit Money ---")

    account_number = input(
        "Account Number: "
    )

    account = bank.find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    amount = float(
        input("Amount: ")
    )

    account.deposit(amount)


def withdraw_money():

    print("\n--- Withdraw Money ---")

    account_number = input(
        "Account Number: "
    )

    account = bank.find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    amount = float(
        input("Amount: ")
    )

    account.withdraw(amount)


def show_balance():

    account_number = input(
        "Account Number: "
    )

    account = bank.find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    print(
        f"\nCurrent Balance: "
        f"{account.get_balance()}"
    )


def show_transactions():

    account_number = input(
        "Account Number: "
    )

    account = bank.find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    account.show_transactions()


def show_interest():

    account_number = input("Account Number: ")
    account = bank.find_account(account_number)

    if account is None:
        print("Account not found.")
        return

    interest = account.calculate_interest()

    print(
        f"Calculated Interest: {interest}"
    )


def main():

    while True:

        print("\n==============================")
        print("       BANKING SYSTEM")
        print("==============================")

        print("1. Create Customer")
        print("2. Create Account")
        print("3. Show Customers")
        print("4. Show Accounts")
        print("5. Deposit Money")
        print("6. Withdraw Money")
        print("7. Check Balance")
        print("8. Transaction History")
        print("9. Calculate Interest")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            create_customer()

        elif choice == "2":
            create_account()

        elif choice == "3":
            bank.show_customers()

        elif choice == "4":
            bank.show_accounts()

        elif choice == "5":
            deposit_money()

        elif choice == "6":
            withdraw_money()

        elif choice == "7":
            show_balance()

        elif choice == "8":
            show_transactions()

        elif choice == "9":
            show_interest()

        elif choice == "0":
            print("Thank you for using Banking System.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()