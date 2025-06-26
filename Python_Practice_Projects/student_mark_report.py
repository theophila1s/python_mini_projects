import math
from datetime import datetime

# List to store student records (each as a dictionary)
students = []

# Lambda to calculate grade
calculate_grade = lambda avg: (
    "A+" if avg >= 90 else
    "A" if avg >= 80 else
    "B+" if avg >= 70 else
    "B" if avg >= 60 else
    "C" if avg >= 50 else
    "Fail"
)

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    subjects = ("Math", "Science", "English", "Social", "Computer")
    
    marks = {}
    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks[subject] = mark

    total = sum(marks.values())
    average = total / len(subjects)
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks,
        "total": math.ceil(total),
        "average": round(average, 2),
        "grade": grade,
        "created_at": datetime.now()
    }

    students.append(student)
    print(f"\n✅ Report card added for {name}!\n")

def view_report_card():
    if not students:
        print("\n❗No records found.\n")
        return

    for student in students:
        print("\n📄----- Report Card -----")
        print(f"Name      : {student['name']}")
        print(f"Roll No   : {student['roll_no']}")
        print(f"Date      : {student['created_at'].strftime('%d-%m-%Y %H:%M:%S')}")
        print("\nMarks:")
        for subject, mark in student['marks'].items():
            print(f"- {subject}: {mark}")
        print(f"\nTotal     : {student['total']}")
        print(f"Average   : {student['average']}")
        print(f"Grade     : {student['grade']}")
        print("--------------------------\n")

def menu():
    while True:
        print("=== Student Report Card System ===")
        print("1. Add Student")
        print("2. View Report Cards")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_report_card()
        elif choice == "3":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")

# Run the system
menu()
