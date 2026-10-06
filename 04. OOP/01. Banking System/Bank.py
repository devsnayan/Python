class Bank:

    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):

        self.customers.append(customer)

        print(
            f"Customer '{customer.name}' "
            f"created successfully."
        )

    def add_account(self, account):

        self.accounts.append(account)

        print(
            f"Account '{account.account_number}' "
            f"created successfully."
        )

    def find_customer(self, customer_id):

        for customer in self.customers:

            if customer.customer_id == customer_id:
                return customer

        return None

    def find_account(self, account_number):

        for account in self.accounts:

            if account.account_number == account_number:
                return account

        return None

    def show_customers(self):

        print("\n--- Customers ---")

        if not self.customers:
            print("No customers found.")
            return

        for customer in self.customers:
            customer.display_info()
            print()

    def show_accounts(self):

        print("\n--- Accounts ---")

        if not self.accounts:
            print("No accounts found.")
            return

        for account in self.accounts:
            account.show_account()