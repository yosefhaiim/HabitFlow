from datetime import datetime

def build_habit(user_id, title, frequency):
    """Create a habit object associated with a specific user."""
    return {
        "user_id": user_id,
        "title": title,
        "frequency": frequency,
        "created_at": datetime.utcnow()
    }
