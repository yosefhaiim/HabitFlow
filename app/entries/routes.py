from flask import Blueprint
from flask import request

from app.auth.middleware import jwt_required
from app.entries.models import build_entry
from app.entries.repository import create_entry



entries_bp = Blueprint("entries", __name__, url_prefix="/entries")

@entries_bp.route("/health")
def entries_health():
    return {"module": "entries", "status": "ok"}


@entries_bp.route("", methods=["POST"])
@jwt_required
def create_entry_route():
    data = request.get_json()

    habit_id = data.get("habit_id")
    status = data.get("status")

    if habit_id is None or status is None:
        return {"error": "habit_id and status are required"}, 400

    entry = build_entry(habit_id, request.user_id, status)
    create_entry(entry)

    return {"message": "Entry created"}, 201
