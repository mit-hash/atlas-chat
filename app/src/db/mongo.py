from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client["chat_app"]

# rooms_collection = db.rooms
# messages_collection = db.messages
# users_collection = db.users
