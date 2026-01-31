from app.database.db import db

def create_entry(entry_data):
    return db.entries.insert_one(entry_data)

def get_entries_for_habit(habit_id, user_id):
    return list(db.entries.find({
        "habit_id": habit_id,
        "user_id": user_id
    }))

def entry_exists(habit_id, user_id, date):
    return db.entries.find_one({
        "habit_id": habit_id,
        "user_id": user_id,
        "date": date
    })
