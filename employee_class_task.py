
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        print(f"{self.first_name} {self.last_name}")

    def email(self):
        print((f"{self.first_name}.{self.last_name}@company.com").lower())


combined = Employee(first_name= "Linas", last_name= "Juska")

combined.full_name()
combined.email()
