class Student:

    def __init__(
        self,
        student_id,
        name,
        email,
        age,
        department
    ):
        self.id = student_id
        self.name = name
        self.email = email
        self.age = age
        self.department = department

    def is_adult(self):
        return self.age >= 18

    def get_info(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "age": self.age,
            "department": self.department
        }

    def __str__(self):
        return (
            f"{self.id} - "
            f"{self.name} - "
            f"{self.email}"
        )