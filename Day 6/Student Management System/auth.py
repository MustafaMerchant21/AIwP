"""
Very simple Role-Based Access Control (RBAC).
Users are stored as: username -> {"password": ..., "role": ...}

Roles, from most to least powerful:
    admin   -> full access (can do everything, including delete HOD in theory)
    hod     -> can manage faculty and students, cannot delete HOD records
    faculty -> can manage students only, and view-only for faculty/HOD
"""

# users in-built creds
users = {
    "admin":   {"password": "admin123",   "role": "admin"},
    "hod1":    {"password": "hod123",     "role": "hod"},
    "fac1":    {"password": "fac123",     "role": "faculty"},
}

# what each role is allowed to do. menu will check against this.
PERMISSIONS = {
    "admin":   {"student": ["c", "r", "u", "d"], "faculty": ["c", "r", "u", "d"], "hod": ["c", "r", "u"]},
    "hod":     {"student": ["c", "r", "u", "d"], "faculty": ["c", "r", "u", "d"], "hod": ["r"]},
    "faculty": {"student": ["c", "r", "u"],      "faculty": ["r"],               "hod": ["r"]},
}


def login(username, password):
    """Returns role string if credentials match, else None."""
    user = users.get(username)
    if user and user["password"] == password:
        return user["role"]
    return None


def has_permission(role, entity, action):
    """entity: 'student' | 'faculty' | 'hod' ; action: 'c' | 'r' | 'u' | 'd'"""
    return action in PERMISSIONS.get(role, {}).get(entity, []) 