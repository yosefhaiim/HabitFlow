from pymongo import MongoClient

def init_db(app):
    """Initialize the MongoDB client and store the DB in app.extensions."""
    client = MongoClient("mongodb://localhost:27017")  # או ה־URI שלך
    app.extensions["db"] = client["habitflow"]  # בחר את שם בסיס הנתונים שלך
    print("MongoDB initialized:", app.extensions["db"])



# def init_db(app):
#     global client, db
#     client = MongoClient(app.config["MONGO_URI"])
#     db = client.get_default_database()
