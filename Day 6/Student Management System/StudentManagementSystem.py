"""
Menu-driven 144p ERP System.
Login first (RBAC), then get a menu based on your role.
"""
import os
import re
import auth
import database as db

# ============ REGEX PATTERNS ============
REGEX_NAME = r"^[A-Za-z\s'-]{2,50}$" # \s matches any whitespace character
REGEX_AGE = r"^(?:[1-9][0-9]?|120)$" # [1-9][0-9]? matches 1-9 or 10-99, |120 matches exactly 120
REGEX_EMAIL = r"^[\w\.-]+@[\w\.-]+\.\w+$" # \w matches word characters, \. matches literal dot
REGEX_BUDGET = r"^\d+(\.\d{1,2})?$" # matches integers or decimals with up to 2 decimal places


# ============ LOGIN ============

def login_screen():
    print("\n===== LOGIN =====")
    for attempt in range(3):
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        role = auth.login(username, password)
        if role:
            print(f"\nWelcome, {username}! Role: {role}")
            return username, role
        print(f"Invalid credentials. Attempts left: {2 - attempt}")
    print("Too many failed attempts. Exiting.")
    return None, None


# ============ HELPERS ============

def ask(prompt):
    return input(prompt).strip()

def ask_valid(prompt, pattern, optional=False):
    """Prompts until regex matches. If optional=True, pressing enter returns None."""
    while True:
        val = input(prompt).strip()
        if not val:
            if optional:
                return None
            print("Field cannot be empty.")
            continue
        if re.match(pattern, val):
            return val
        print("Invalid format. Please try again.")

def ask_list(prompt):
    raw = input(prompt + " (comma separated): ").strip()
    return [x.strip() for x in raw.split(",") if x.strip()]

def denied():
    print(">> Permission denied for your role.")


# ============ STUDENT MENU ============

