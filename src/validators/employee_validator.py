def validate_employee(data):
    errors = []

    if not data.get("name") or len(data["name"]) < 2:
        errors.append("Name must be at least 2 characters")

    if "@" not in data.get("email", ""):
        errors.append("Invalid email")

    if not data.get("department"):
        errors.append("Department is required")

    if not data.get("designation"):
        errors.append("Designation is required")

    return errors
