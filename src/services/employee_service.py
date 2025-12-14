from src.repositories.employee_repository import EmployeeRepository # type: ignore
from src.models.employee import Employee

class EmployeeService:

    def __init__(self):
        self.repo = EmployeeRepository()

    def add_employee(self, data):
        
        if not data.get("date_of_joining"):
            data.pop("date_of_joining", None)
        
        employee = Employee(**data)
        return self.repo.save(employee)

    def fetch_employees(self):
        return self.repo.find_all()

    def fetch_employee(self, employee_id):
        employee = self.repo.find_by_id(employee_id)
        if not employee:
            raise ValueError("Employee not found")
        return employee

    def modify_employee(self, employee_id, data):
        employee = self.fetch_employee(employee_id)
        for key, value in data.items():
            setattr(employee, key, value)
        self.repo.update()
        return employee

    def remove_employee(self, employee_id):
        employee = self.fetch_employee(employee_id)
        self.repo.delete(employee)
