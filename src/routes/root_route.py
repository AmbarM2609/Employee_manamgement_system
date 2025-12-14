from flask import Blueprint, redirect, url_for

root_bp = Blueprint("root", __name__)

@root_bp.route("/")
def index():
    # Redirect to the main employee list page
    return redirect(url_for("employee.list_employees"))