from datetime import datetime

def build_habit(user_id, title, frequency):
    return {
        "user_id": user_id,
        "title": title,
        "frequency": frequency,
        "created_at": datetime.utcnow()
    }
