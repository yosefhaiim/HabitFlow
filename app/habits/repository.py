# from app.database.db import db
#
# def create_habit(habit_data):
#     return db.habits.insert_one(habit_data)
#
# def get_habits_by_user(user_id):
#     """Retrieve all habits belonging to a specific user."""
#     return list(db.habits.find({"user_id": user_id}))
#
#
# def get_habit_by_id(habit_id, user_id):
#     return db.habits.find_one({
#         "_id": habit_id,
#         "user_id": user_id
#     })
#
#
# def update_habit(habit_id, user_id, updates):
#     return db.habits.update_one(
#         {"_id": habit_id, "user_id": user_id},
#         {"$set": updates}
#     )
#
#
#
# def delete_habit(habit_id, user_id):
#     return db.habits.delete_one({
#         "_id": habit_id,
#         "user_id": user_id
#     })
#
# def delete_habits_by_user(user_id):
#     db.habits.delete_many({"user_id": user_id})



from flask import current_app
from bson import ObjectId  # שימושי אם _id הוא ObjectId

def get_db():
    """Return the current app's MongoDB database."""
    return current_app.extensions["db"]


def create_habit(habit_data: dict):
    """Insert a new habit into the DB."""
    return get_db().habits.insert_one(habit_data)


def get_habits_by_user(user_id):
    """Retrieve all habits belonging to a specific user."""
    return list(get_db().habits.find({"user_id": user_id}))


def get_habit_by_id(habit_id, user_id):
    """Retrieve a specific habit by its ID and owner."""
    # Convert habit_id to ObjectId if needed
    if not isinstance(habit_id, ObjectId):
        habit_id = ObjectId(habit_id)
    return get_db().habits.find_one({
        "_id": habit_id,
        "user_id": user_id
    })


def update_habit(habit_id, user_id, updates: dict):
    """Update a habit with given changes."""
    if not isinstance(habit_id, ObjectId):
        habit_id = ObjectId(habit_id)
    return get_db().habits.update_one(
        {"_id": habit_id, "user_id": user_id},
        {"$set": updates}
    )


def delete_habit(habit_id, user_id):
    """Delete a specific habit."""
    if not isinstance(habit_id, ObjectId):
        habit_id = ObjectId(habit_id)
    return get_db().habits.delete_one({
        "_id": habit_id,
        "user_id": user_id
    })


def delete_habits_by_user(user_id):
    """Delete all habits for a given user."""
    return get_db().habits.delete_many({"user_id": user_id})
