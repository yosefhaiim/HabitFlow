from flask import Blueprint

insights_bp = Blueprint("insights", __name__, url_prefix="/insights")

@insights_bp.route("/health")
def insights_health():
    return {"module": "insights", "status": "ok"}
