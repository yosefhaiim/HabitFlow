from flask import Blueprint
from flask import request

from app.auth.middleware import jwt_required
from app.entries.models import build_entry
from app.entries.repository import create_entry
from app.entries.repository import entry_exists
from datetime import datetime
from app.utils.responses import error_response, success_response
from app.habits.repository import get_habit_by_id


entries_bp = Blueprint("entries", __name__, url_prefix="/entries")


@entries_bp.route("", methods=["POST"])
@jwt_required
def create_entry_route():
    data = request.get_json()

    habit_id = data.get("habit_id")
    status = data.get("status")

    if habit_id is None or status is None:
        return error_response("habit_id and status are required", 400)

    date = datetime.utcnow().date().isoformat()

    if entry_exists(habit_id, request.user_id, date):
        return error_response("Entry already exists for today", 409)

    if not get_habit_by_id(habit_id, request.user_id):
        return error_response("Habit not found", 404)


    entry = build_entry(habit_id, request.user_id, status)
    create_entry(entry)

    return success_response(message="Entry created", status_code=201)




