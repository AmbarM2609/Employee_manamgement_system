from src.utils.db import db
from datetime import date

class Employee(db.Model):
    
    
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    department = db.Column(db.String(50))
    designation = db.Column(db.String(50))
    date_of_joining = db.Column(db.Date)
    status = db.Column(db.String(10), default="Active")
    

    def __init__(self, name, email, phone, department, designation, date_of_joining=None, status="Active"):
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.designation = designation
        self.date_of_joining = date_of_joining if date_of_joining else date.today() # Improved default
        self.status = status
