from flask import Blueprint
from flask import request

from app.auth.middleware import jwt_required
from app.entries.models import build_entry
from app.entries.repository import create_entry
from app.entries.repository import entry_exists
from app.utils.responses import error_response, success_response
from app.habits.repository import get_habit_by_id
from datetime import datetime
from app.entries.repository import get_entry_by_id, update_entry
from app.entries.repository import delete_entry


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


@entries_bp.route("/<entry_id>", methods=["PATCH"])
@jwt_required
def update_entry_route(entry_id):
    entry = get_entry_by_id(entry_id, request.user_id)

    if not entry:
        return error_response("Entry not found", 404)

    today = datetime.utcnow().date().isoformat()
    if entry["date"] != today:
        return error_response("Only today's entry can be updated", 403)

    data = request.json or {}
    allowed_fields = {"status", "duration", "note"}
    updates = {k: v for k, v in data.items() if k in allowed_fields}

    if not updates:
        return error_response("No valid fields to update", 400)

    update_entry(entry_id, request.user_id, updates)

    return success_response(message="Entry updated successfully")



@entries_bp.route("/<entry_id>", methods=["DELETE"])
@jwt_required
def delete_entry_route(entry_id):
    entry = get_entry_by_id(entry_id, request.user_id)

    if not entry:
        return error_response("Entry not found", 404)

    today = datetime.utcnow().date().isoformat()
    if entry["date"] != today:
        return error_response("Only today's entry can be deleted", 403)

    delete_entry(entry_id, request.user_id)

    return success_response(message="Entry deleted successfully")
