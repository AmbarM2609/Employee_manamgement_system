from flask import Flask
from src.utils.db import init_db
from src.routes.root_route import root_bp
from src.routes.employee_routes import employee_bp
from src.routes.auth_routes import auth_bp
from src.utils.logger import setup_logger
from src.utils.db import db
from src.models.admin import Admin

def create_app():
    app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
    app.config.from_object("config.Config")

    setup_logger()
    init_db(app)
    
    app.register_blueprint(root_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()  # Creates tables if not exist

    return app

def create_initial_admin(app):
    with app.app_context():
        if not Admin.query.first():
            # For this example, we'll keep it simple:
            admin = Admin(username="admin", password="admin123")
            db.session.add(admin)
            db.session.commit()
            print("--- Initial admin created: username='admin', password='admin123' ---")

if __name__ == "__main__":
    
    app = create_app()
    create_initial_admin(app) # <--- Call the function here
    app.run(debug=True)
