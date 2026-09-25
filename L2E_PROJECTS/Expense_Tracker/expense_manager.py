import json
from Models.expense import Expense

class ExpenseManager:
    def __init__(self): #automatically runs when an object is created.
        self.expenses = []

    def save_expenses(self):
        data = []
        for expense in self.expenses:
            data.append(vars(expense))

        with open("expenses.json", "w") as file:
            json.dump(data, file, indent=3)

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
            expense.id = "1"
        else:
            ids = []
            for existing_expense in self.expenses:
                ids.append(int((existing_expense.id)))
            expense.id = max(ids)+1
            expense.id = str(expense.id)
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
                print("No expense yet.\n\n")
                return
        for expense in self.expenses:
            print(f"Id: {expense.id}\nCategory: {expense.category}\nAmount: {expense.amount}\nDescription: {expense.description}")
            print()

    def view_expenses_by_category(self, category_search):
        found = False
        for expense in self.expenses:
            if expense.category.lower() == category_search.strip().lower():
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
        for existingExpense in self.expenses:
            if existingExpense.id == id_search:
                
                if new_category != "":
                    existingExpense.category = new_category
                if new_amount != "":
                    existingExpense.amount = float(new_amount)
                if new_description != "":
                    existingExpense.description = new_description
                self.save_expenses() #does not update the json file without this line.
                return True
        return False
            

    def delete_expense_by_id(self, id_delete):
        for expense in self.expenses:
            if expense.id == id_delete:
                self.expenses.remove(expense)
                print(f"Expense {expense.id} deleted successfully!")

                for remaining_expense in self.expenses:
                    if int(remaining_expense.id) > int(id_delete):
                        remaining_expense.id = str(int(remaining_expense.id) - 1)
                self.save_expenses()
                return True

        return False


    def view_total_expense_amount(self):
        total = 0
        for expense in self.expenses:
            # print(f"{expense.amount} + ")
            total += int(expense.amount)
        print(f"Total expenses is {total}.")