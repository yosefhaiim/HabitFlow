from datetime import datetime

def build_user(email, password_hash):
    return {
        "email": email,
        "password": password_hash,
        "created_at": datetime.utcnow()
    }
