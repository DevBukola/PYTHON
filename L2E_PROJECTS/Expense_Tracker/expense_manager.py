import json
from Models.expense import Expense

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def save_expenses(self):
        data = []
        for expense in self.expenses:
            data.append(vars(expense))

        with open("expenses.json", "w") as file:
            json.dump(data, file, indent=4)

    def read_expenses(self):
        try:
            with open("expenses.json", "r") as file:
                d = json.load(file)
        except FileNotFoundError:
            return
        for item in d:            
            self.expenses.append(Expense(item["category"], item["amount"], item["description"], item["id"]))

    def add_expense(self, expense):
        if not self.expenses: #if there is no expense already, the added expense get id of 1.
            expense.id = 1
        else:
            ids = []
            for existingIds in self.expenses:
                ids.append(existingIds.id)
            expense.id = max(ids)+1
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
                print("No expense yet.\n\n")
                return
        for expense in self.expenses:
            print(f"Id:{expense.id}\nCategory: {expense.category}\nAmount: {expense.amount}\nDescription: {expense.description}")
            print()

    def view_expenses_by_category(self, category_search):
        found = False
        for idx, expense in enumerate(self.expenses, start = 1):
            if expense.category == category_search:
                print(f"Id: {expense.id}\nCategory: {expense.category}\nAmount: {expense.amount}\nDescription: {expense.description}")
                print()
                found = True
        if not found:
            print("Category not found.")

        