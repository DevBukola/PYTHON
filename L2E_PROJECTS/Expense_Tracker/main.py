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

            while True:
                cat = input("Enter an option: ").strip()
                if not cat.isdigit():
                    print("Please enter a number.")
                    continue
                cat_num = int(cat)
                if cat_num < 1 or cat_num > custom_category:
                    print("Please choose a valid option.")
                    continue
                break

            if cat_num == custom_category:
                while True:
                    new_category = input("Enter your category name: ")
                    if new_category == "" or new_category.isdigit():
                        print("category name cannot be empty, and cannot be a digit.")
                        continue
                    elif len(new_category) <= 3:
                        print("Length of category name must be greater than three.")
                        continue
                    elif not new_category.isalpha():
                        print("This contains something other than alphabets.")
                        continue
                    CATEGORIES.append(new_category)
                    cat = new_category
                    break
            else:
                cat = CATEGORIES[cat_num - 1]

            while True:
                try:
                    amt = input("Enter the expense amount: ")
                    if amt == "":
                        print("Amount cannot be empty.")
                        continue
                    elif float(amt) < -1:
                        print("Amount cannot be negative.")
                        continue
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
            while True:
                update_expense_id = input("What is the id of the expense you want to update?: ")
                if update_expense_id == "" or not update_expense_id.isdigit():
                    print("Id cannot be empty, and must be a digit")
                    continue
                expense = manager.get_expense_by_id(update_expense_id)
                break

            if expense is None:
                print(f"Expense with id {update_expense_id} does not exist.")
            else:
                new_category = ""
                new_amount = ""
                new_description = ""

                #asking until a valid property is chosen.
                while True:
                    option = input("Which property do you want to change? Enter 'category', 'amount', or 'description': ")
                    option = option.strip().lower()
                    if option in ("category", "amount", "description"):
                        break
                    print("Please select a valid property.")

                #asking until a non-empty value is given
                while True:
                    new_value = input(f"What is the new {option}: ").strip()
                    if new_value == "":
                        print(f"{option} cannot be empty.")
                        continue
                    if option == "category" and (len(new_value) <= 3 or not new_value.isalpha()):
                        print(f"Category must be longer than three characters and contain only letters.")
                        continue
                    if option == "description" and (len(new_value) <= 3 or not new_value.isalpha()):
                        print("Description must be longer than three characters and contain only letters.")
                        continue
                    if option == "amount":
                        try:
                            if float(new_value) < 0:
                                print("Amount cannot be negative.")
                                continue
                        except ValueError:
                            print("Amount must be a number.")
                            continue
                    break

                if option == "category":
                    new_category = new_value
                elif option == "amount":
                        new_amount = new_value
                elif option == "description":
                        new_description = new_value

                if manager.update_expense_by_id(update_expense_id, new_category, new_amount, new_description):
                        print("Expense updated successfully!")
                else:
                        print(f"Expense with id {update_expense_id} not found.")
                input("Press enter to continue...")

        case "6":
            print("Available expenses:")
            manager.view_expenses()
            delete_expense_id = input("Enter the id of the expense you want to delete: ")
            expense = manager.get_expense_by_id(delete_expense_id)

            if expense is None:
                print(f"Expense with id {delete_expense_id} does not exist.")
            else:
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

