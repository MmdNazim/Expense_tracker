# #Expense Information:
def expense_info():
    expense_id = input("Expense ID: ")
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = int(input("Amount:"))
    user_inputs = f"{expense_id},{date},{category},{description},{amount}\n"
    with open("expenses.txt", "a") as file:
     file.write(user_inputs)
     print("Data successfully added")
expense_info()

#Menu:
print("=================Expense Tracker================")

def main():
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expense")
    print("4. Update Expense")
    print("5. Delete Expense")
    print("6. Expense Summary")
    print("7. Exit")

    choice = input("Choose an option: ")
main()

#Functional Requirements: 1. Add Expense
def add_expense():
    expense_id = input("Expense ID: ")
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    description = input("Description: ")
    amount = int(input("Amount:"))
    user_inputs = f"{expense_id},{date},{category},{description},{amount}\n"
    with open("expenses.txt", "a") as file:
     file.write(user_inputs)
     print("Data successfully added")
add_expense()

#Functional Requirements: 2. View All Expenses
def view_expenses():
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            expense_id, date, category, description, amount = parts
            print("-" * 30)
            print(f"Expense ID:{expense_id}")
            print(f"Date: {date}")
            print(f"Category: {category}")
            print(f"Description: {description}")
            print(f"Amount: {amount}")
            print("-" * 30)
view_expenses()

#Functional Requirements: 3. Search Expense
def search_expense():
    search_id = input("Search by expense id: ")
    found = False
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            expense_id, date, category, description, amount = parts
            if search_id == expense_id:
                found = True
                print("Expense Found")
                print(f"Expense ID:{expense_id}")
                print(f"Date: {date}")
                print(f"Category: {category}")
                print(f"Description: {description}")
                print(f"Amount: {amount}")
                break
        if found == False:
             print("Expense not found.")
search_expense()


#Functional Requirements: 4. Update Expense
def update_expense():
    search_id = input("Updated expense id: ")
    found = False
    updated_lines = []
    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            expense_id, date, category, description, amount = parts
            if search_id == expense_id:
                found = True
                # print("\nExpense Found!")
                # print(f"Expense ID : {expense_id}")
                # print(f"Date : {date}")
                # print(f"Category : {category}")
                # print(f"Description : {description}")
                # print(f"Amount : {amount}")
                date = input("Update Date (YYYY-MM-DD): ")
                category = input("Update Category: ")
                description = input("Update Description: ")
                amount = input("Update Amount: ")
                updated_line = f"{expense_id},{date},{category},{description},{amount}\n"
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)
    if found:
        with open("expenses.txt", "w") as file:
            for line in updated_lines:
                file.write(line)
        print("Expense updated successfully.")

    else:
        print("Expense not found.")

update_expense()


#Functional Requirements: 5. Delete Expense
def delete_expense():
    search_id = input("Enter Expense ID to delete: ")
    found = False
    updated_lines = []

    with open("expenses.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")

            expense_id, date, category, description, amount = parts

            if search_id == expense_id:
                found = True
                print("Expense deleted successfully.")
                continue     

            updated_lines.append(line)

    if found:
        with open("expenses.txt", "w") as file:
            for line in updated_lines:
                file.write(line)
    else:
        print("Expense not found.")
delete_expense()


#Functional Requirements: 6. Expense Summary
def expense_summary():
        amounts = []
        with open("expenses.txt", "r") as file:
            for line in file:
                 parts = line.strip().split(",")
                 expense_id, date, category, description, amount = parts
                 amounts.append(float(amount))

        total_expenses = len(amounts)
        total_spending = sum(amounts)
        average = total_spending / total_expenses
        highest = max(amounts)
        lowest = min(amounts)

        print("========= Expense Summary =========")
        print("Total Expenses :", total_expenses)
        print("Total Spending :", total_spending, "BDT")
        print("Average Expense :", average, "BDT")
        print("Highest Expense :", highest, "BDT")
        print("Lowest Expense :", lowest, "BDT")
expense_summary()

#Functional Requirements: 7. Exit
def main():
    while True:
        print("\n========= Expense Tracker =========")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Expense Summary")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            update_expense()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            expense_summary()

        elif choice == "7":
            print("Thank you for using Expense Tracker.")
            break

        else:
            print("Invalid choice! Please select a valid option.")

main()

#Exception Handling: Invalid Amount

try:
    amount = float(input("Amount: "))

except ValueError:
    print("Invalid amount! Please enter a valid number.")

# #Exception Handling: Negative Amount
# try:
#     amount = float(input("Amount: "))

#     if amount < 0:
#         print("Amount cannot be negative.")
#         return

# except ValueError:
#     print("Invalid amount! Please enter a valid number.")
#     return