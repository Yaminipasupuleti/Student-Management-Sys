students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        students[roll_no] = name
        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for roll, name in students.items():
                print(f"Roll No: {roll}, Name: {name}")

    elif choice == "3":
        roll_no = input("Enter Roll Number to Search: ")
        if roll_no in students:
            print("Student Found:", students[roll_no])
        else:
            print("Student Not Found.")

    elif choice == "4":
        roll_no = input("Enter Roll Number to Delete: ")
        if roll_no in students:
            del students[roll_no]
            print("Student Deleted Successfully!")
        else:
            print("Student Not Found.")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")