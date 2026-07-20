class Student:
    def __init__(self, name, age, email, addr, branch, class_name):
        self.name = name 
        self.age = age 
        self.email = email 
        self.addr = addr 
        self.branch = branch 
        self.class_name = class_name

    def print_data(self):
        print("======= Student ======")
        print(self.name)
        print(self.age)
        print(self.email)
        print(self.addr)
        print(self.branch)
        print(self.class_name)

class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # Create
    def create(self):
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        email = input("Enter Email: ")
        addr = input("Enter Address: ")
        branch = input("Enter Branch: ")
        class_name = input("Enter Class: ")

        student = Student(name, age, email, addr, branch, class_name)
        self.students.append(student)

        print("Student added successfully!")

    # Read
    def read(self):
        if len(self.students) == 0:
            print("No student records found.")
            return

        for student in self.students:
            student.print_data()
            print()

    # Update
    def update(self):
        email = input("Enter the student's email to update: ")

        for student in self.students:
            if student.email == email:
                student.name = input("New Name: ")
                student.age = input("New Age: ")
                student.addr = input("New Address: ")
                student.branch = input("New Branch: ")
                student.class_name = input("New Class: ")

                print("Student updated successfully!")
                return

        print("Student not found.")

    # Delete
    def delete(self):
        email = input("Enter the student's email to delete: ")

        for student in self.students:
            if student.email == email:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found.")


# Main Program
sms = StudentManagementSystem()

while True:
    print("\n===== Student Management System =====")
    print("1. Create Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sms.create()
    elif choice == "2":
        sms.read()
    elif choice == "3":
        sms.update()
    elif choice == "4":
        sms.delete()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
