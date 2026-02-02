from collections import defaultdict
from datetime import datetime, timedelta



def analyze_entries(entries):
    """
    Analyze habit entries to calculate success rate,
    weak days, and per-day statistics.
    """

    total = len(entries)
    success = sum(1 for e in entries if e["status"] is True)

    success_rate = (success / total * 100) if total > 0 else 0

    day_stats = defaultdict(lambda: {"success": 0, "fail": 0})

    for entry in entries:
        date_obj = datetime.fromisoformat(entry["date"])
        day_name = date_obj.strftime("%A")

        if entry["status"]:
            day_stats[day_name]["success"] += 1
        else:
            day_stats[day_name]["fail"] += 1

    weak_days = [
        day for day, stats in day_stats.items()
        if stats["fail"] > stats["success"]
    ]

    worst_day = None
    max_failures = 0

    for day, stats in day_stats.items():
        if stats["fail"] > max_failures:
            max_failures = stats["fail"]
            worst_day = day

    return {
        "success_rate": round(success_rate, 2),
        "weak_days": weak_days,
        "day_stats": dict(day_stats),
        "worst_day": worst_day
    }



def calculate_streaks(entries):
    """Calculate current and maximum streaks of habit completion."""
    if not entries:
        return {"current_streak": 0, "max_streak": 0}

    dates = sorted(
        [datetime.fromisoformat(e["date"]).date() for e in entries if e["status"]],
        reverse=True
    )

    current_streak = 0
    today = dates[0]

    for i, d in enumerate(dates):
        if d == today - timedelta(days=i):
            current_streak += 1
        else:
            break

    max_streak = 1
    streak = 1

    for i in range(1, len(dates)):
        if dates[i] == dates[i-1] - timedelta(days=1):
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 1

    return {
        "current_streak": current_streak,
        "max_streak": max_streak
    }


def generate_recommendations(analysis, streaks):
    """Generate personalized recommendations based on user behavior."""
    recommendations = []

    if analysis["weak_days"]:
        days = ", ".join(analysis["weak_days"])
        recommendations.append(
            f"You tend to struggle on {days}. Consider lowering the habit intensity on these days."
        )

    if streaks["current_streak"] == 0:
        recommendations.append(
            "You currently have no active streak. Try starting with a small, achievable goal today."
        )

    if streaks["current_streak"] >= 5:
        recommendations.append(
            "Great job maintaining your habit! Consider increasing the challenge slightly."
        )

    return recommendations
