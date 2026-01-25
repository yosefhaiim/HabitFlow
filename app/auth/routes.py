from flask import Blueprint

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/health")
def auth_health():
    return {"module": "auth", "status": "ok"}
