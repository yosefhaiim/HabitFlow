from app.database.db import db

def get_entries_for_habit(habit_id, user_id):
    return list(db.entries.find({
        "habit_id": habit_id,
        "user_id": user_id
    }))
