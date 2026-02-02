from datetime import datetime


def build_habit(user_id, title, frequency, reminder_time=None):
    """
    Create a habit object associated with a specific user,
    including optional reminder time.
    """
    return {
        "user_id": user_id,
        "title": title,
        "frequency": frequency,
        "reminder_time": reminder_time,  # "HH:MM"
        "reminder_enabled": reminder_time is not None,
        "created_at": datetime.utcnow()
    }

