import math

# Lambda to calculate per person share (equal split)
equal_split = lambda total, count: round(total / count, 2)

# Function to input names
def get_people():
    n = int(input("Enter number of people: "))
    people = []
    for _ in range(n):
        name = input("Enter person’s name: ")
        people.append(name)
    return people

# Function to perform equal split
def split_bill_equally():
    total = float(input("\nEnter total bill amount: ₹"))
    people = get_people()
    per_head = equal_split(total, len(people))

    print(f"\n💰 Each person should pay: ₹{per_head}\n")
    for name in people:
        print(f"- {name}: ₹{per_head}")

# Function to perform custom split
def split_bill_custom():
    total = float(input("\nEnter total bill amount: ₹"))
    people = get_people()
    amounts = []
    
    print("Enter custom amount for each person:")
    for name in people:
        amt = float(input(f"{name}'s share: ₹"))
        amounts.append(amt)

    if math.isclose(sum(amounts), total, abs_tol=0.01):
        print("\n✅ Bill split successfully!\n")
        for name, amt in zip(people, amounts):
            print(f"- {name} should pay: ₹{amt}")
    else:
        print("\n❌ Error: The sum of entered amounts does not match the total bill.")

# Function to display menu
def menu():
    while True:
        print("\n--- Bill Splitter Menu ---")
        print("1. Equal Split")
        print("2. Custom Split")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            split_bill_equally()
        elif choice == "2":
            split_bill_custom()
        elif choice == "3":
            print("👋 Exiting Bill Splitter. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run the app
menu()
