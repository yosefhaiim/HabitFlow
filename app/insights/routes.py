from flask import Blueprint
from flask import request

from app.auth.middleware import jwt_required
from app.insights.repository import get_entries_for_habit

from app.insights.logic import (
    analyze_entries,
    calculate_streaks,
    generate_recommendations
)


insights_bp = Blueprint("insights", __name__, url_prefix="/insights")

@insights_bp.route("/health")
def insights_health():
    return {"module": "insights", "status": "ok"}


@insights_bp.route("/habit", methods=["GET"])
@jwt_required
def habit_insights():
    habit_id = request.args.get("habit_id")

    if not habit_id:
        return {"error": "habit_id is required"}, 400

    entries = get_entries_for_habit(habit_id, request.user_id)

    analysis = analyze_entries(entries)
    streaks = calculate_streaks(entries)
    recommendations = generate_recommendations(analysis, streaks)

    return {
        **analysis,
        **streaks,
        "recommendations": recommendations
    }, 200




