from flask import request, render_template, redirect, url_for, session
from src.services.auth_service import AuthService

auth_service = AuthService()

def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        admin = auth_service.authenticate(username, password)
        if not admin:
            return render_template("auth/login.html", error="Invalid credentials")
        session["admin_id"] = admin.id
        return redirect(url_for("employee.list_employees"))
    return render_template("auth/login.html")

def logout():
    session.clear()
    return redirect(url_for("auth.login"))
