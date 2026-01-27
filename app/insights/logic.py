from collections import defaultdict
from datetime import datetime, timedelta



def analyze_entries(entries):
    total = len(entries)
    if total == 0:
        return {
            "success_rate": 0,
            "weak_days": []
        }

    success_count = sum(1 for e in entries if e["status"] is True)

    by_weekday = defaultdict(list)
    for e in entries:
        date = datetime.fromisoformat(e["date"])
        weekday = date.strftime("%A")
        by_weekday[weekday].append(e["status"])

    weak_days = []
    for day, statuses in by_weekday.items():
        rate = sum(statuses) / len(statuses)
        if rate < 0.5:
            weak_days.append(day)

    return {
        "success_rate": round(success_count / total * 100, 2),
        "weak_days": weak_days
    }



def calculate_streaks(entries):
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
