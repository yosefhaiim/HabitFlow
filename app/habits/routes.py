from flask import Blueprint
from flask import request

from app.entries.repository import delete_entries_by_habit
from app.habits.repository import get_habits_by_user, update_habit, delete_habit
from app.auth.middleware import jwt_required
from app.habits.models import build_habit
from app.habits.repository import create_habit
from app.utils.responses import success_response, error_response

habits_bp = Blueprint("habits", __name__, url_prefix="/habits")



@habits_bp.route("", methods=["POST"])
@jwt_required
def create_habit_route():
    data = request.get_json()

    title = data.get("title")
    frequency = data.get("frequency")
    reminder_time = data.get("reminder_time")  # "HH:MM"

    if not title or not frequency:
        return error_response("title and frequency are required", 400)

    habit = build_habit(
        request.user_id,
        title,
        frequency,
        reminder_time
    )
    create_habit(habit)

    return success_response("Habit created", 201)


@habits_bp.route("/protected")
@jwt_required
def protected_test():
    return {"message": "Access granted"}


@habits_bp.route("", methods=["GET"])
@jwt_required
def get_habits_route():
    habits = get_habits_by_user(request.user_id)

    for habit in habits:
        habit["_id"] = str(habit["_id"])

    return success_response(f"habits: {habits}", 200)


@habits_bp.route("/<habit_id>", methods=["PATCH"])
@jwt_required
def update_habit_route(habit_id):
    data = request.json or {}

    allowed_fields = {"title", "frequency"}
    updates = {k: v for k, v in data.items() if k in allowed_fields}

    if "reminder_time" in data:
        updates["reminder_time"] = data["reminder_time"]
        updates["reminder_enabled"] = True

    if not updates:
        return error_response("No valid fields to update", 400)

    result = update_habit(habit_id, request.user_id, updates)

    if result.matched_count == 0:
        return error_response("Habit not found", 404)

    return success_response(message="Habit updated successfully")


@habits_bp.route("/<habit_id>", methods=["DELETE"])
@jwt_required
def delete_habit_route(habit_id):
    delete_entries_by_habit(habit_id, request.user_id)
    result = delete_habit(habit_id, request.user_id)

    if result.deleted_count == 0:
        return error_response("Habit not found", 404)

    return success_response(message="Habit deleted successfully")
