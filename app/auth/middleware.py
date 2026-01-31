import jwt
from functools import wraps
from flask import request, current_app



def jwt_required(func):
    """Protect routes by requiring a valid JWT access token."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return {"error": "Authorization token required"}, 401

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}, 401
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}, 401

        request.user_id = payload["sub"]
        return func(*args, **kwargs)

    return wrapper
