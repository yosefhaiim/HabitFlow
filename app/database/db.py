from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")  # או כתובת MongoDB Atlas
db = client["habitflow_db"]
