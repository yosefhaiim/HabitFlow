from flask import Blueprint

entries_bp = Blueprint("entries", __name__, url_prefix="/entries")

@entries_bp.route("/health")
def entries_health():
    return {"module": "entries", "status": "ok"}
