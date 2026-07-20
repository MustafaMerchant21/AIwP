class Faculty:
    def __init__(self, name, faculty_id, email, title, courses, department):
        self.name = name
        self.faculty_id = faculty_id
        self.email = email
        self.title = title
        self.courses = courses
        self.department = department

    def print_data(self):
        print(f"======= Faculty {self.name} =======")
        print(f"ID: {self.faculty_id}")
        print(f"Email: {self.email}")
        print(f"Title: {self.title}")
        print(f"Courses: {', '.join(self.courses)}")
        print(f"Department: {self.department}")