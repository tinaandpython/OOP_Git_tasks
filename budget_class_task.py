class Record:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def __str__(self):
        return f"{self.type}: {self.amount}"


class Budget:

    def __init__(self):
        self.journal = []

    def add_income_record(self, amount):
        income_record = Record("Income", amount)
        self.journal.append(income_record)

    def add_expense_record(self, amount):
        expense_record = Record("Expense", amount)
        self.journal.append(expense_record)

    def get_balance(self):
        total = 0
        for record in self.journal:
            if record.type == "Income":
                total += record.amount
            if record.type == "Expense":
                total -= record.amount
        print(total)

    def show_report(self):
        for record in self.journal:
            print(f"{record.type}: {record.amount}")

budget = Budget()

while True:
    print("Please choose an option:")
    print("1. Enter income")
    print("2. Enter expense")
    print("3. View balance")
    print("4. View budget report")
    print("5. Exit")
    option = int(input("Select your option: "))
    if option == 1:
        amount = float(input("Enter the income amount: "))
        budget.add_income_record(amount)
    elif option == 2:
        amount = float(input("Enter the expense amount: "))
        budget.add_expense_record(amount)
    elif option == 3:
        budget.get_balance()
    elif option == 4:
        budget.show_report()
    elif option == 5:
        print("Thank you for using the budget program")
        exit()
    else:
        print("The selected option does not exist")