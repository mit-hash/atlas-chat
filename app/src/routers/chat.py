from db.mongo import db
from fastapi import APIRouter
from pydantic import BaseModel
from models.message import Message

router = APIRouter(prefix="/chat", tags=["chat"])

@router.get("/{room}/messages")
async def get_messages(room: str):
    messages_cursor = db.rooms.find({"room": room})
    messages = await messages_cursor.to_list(length=1000)
    return [{"sender": m["sender"], "text": m["text"]} for m in messages]

@router.post("/{room}/messages")
async def post_message(room: str, message: Message):
    await db.rooms.insert_one({"room": room, "sender": message.sender, "text": message.text})
    return {"status": "ok"}

# # Get messages for a room
# def get_messages(room: str):
#     return list(messages_collection.find({"room": room}, {"_id": 0}))
