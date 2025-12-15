from flask import Blueprint
from src.controllers.auth_controller import login, logout

auth_bp = Blueprint("auth", __name__)

auth_bp.route("/login", methods=["GET", "POST"])(login)

auth_bp.route("/logout")(logout)

