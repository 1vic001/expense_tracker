import json
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expense_list = []

    def save(self):
            data = {"expenses": [expense.to_dict() for expense in self.expense_list]}
            with open("expense_list.json", "w") as file:
                json.dump(data, file, indent=4)


    def load(self):
        try:
            with open("expense_list.json", "r") as file:
                loaded_file = json.load(file)
                self.expense_list.extend(Expense.from_dict(expense) for expense in loaded_file["expenses"])
        except FileNotFoundError:
            print("No save file available")

    def add_expense(self, expense):
        self.expense_list.append(expense)
        print("Expense added")

    @staticmethod
    def print_expenses(expense_list):
        print("NAME | AMOUNT | CATEGORY | DATE")
        for index, expense in enumerate(expense_list):
            print(f"{index+1}. {expense.name} | {expense.amount:.2f}$ | {expense.category} | {expense.date.strftime('%d-%m-%Y')}")

    def show_expenses(self):
        print("1. Name")
        print("2. Amount")
        print("3. Category")
        print("4. Date")
        choice = input("Enter sorting category (1-4): ")
        match choice:
            case "1":
                name_list = sorted(self.expense_list, key=lambda e: e.name)
                self.print_expenses(name_list)
            case "2":
                amount_list = sorted(self.expense_list, key=lambda e: e.amount, reverse=True)
                self.print_expenses(amount_list)
            case "3":
                category_list = sorted(self.expense_list, key=lambda e: e.category)
                self.print_expenses(category_list)
            case "4":
                date_list = sorted(self.expense_list, key=lambda e: e.date)
                self.print_expenses(date_list)
            case _:
                print("Invalid choice")

    def summary(self):
        total = sum(expense.amount for expense in self.expense_list)
        print(f"Total spent: {total:.2f}$")
        print("By category: ")
        category_list = {} #{category:[amount]}
        for expense in self.expense_list:
            if expense.category in category_list:
                category_list[expense.category].append(expense.amount)
            else:
                category_list.update({expense.category:[expense.amount]})
        for category in category_list.keys():
            print(f"{category}: {sum(category_list[category]):.2f}$")

class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = float(amount)
        self.category = category
        self.date = datetime.now()

    def to_dict(self):
        data = {"name":self.name, "amount":self.amount, "category":self.category, "date":datetime.strftime(self.date, "%d-%m-%Y")}
        return data

    @classmethod
    def from_dict(cls, data):
        new_expense = cls(data["name"], data["amount"], data["category"])
        new_expense.date = datetime.strptime(data["date"], "%d-%m-%Y")
        return new_expense

def main():
    expense_tracker = ExpenseTracker()
    expense_tracker.load()
    while True:
        print("1. Add expense")
        print("2. Show expenses")
        print("3. Summary")
        print("4. Save & Quit")
        choice = input("Enter choice: ")
        match choice:
            case "1":
                name = input("Enter expense name: ").lower()
                category = input("Enter expense category: ").lower()
                amount = input("Enter expense amount: ")
                try:
                    amount = float(amount)
                except ValueError:
                    print("Not a valid number")
                    continue
                expense_tracker.add_expense(Expense(name, amount, category))
            case "2":
                expense_tracker.show_expenses()
            case "3":
                expense_tracker.summary()
            case "4":
                expense_tracker.save()
                break
            case _:
                print("Invalid choice")
                continue

if __name__ == "__main__":
    main()