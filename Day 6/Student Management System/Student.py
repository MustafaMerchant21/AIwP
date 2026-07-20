class Student:
    def __init__(self, name, id, age, email, addr, branch, class_name):
        self.name = name
        self.student_id = id
        self.age = age
        self.email = email
        self.addr = addr
        self.branch = branch
        self.class_name = class_name

    def print_data(self):
        print("======= Student ======")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Address: {self.addr}")
        print(f"Branch: {self.branch}")
        print(f"Class: {self.class_name}")