from app.database.db import db

def create_habit(habit_data):
    return db.habits.insert_one(habit_data)

def get_habits_by_user(user_id):
    return list(db.habits.find({"user_id": user_id}))
