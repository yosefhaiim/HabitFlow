from flask import Blueprint, request

from app.auth.repository import get_user_by_email, create_user
from app.auth.models import build_user
from app.auth.security import hash_password
from app.auth.security import verify_password
from app.auth.jwt_utils import create_access_token
from app.utils.responses import error_response, success_response




auth_bp = Blueprint("auth", __name__, url_prefix="/auth")



@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return error_response("Email and password are required", 400)

    if get_user_by_email(email):
        return error_response("User already exists", 409)

    password_hash = hash_password(password)
    user = build_user(email, password_hash)

    create_user(user)

    return success_response("User created successfully", 201)


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return error_response("Email and password are required", 400)

    user = get_user_by_email(email)
    if not user or not verify_password(password, user["password"]):
        return error_response("Invalid credentials", 401)

    token = create_access_token(str(user["_id"]))
    return success_response(f"access_token: {token}",200)
