class HOD:
    def __init__(self, name, hod_id, email, title, courses, department, office_room, budget):
        self.name = name
        self.hod_id = hod_id
        self.email = email
        self.title = title
        self.courses = courses
        self.department = department
        self.office_room = office_room
        self.budget = budget
        self.managed_faculty = []

    def print_data(self):
        print(f"======= HOD {self.name} =======")
        print(f"HOD ID: {self.hod_id}")
        print(f"Email: {self.email}")
        print(f"Title: {self.title}")
        print(f"Teaching Courses: {', '.join(self.courses)}")
        print(f"Department Managed: {self.department}")
        print(f"Office Room: {self.office_room}")

    def add_faculty_member(self, faculty_object):
        """Adds a faculty member object to the department's managed list."""
        self.managed_faculty.append(faculty_object)
        return f"Added {faculty_object.name} to {self.department} department."

    def approve_leave(self, employee_name, days):
        """Approves leave requests for departmental staff."""
        return f"HOD {self.name} approved {days} days of leave for {employee_name}."