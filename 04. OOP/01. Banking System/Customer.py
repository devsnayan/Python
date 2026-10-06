class Customer:

    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def get_info(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    def display_info(self):
        print(f"Customer ID : {self.customer_id}")
        print(f"Name        : {self.name}")
        print(f"Email       : {self.email}")
        print(f"Phone       : {self.phone}")