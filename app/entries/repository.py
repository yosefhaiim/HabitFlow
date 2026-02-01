from app.database.db import db

def create_entry(entry_data):
    return db.entries.insert_one(entry_data)

def get_entries_for_habit(habit_id, user_id):
    return list(db.entries.find({
        "habit_id": habit_id,
        "user_id": user_id
    }))

def entry_exists(habit_id, user_id, date):
    """Check if a habit entry already exists for a given date."""
    return db.entries.find_one({
        "habit_id": habit_id,
        "user_id": user_id,
        "date": date
    })

def delete_entries_by_habit(habit_id, user_id):
    db.entries.delete_many({
        "habit_id": habit_id,
        "user_id": user_id
    })

def get_entry_by_id(entry_id, user_id):
    return db.entries.find_one({
        "_id": entry_id,
        "user_id": user_id
    })

def update_entry(entry_id, user_id, updates):
    return db.entries.update_one(
        {"_id": entry_id, "user_id": user_id},
        {"$set": updates}
    )


def delete_entry(entry_id, user_id):
    return db.entries.delete_one({
        "_id": entry_id,
        "user_id": user_id
    })


def delete_entries_by_user(user_id):
    db.entries.delete_many({"user_id": user_id})
