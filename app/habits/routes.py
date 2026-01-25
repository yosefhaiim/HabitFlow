from flask import Blueprint

habits_bp = Blueprint("habits", __name__, url_prefix="/habits")

@habits_bp.route("/health")
def habits_health():
    return {"module": "habits", "status": "ok"}
