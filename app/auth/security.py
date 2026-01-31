import bcrypt

def hash_password(password: str) -> str:
    """Hash a plain text password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a password against its hashed version."""
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
