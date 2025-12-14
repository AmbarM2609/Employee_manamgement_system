from src.models.admin import Admin

class AuthService:

    def authenticate(self, username, password):
        admin = Admin.query.filter_by(username=username).first()
        if not admin or admin.password != password:
            return None
        return admin
