"""
Simple in-memory 'database' using dictionaries.
Each dict maps: id -> object
Not persistence
"""

from Student import Student
from Faculty import Faculty
from Hod import HOD

# ---- storage ----
students = {}
faculties = {}
hods = {}

# ---- auto-increment counters ----
# Each counter holds the NEXT id number to hand out for that entity.
# On create   -> use counter, then increment.
# On delete   -> if the deleted id was the last one given out, step the
#                counter back down (simple decrement, no gap-filling).
_counters = {"student": 0, "faculty": 0, "hod": 0}
_PREFIX = {"student": "S", "faculty": "F", "hod": "H"}


def _next_id(entity):
    """Generates the next id, e.g. S1, F3, H2, and advances the counter."""
    _counters[entity] += 1
    return f"{_PREFIX[entity]}{_counters[entity]}"

def _release_id(entity, used_id):
    """If used_id was the most recently issued id, decrement the counter
    so the next create() reuses that same number instead of skipping it."""
    prefix = _PREFIX[entity]
    current = f"{prefix}{_counters[entity]}"
    if used_id == current:
        _counters[entity] -= 1


# ============ STUDENT CRUD ============

def create_student(name, age, email, addr, branch, class_name):
    id = _next_id("student")
    s = Student(name, id, age, email, addr, branch, class_name)
    students[id] = s
    return s, f"Student {name} created with ID {id}."

def read_student(student_id):
    return students.get(student_id)

def read_all_students():
    return list(students.values())

def update_student(student_id, **fields):
    s = students.get(student_id)
    if not s:
        return False, "Student not found."
    for key, value in fields.items():
        if hasattr(s, key) and value is not None:
            setattr(s, key, value)
    return True, "Student updated."

def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        _release_id("student", student_id)
        return True, "Student deleted."
    return False, "Student not found."


# ============ FACULTY CRUD ============

def create_faculty(name, email, title, courses, department):
    faculty_id = _next_id("faculty")
    f = Faculty(name, faculty_id, email, title, courses, department)
    faculties[faculty_id] = f
    return f, f"Faculty {name} created with ID {faculty_id}."

def read_faculty(faculty_id):
    return faculties.get(faculty_id)

def read_all_faculties():
    return list(faculties.values())

def update_faculty(faculty_id, **fields):
    f = faculties.get(faculty_id)
    if not f:
        return False, "Faculty not found."
    for key, value in fields.items():
        if hasattr(f, key) and value is not None:
            setattr(f, key, value)
    return True, "Faculty updated."

def delete_faculty(faculty_id):
    if faculty_id in faculties:
        del faculties[faculty_id]
        _release_id("faculty", faculty_id)
        return True, "Faculty deleted."
    return False, "Faculty not found."


# ============ HOD - CREATE, READ, UPDATE only (no delete) ============

def create_hod(name, email, title, courses, department, office_room, budget):
    hod_id = _next_id("hod")
    h = HOD(name, hod_id, email, title, courses, department, office_room, budget)
    hods[hod_id] = h
    return h, f"HOD {name} created with ID {hod_id}."

def read_hod(hod_id):
    return hods.get(hod_id)

def read_all_hods():
    return list(hods.values())

def update_hod(hod_id, **fields):
    h = hods.get(hod_id)
    if not h:
        return False, "HOD not found."
    for key, value in fields.items():
        if hasattr(h, key) and value is not None:
            setattr(h, key, value)
    return True, "HOD updated."