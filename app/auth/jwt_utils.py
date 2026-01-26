import jwt
from datetime import datetime, timedelta
from flask import current_app

def create_access_token(user_id: str):
    payload = {
        "sub": user_id,
        "exp": datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
