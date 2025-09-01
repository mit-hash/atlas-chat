from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.chat_app

rooms_collection = db.rooms
messages_collection = db.messages
users_collection = db.users
