from src.models.employee import Employee
from src.utils.db import db

class EmployeeRepository:
    def save(self, employee):
        db.session.add(employee)
        db.session.commit()
        return employee

    def find_all(self):
        return Employee.query.all()

    def find_by_id(self, employee_id):
        return Employee.query.get(employee_id)

    def update(self):
        db.session.commit()

    def delete(self, employee):
        db.session.delete(employee)
        db.session.commit()
