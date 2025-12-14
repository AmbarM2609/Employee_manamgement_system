from flask import Flask
import os
from src.utils.db import init_db
from src.routes.root_route import root_bp
from src.routes.employee_routes import employee_bp
from src.routes.auth_routes import auth_bp
from src.utils.logger import setup_logger
from src.utils.db import db
from src.models.admin import Admin
from dotenv import load_dotenv # Assuming you use this for local secrets

# Load environment variables for local testing (Render ignores this but it's good practice)
load_dotenv() 


def create_initial_admin(app):
    with app.app_context():
        # 1. READ HASHED PASSWORD FROM RENDER SECRET
        initial_hash = os.environ.get('INITIAL_ADMIN_PASSWORD_HASH')
        
        # Check if the table is empty AND the hash variable exists
        if initial_hash and not Admin.query.first():
            
            # 2. CREATE ADMIN USING THE HASHED SECRET
            print("--- Running Initial Admin Creation ---")
            
            admin = Admin(
                username="admin", 
                password_hash=initial_hash # Assuming this is the field name
            )
            
            db.session.add(admin)
            db.session.commit()
            print("--- Initial admin created securely. Delete the hash from Render NOW. ---")


def create_app():
    app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
    app.config.from_object("config.Config")

    setup_logger()
    init_db(app)
    
    app.register_blueprint(root_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(auth_bp)

    # 3. RUN SETUP LOGIC INSIDE THE FACTORY
    with app.app_context():
        db.create_all()  # Creates tables if not exist
    
    # Run the setup function after db.create_all()
    create_initial_admin(app) 

    return app


# This line is for Gunicorn (if using gunicorn app:app) 
# and for local Flask CLI commands like 'flask run' and 'flask shell'
app = create_app() 

if __name__ == "__main__":
    # Remove the extra call to create_initial_admin(app) as it's already run above
    # The 'app' object here already contains the configured, ready-to-run app.
    app.run(debug=True)