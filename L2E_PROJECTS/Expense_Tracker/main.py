from Models.expense import Expense
from expense_manager import ExpenseManager
import os

# e = Expense("Food", 200.0, "To eat")
# print(e)
# print(vars(e))
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("\n\n\n====== EXPENSE TRACKER ======")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Expenses By Category")
    print("4. Find Expense")
    print("5. Update Expense")
    print("6. Delete Expense")
    print("7. View Total")
    print("0. Exit")

manager = ExpenseManager()
manager.read_expenses()
choice = ""

CATEGORIES = ["Food", "Transport", "Enjoyment"]
# while choice != "0":
while True:
    display_menu()
    choice = input("Choose an option: ")
    match choice:

        case "1":
            for number, category in enumerate(CATEGORIES, start=1):
                print(f"{number}. {category}")
            custom_category = len(CATEGORIES)+1
            print(f"{custom_category}. Enter my own category")
            cat = input("Enter an option: ")
            if cat == "4":
                new_category = input("Enter your category name: ")
                CATEGORIES.append(new_category)
            cat = CATEGORIES[int(cat) -1]
            while True:
                try:
                    amt = float(input("Enter the expense amount: "))
                    break
                except ValueError:
                    print("Amount must be a number.")
            descrp = input("What was the expense for? Add a description: ")
            expense = Expense(cat, amt, descrp)
            manager.add_expense(expense)
            print(f"Expense added successfully!\nCategory: {cat}\nAmount: {amt}\n")
            input("Press enter to continue...")
        case "2":
            manager.view_expenses()
            input("Press enter to continue...")

        case "3":
            search_cat = input("What expense category do you want to get?: ")
            manager.view_expenses_by_category(search_cat)
            input("Press enter to continue...")

        case "4":
            find_expense_id = int(input("What is the id of the expense you want to search?: "))
            manager.get_expense_by_id(find_expense_id)
            input("Press enter to continue...")

        case "5":
            # manager.read_expenses()
            print("Available expenses:")
            manager.view_expenses()
            update_expense_id = input("What is the id of the expense you want to update?: ")
            expense = manager.get_expense_by_id(update_expense_id)

            if expense is None:
                print(f"Expense with id {update_expense_id} does not exist.")
            else:
                option = input("Which property do you want to change? Enter 'category', 'amount', or 'description': ")
                if option.lower == "Category":
                    new_category = input("What category do you want change to?: ")
                elif option.lower == "Amount":
                    new_amount = input("What is the new amount?: ")
                elif option.lower == "Description":
                    new_description = input("What is the new description?: ")
                else:
                    print("Please select a valid property.")
            manager.update_expense_by_id(update_expense_id, new_category, new_amount, new_description)
            input("Press enter to continue...")

        case "6":
            print("Available expenses:")
            manager.view_expenses()
            delete_expense_id = input("Enter the id of the expense you want to delete: ")
            manager.delete_expense_by_id(delete_expense_id)
            input("Press enter to continue...")

        case "7":
            manager.view_total_expense_amount()
            input("Press enter to continue...")

        case "0":
            print("Thank you for using the expense tracker, we'd love to see you again.")
            break

        case _:
            print("Invalid entry. Please, choose from the menu.")

