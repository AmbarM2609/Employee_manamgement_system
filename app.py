from flask import Flask
import os
from dotenv import load_dotenv # Used for local testing
from src.utils.db import init_db
from src.routes.root_route import root_bp
from src.routes.employee_routes import employee_bp
from src.routes.auth_routes import auth_bp
from src.utils.logger import setup_logger
from src.utils.db import db
from src.models.admin import Admin

# --- CRITICAL: Load environment variables locally (.env file) ---
# This line allows your app to read local secrets during development
load_dotenv() 


def create_initial_admin(app):
    """
    Checks if the 'admins' table is empty and creates an initial admin user 
    using a plaintext password read from a secret environment variable.
    """
    with app.app_context():
        
        # 1. READ PLAINTEXT PASSWORD FROM RENDER SECRET (INITIAL_ADMIN_PLAINTEXT_PASSWORD)
        initial_password = os.environ.get('INITIAL_ADMIN_PLAINTEXT_PASSWORD')
        
        # Check if the table is empty AND the plaintext variable exists
        if initial_password and not Admin.query.first():
            
            # 2. CREATE ADMIN AND LET THE MODEL HASH IT
            print("--- Running Initial Admin Creation ---")
            
            admin = Admin(username="admin") 
            
            # IMPORTANT: This method MUST be defined in your src/models/admin.py
            # It hashes the plaintext password before saving it to the database.
            admin.set_password(initial_password) 
            
            db.session.add(admin)
            db.session.commit()
            print("--- Initial admin created securely: username='admin' ---")
            print("--- IMPORTANT: Delete the INITIAL_ADMIN_PLAINTEXT_PASSWORD variable from Render NOW! ---")


def create_app():
    """Application Factory Function"""
    app = Flask(__name__, template_folder='src/templates', static_folder='src/static')
    
    # Load configuration from config.py
    app.config.from_object("config.Config")

    setup_logger()
    init_db(app) # Initializes Flask-SQLAlchemy

    # Register Blueprints
    app.register_blueprint(root_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(auth_bp)

    # --- Database Setup & Initial User Creation ---
    with app.app_context():
        # 1. Create all database tables (safe to call multiple times)
        db.create_all()  
    
    # 2. Run the one-time setup function after tables are guaranteed to exist
    create_initial_admin(app) 

    return app


# This line calls the factory and is the entry point for Gunicorn
app = create_app() 

if __name__ == "__main__":
    # This block is for local development only (ignored by Render)
    # The 'app' object is already created above, configured, and ready to run
    app.run(debug=True)