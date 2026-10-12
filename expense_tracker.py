# ================= Expense Tracker =================

# Helper Function: Get a Valid Amount
def get_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount < 0:
                print("Amount cannot be negative. Try again.")
                continue

            return amount

        except ValueError:
            print("Invalid amount! Please enter a number.")
# get_amount()

# Helper Function: Read Expense Records
def read_expenses():
    try:
        with open("expenses.txt", "r") as file:
            return[line.strip() for line in file if line.strip()]

    except FileNotFoundError:
        return []


#Functional Requirements: 1. Add Expense
def add_expense():
    expense_id = input("Enter Expense ID: ")
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")
    amount = get_amount()
    # Keep the description free of commas for this file format.
    records = f"{expense_id},{date},{category},{description},{amount}\n"

    with open("expenses.txt", "a") as file:
     file.write(records)

     print("Expense successfully added")


#Functional Requirements: 2. View All Expenses
def view_expenses():
    records = read_expenses()

    if not records:
        print("No expense record found")
        return

    print("=================Expense Tracker================")

    for record in records:
        parts = record.split(",", 4)

        if len(parts) == 5:
            expense_id, date, category, description, amount = parts

            print(f"Expense ID:{expense_id}")
            print(f"Date: {date}")
            print(f"Category: {category}")
            print(f"Description: {description}")
            print(f"Amount: {amount}")
            print("-" * 30)



#Functional Requirements: 3. Search Expense
def search_expense():
    search_id = input("Enter Expense ID to search: ")
    records = read_expenses()

    for record in records:
        parts = record.split(",", 4)


        if len(parts) == 5 and parts[0] == search_id:
                      print("\nExpense Found")
                      print(f"Expense ID:{parts[0]}")
                      print(f"Date: {parts[1]}")
                      print(f"Category: {parts[2]}")
                      print(f"Description: {parts[3]}")
                      print(f"Amount: {parts[4]}")
                      return

    print("Expense not found.")



#Functional Requirements: 4. Update Expense
def update_expense():
    update_id = input("Enter Expense ID to update: ")
    records = read_expenses()
    updated_records = []
    found = False

    for record in records:
                parts = record.split(",", 4)

                if len(parts) == 5 and parts[0] == update_id:
                     print("Enter the updated information: ")

                     date = input("Enter new Date (YYYY-MM-DD): ")
                     category = input("Enter new Category: ")
                     description = input("Enter new Description: ")
                     amount = get_amount()

                     new_record = f"{update_id},{date},{category},{description},{amount}\n"

                     updated_records.append(new_record)
                     found = True

                else:
                     updated_records.append(record)


    if found:
        with open("expenses.txt", "w") as file:
            for record in updated_records:
                file.write(record + "\n")

        print("Expense updated successfully.")


    else:    
        print("Expense not found.")



#Functional Requirements: 5. Delete Expense
def delete_expense():
    delete_id = input("Enter Expense ID to delete: ")
    records = read_expenses()
    remaining_records = []
    found = False

    for record in records:
        parts = record.split(",", 4)

        if len(parts) == 5 and parts[0] == delete_id:
            found = True
        else:
            remaining_records.append(record)


    if found:
            with open("expenses.txt", "w") as file:
                for record in remaining_records:
                    file.write(record + "\n")

            print("Expense deleted successfully.")

    else:
            print("Expense not found.")




#Functional Requirements: 6. Expense Summary
def expense_summary():
        records = read_expenses()


        if not records:
             print("No expense available for summary")
             return
        
        amounts = []

        for record in records:
             parts = record.split(",", 4)

             if len(parts) == 5:
                  try:
                       amounts.append(float(parts[4]))
                  except ValueError:
                       print("Warning: An invalid amount was skipped.")

        if not amounts:
             print("No valid expense amounts found.")
             return


        total_expenses = len(amounts)
        total_spending = sum(amounts)
        average = total_spending / total_expenses
        highest = max(amounts)
        lowest = min(amounts)

        print("\n========== Expense Summary ==========")
        print(f"Total number of expenses: {total_expenses}")
        print(f"Total spending: {total_spending:g}", "BDT")
        print(f"Average expense: {average:.2f}", "BDT")
        print(f"Highest expense: {highest:g}", "BDT")
        print(f"Lowest expense: {lowest:g}", "BDT")



#Functional Requirements: Main Menu
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
            print("Invalid choice! Please select a number from 1 to 7.")

main()