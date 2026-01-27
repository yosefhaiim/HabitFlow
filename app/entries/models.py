from datetime import datetime

def build_entry(habit_id, user_id, status, date=None):
    return {
        "habit_id": habit_id,
        "user_id": user_id,
        "status": status,  # True / False
        "date": date or datetime.utcnow().date().isoformat()
    }
