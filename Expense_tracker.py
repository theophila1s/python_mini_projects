import math
from datetime import datetime

expenses = []

def add_expense():
    date_str = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter amount: "))
    category = input("Enter category (e.g., food, travel, bills): ")
    note = input("Enter note (optional): ")

    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    expense = {
        "date": date_obj,
        "amount": amount,
        "category": category.lower(),
        "note": note
    }
    expenses.append(expense)
    print("Expense added successfully!\n")

def monthly_summary(month, year):
    total = 0
    for exp in expenses:
        if exp["date"].month == month and exp["date"].year == year:
            total += exp["amount"]
    print(f"\nTotal expenses for {month}/{year}: ₹{math.ceil(total)}\n")

def yearly_summary(year):
    total = 0
    for exp in expenses:
        if exp["date"].year == year:
            total += exp["amount"]
    print(f"\nTotal expenses for {year}: ₹{math.ceil(total)}\n")

def category_summary():
    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    print("\nExpenses by category:")
    for cat, total in category_totals.items():
        print(f"- {cat.title()}: ₹{math.ceil(total)}")
    print()

def show_menu():
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Yearly Summary")
        print("4. View Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            month = int(input("Enter month (1-12): "))
            year = int(input("Enter year: "))
            monthly_summary(month, year)
        elif choice == "3":
            year = int(input("Enter year: "))
            yearly_summary(year)
        elif choice == "4":
            category_summary()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the tracker
show_menu()
