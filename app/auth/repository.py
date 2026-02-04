# from app.database.db import db
#
# def get_user_by_email(email):
#     return db.users.find_one({"email": email})
#
# def create_user(user_data):
#     return db.users.insert_one(user_data)
#
# def delete_user(user_id):
#     return db.users.delete_one({"_id": user_id})



from flask import current_app
from bson import ObjectId

def get_db():
    """Return the current app's MongoDB database."""
    return current_app.extensions["db"]


def get_user_by_email(email: str):
    """Retrieve a user document by email."""
    return get_db().users.find_one({"email": email})


def create_user(user_data: dict):
    """Insert a new user into the database."""
    return get_db().users.insert_one(user_data)


def delete_user(user_id):
    """Delete a user by their ID."""
    if not isinstance(user_id, ObjectId):
        user_id = ObjectId(user_id)
    return get_db().users.delete_one({"_id": user_id})
