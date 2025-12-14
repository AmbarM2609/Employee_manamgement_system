from flask import request, render_template, redirect, url_for
from src.services.employee_service import EmployeeService
from src.validators.employee_validator import validate_employee
from src.utils.auth import login_required

service = EmployeeService()

@login_required
def list_employees():
    employees = service.fetch_employees()
    return render_template("employees/list.html", employees=employees)

@login_required
def create_employee():
    if request.method == "POST":
        data = request.form.to_dict()
        errors = validate_employee(data)
        if errors:
            return render_template("employees/form.html", errors=errors)
        service.add_employee(data)
        return redirect(url_for("employee.list_employees"))
    return render_template("employees/form.html")

@login_required
def view_employee(employee_id):
    employee = service.fetch_employee(employee_id)
    return render_template("employees/view.html", employee=employee)

@login_required
def edit_employee(employee_id):
    employee = service.fetch_employee(employee_id)
    if request.method == "POST":
        data = request.form.to_dict()
        service.modify_employee(employee_id, data)
        return redirect(url_for("employee.list_employees"))
    return render_template("employees/form.html", employee=employee)

@login_required
def delete_employee(employee_id):
    service.remove_employee(employee_id)
    return redirect(url_for("employee.list_employees"))
