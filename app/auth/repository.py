from app.database.db import db

def get_user_by_email(email):
    return db.users.find_one({"email": email})

def create_user(user_data):
    return db.users.insert_one(user_data)
