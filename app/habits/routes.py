from flask import Blueprint
from flask import request

from app.habits.repository import get_habits_by_user
from app.auth.middleware import jwt_required
from app.habits.models import build_habit
from app.habits.repository import create_habit

habits_bp = Blueprint("habits", __name__, url_prefix="/habits")



@habits_bp.route("", methods=["POST"])
@jwt_required
def create_habit_route():
    data = request.get_json()

    title = data.get("title")
    frequency = data.get("frequency")

    if not title or not frequency:
        return {"error": "title and frequency are required"}, 400

    habit = build_habit(request.user_id, title, frequency)
    create_habit(habit)

    return {"message": "Habit created"}, 201


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

    return {"habits": habits}, 200

