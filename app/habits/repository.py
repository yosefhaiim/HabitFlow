from app.database.db import db

def create_habit(habit_data):
    return db.habits.insert_one(habit_data)

def get_habits_by_user(user_id):
    """Retrieve all habits belonging to a specific user."""
    return list(db.habits.find({"user_id": user_id}))


def get_habit_by_id(habit_id, user_id):
    return db.habits.find_one({
        "_id": habit_id,
        "user_id": user_id
    })


def update_habit(habit_id, user_id, updates):
    return db.habits.update_one(
        {"_id": habit_id, "user_id": user_id},
        {"$set": updates}
    )



def delete_habit(habit_id, user_id):
    return db.habits.delete_one({
        "_id": habit_id,
        "user_id": user_id
    })
