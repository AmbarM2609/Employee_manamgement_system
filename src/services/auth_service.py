from src.models.admin import Admin

class AuthService:

    # def authenticate(self, username, password):
    #     admin = Admin.query.filter_by(username=username).first()
    #     if not admin or admin.password != password:
    #         return None
    #     return admin
    def authenticate(self, username, password):
        admin = Admin.query.filter_by(username=username).first()
        
        # CRITICAL FIX: Use the check_password method for secure verification!
        if not admin or not admin.check_password(password):
            return None
        return admin