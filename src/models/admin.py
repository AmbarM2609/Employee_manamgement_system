from src.utils.db import db
import bcrypt

class Admin(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


    # 3. Method to set and hash the password
    def set_password(self, plaintext_password):
        """Hashes the password and sets the hash to the 'password' field."""
        hashed_bytes = bcrypt.hashpw(
            plaintext_password.encode('utf-8'), 
            bcrypt.gensalt()
        )
        self.password = hashed_bytes.decode('utf-8')

    # 4. Method to check the password during login
    def check_password(self, plaintext_password):
        """Checks the stored hash against the plaintext password entered by the user."""
        if self.password and self.password.startswith('$2b$'):
            return bcrypt.checkpw(
                plaintext_password.encode('utf-8'), 
                self.password.encode('utf-8')
            )
        return False