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
        for expense in self.expenses:
            if expense.category == category_search:
                print(f"Id: {expense.id}\nCategory: {expense.category}\nAmount: {expense.amount}\nDescription: {expense.description}")
                print()
                found = True
        if not found:
            print("Category not found.")

    def get_expense_by_id(self, identity_number):
        found_id = False
        for expense in self.expenses:
            if expense.id == identity_number:
                print(f"Id: {expense.id}\nCategory: {expense.category}\nAmount: {expense.amount}\nDescription: {expense.description}")
                found_id = True
                return expense
        if not found_id:
                print(f"Id {identity_number} does not exist.")

    def update_expense_by_id(self, id_search, new_category, new_amount, new_description):
        foundExistingExpense = False
        for existingExpense in self.expenses:
            if existingExpense.id == id_search:
                if new_category != "":
                    existingExpense.category = new_category
                if new_amount != "":
                    existingExpense.amount = float(new_amount)
                if new_description != "":
                    existingExpense.description = new_description
            foundExistingExpense = True
        if not foundExistingExpense:
            print(f"Expense with id {id_search} not found.")
        