# from app.database.db import db
#
# def get_entries_for_habit(habit_id, user_id):
#     return list(db.entries.find({
#         "habit_id": habit_id,
#         "user_id": user_id
#     }))


from flask import current_app

def get_db():
    """Return the current app's MongoDB database."""
    return current_app.extensions["db"]


def get_entries_for_habit(habit_id, user_id):
    """Retrieve all entries for a specific habit and user."""
    return list(get_db().entries.find({
        "habit_id": habit_id,
        "user_id": user_id
    }))
