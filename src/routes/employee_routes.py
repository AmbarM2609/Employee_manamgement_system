from flask import Blueprint
from src.controllers import employee_controller as ctrl

employee_bp = Blueprint("employee", __name__, url_prefix="/employees")

employee_bp.route("/", methods=["GET"])(ctrl.list_employees)
employee_bp.route("/add", methods=["GET", "POST"])(ctrl.create_employee)
employee_bp.route("/<int:employee_id>", methods=["GET"])(ctrl.view_employee)
employee_bp.route("/<int:employee_id>/edit", methods=["GET", "POST"])(ctrl.edit_employee)
employee_bp.route("/<int:employee_id>/delete", methods=["POST"])(ctrl.delete_employee)
