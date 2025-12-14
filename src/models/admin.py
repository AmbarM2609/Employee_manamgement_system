from src.utils.db import db
import bcrypt

class Admin(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    # Increase size to 128 to safely store any hash output
    password = db.Column(db.String(128), nullable=False) 

    def set_password(self, plaintext_password):
        """Hashes the password and sets the hash to the 'password' field."""
        hashed_bytes = bcrypt.hashpw(
            plaintext_password.encode('utf-8'), 
            bcrypt.gensalt()
        )
        self.password = hashed_bytes.decode('utf-8')

    def check_password(self, plaintext_password):
        """Checks the stored hash against the plaintext password entered by the user."""
        # Check if the stored password is a valid hash before comparing
        if self.password.startswith('$2b$'):
            return bcrypt.checkpw(
                plaintext_password.encode('utf-8'), 
                self.password.encode('utf-8')
            )
        return False # Password comparison failed