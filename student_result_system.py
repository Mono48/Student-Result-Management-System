def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    else:
        return "F"


def add_student(students):
    name = input("Enter student name: ")
    matric = input("Enter matric number: ")
    score = int(input("Enter score: "))

    grade = calculate_grade(score)

    student = {
        "name": name,
        "matric": matric,
        "score": score,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully.\n")


def display_students(students):
    if not students:
        print("No student records found.\n")
        return

    for student in students:
        print("Name:", student["name"])
        print("Matric:", student["matric"])
        print("Score:", student["score"])
        print("Grade:", student["grade"])
        print("------------------------")


def main_menu():
    students = []

    while True:
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


main_menu()
