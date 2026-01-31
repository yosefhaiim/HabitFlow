from datetime import datetime

def build_user(email, password_hash):
    """Create a user data structure for database insertion."""
    return {
        "email": email,
        "password": password_hash,
        "created_at": datetime.utcnow()
    }
