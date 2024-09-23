expenses = []

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    expenses.append((category, amount))
    print("Expense added!\n")

def view_expenses():
    if not expenses:
        print("No expenses yet!\n")
        return
    total = sum(amount for _, amount in expenses)
    for idx, (category, amount) in enumerate(expenses, 1):
        print(f"{idx}. {category}: ${amount:.2f}")
    print(f"Total: ${total:.2f}\n")

def save_expenses(filename="expenses.txt"):
    with open(filename, "w") as file:
        for category, amount in expenses:
            file.write(f"{category}: ${amount:.2f}\n")
    print("Expenses saved!\n")

def menu():
    while True:
        choice = input("1. Add Expense\n2. View Expenses\n3. Save\n4. Quit\nChoose: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            save_expenses()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, try again.\n")

if __name__ == "__main__":
    menu()