def student_menu(role):
    while True:
        print("\n--- Student Menu ---")
        print("1. Create Student")
        print("2. View Student")
        print("3. View All Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("0. Back")
        choice = ask("Choose: ")

        if choice == "1":
            if not auth.has_permission(role, "student", "c"):
                denied(); continue
            name = ask_valid("Name: ", REGEX_NAME)
            age = ask_valid("Age: ", REGEX_AGE)
            email = ask_valid("Email: ", REGEX_EMAIL)
            addr = ask("Address: ")
            branch = ask("Branch: ")
            class_name = ask("Class: ")
            obj, msg = db.create_student(name, age, email, addr, branch, class_name)
            print(msg)

        elif choice == "2":
            if not auth.has_permission(role, "student", "r"):
                denied(); continue
            sid = ask("Student ID: ")
            s = db.read_student(sid)
            s.print_data() if s else print("Not found.")

        elif choice == "3":
            if not auth.has_permission(role, "student", "r"):
                denied(); continue
            all_students = db.read_all_students()
            if not all_students:
                print("No students found.")
            for s in all_students:
                s.print_data()

        elif choice == "4":
            if not auth.has_permission(role, "student", "u"):
                denied(); continue
            sid = ask("Student ID to update: ")
            if not db.read_student(sid):
                print("Not found."); continue
            print("Leave blank to keep existing value.")
            fields = {
                "name": ask_valid("New name: ", REGEX_NAME, optional=True),
                "age": ask_valid("New age: ", REGEX_AGE, optional=True),
                "email": ask_valid("New email: ", REGEX_EMAIL, optional=True),
                "addr": ask("New address: ") or None,
                "branch": ask("New branch: ") or None,
                "class_name": ask("New class: ") or None,
            }
            ok, msg = db.update_student(sid, **fields)
            print(msg)

        elif choice == "5":
            if not auth.has_permission(role, "student", "d"):
                denied(); continue
            sid = ask("Student ID to delete: ")
            ok, msg = db.delete_student(sid)
            print(msg)

        elif choice == "0":
            break
        else:
            print("Invalid choice.")


# ============ FACULTY MENU ============

def faculty_menu(role):
    while True:
        print("\n--- Faculty Menu ---")
        print("1. Create Faculty")
        print("2. View Faculty")
        print("3. View All Faculty")
        print("4. Update Faculty")
        print("5. Delete Faculty")
        print("0. Back")
        choice = ask("Choose: ")

        if choice == "1":
            if not auth.has_permission(role, "faculty", "c"):
                denied(); continue
            name = ask_valid("Name: ", REGEX_NAME)
            email = ask_valid("Email: ", REGEX_EMAIL)
            title = ask("Title: ")
            courses = ask_list("Courses")
            department = ask("Department: ")
            obj, msg = db.create_faculty(name, email, title, courses, department)
            print(msg)

        elif choice == "2":
            if not auth.has_permission(role, "faculty", "r"):
                denied(); continue
            fid = ask("Faculty ID: ")
            f = db.read_faculty(fid)
            f.print_data() if f else print("Not found.")

        elif choice == "3":
            if not auth.has_permission(role, "faculty", "r"):
                denied(); continue
            all_faculty = db.read_all_faculties()
            if not all_faculty:
                print("No faculty found.")
            for f in all_faculty:
                f.print_data()

        elif choice == "4":
            if not auth.has_permission(role, "faculty", "u"):
                denied(); continue
            fid = ask("Faculty ID to update: ")
            if not db.read_faculty(fid):
                print("Not found."); continue
            print("Leave blank to keep existing value.")
            name = ask_valid("New name: ", REGEX_NAME, optional=True)
            email = ask_valid("New email: ", REGEX_EMAIL, optional=True)
            title = ask("New title: ") or None
            department = ask("New department: ") or None
            courses_raw = ask("New courses (comma separated, blank to keep): ")
            courses = [c.strip() for c in courses_raw.split(",") if c.strip()] or None
            ok, msg = db.update_faculty(fid, name=name, email=email, title=title,
                                         department=department, courses=courses)
            print(msg)

        elif choice == "5":
            if not auth.has_permission(role, "faculty", "d"):
                denied(); continue
            fid = ask("Faculty ID to delete: ")
            ok, msg = db.delete_faculty(fid)
            print(msg)

        elif choice == "0":
            break
        else:
            print("Invalid choice.")


# ============ HOD MENU (Create, Read, Update only — no Delete) ============

def hod_menu(role):
    while True:
        print("\n--- HOD Menu ---")
        print("1. Create HOD")
        print("2. View HOD")
        print("3. View All HODs")
        print("4. Update HOD")
        print("0. Back")
        choice = ask("Choose: ")

        if choice == "1":
            if not auth.has_permission(role, "hod", "c"):
                denied(); continue
            name = ask_valid("Name: ", REGEX_NAME)
            email = ask_valid("Email: ", REGEX_EMAIL)
            title = ask("Title: ")
            courses = ask_list("Courses")
            department = ask("Department: ")
            office_room = ask("Office Room: ")
            budget = ask_valid("Budget: ", REGEX_BUDGET)
            obj, msg = db.create_hod(name, email, title, courses, department, office_room, budget)
            print(msg)

        elif choice == "2":
            if not auth.has_permission(role, "hod", "r"):
                denied(); continue
            hid = ask("HOD ID: ")
            h = db.read_hod(hid)
            h.print_data() if h else print("Not found.")

        elif choice == "3":
            if not auth.has_permission(role, "hod", "r"):
                denied(); continue
            all_hods = db.read_all_hods()
            if not all_hods:
                print("No HODs found.")
            for h in all_hods:
                h.print_data()

        elif choice == "4":
            if not auth.has_permission(role, "hod", "u"):
                denied(); continue
            hid = ask("HOD ID to update: ")
            if not db.read_hod(hid):
                print("Not found."); continue
            print("Leave blank to keep existing value.")
            name = ask_valid("New name: ", REGEX_NAME, optional=True)
            email = ask_valid("New email: ", REGEX_EMAIL, optional=True)
            office_room = ask("New office room: ") or None
            budget = ask_valid("New budget: ", REGEX_BUDGET, optional=True)
            ok, msg = db.update_hod(hid, name=name, email=email,
                                     office_room=office_room, budget=budget)
            print(msg)

        elif choice == "0":
            break
        else:
            print("Invalid choice.")


# ============ MAIN MENU ============

def main_menu(username, role):
    while True:
        print(f"\n===== MAIN MENU (User: {username} | Role: {role}) =====")
        print("1. Student Management")
        print("2. Faculty Management")
        print("3. HOD Management")
        print("0. Logout")
        choice = ask("Choose: ")

        if choice == "1":
            student_menu(role)
        elif choice == "2":
            faculty_menu(role)
        elif choice == "3":
            hod_menu(role)
        elif choice == "0":
            print("Logged out.")
            break
        else:
            print("Invalid choice.")


def main():
    print("===== ERP SYSTEM =====")
    username, role = login_screen()
    if role:
        main_menu(username, role)


if __name__ == "__main__":
    main()