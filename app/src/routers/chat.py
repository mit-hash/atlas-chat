from db.mongo import db
from fastapi import APIRouter, HTTPException
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

@router.get("/")
async def list_rooms():
    """List all existing rooms."""
    rooms = await db.rooms.distinct("name")
    return rooms


@router.get("/{room}/users")
async def list_users_in_room(room_name: str):
    """List all users in a given room."""
    room = await db.rooms.find_one({"name": room_name})
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room.get("users", [])


@router.get("/{room}/messages/count")
async def count_messages_in_room(room_name: str):
    """Get the number of messages in a given room."""
    count = await db.messages.count_documents({"room": room_name})
    return {"room": room_name, "message_count": count}


# # Get messages for a room
# def get_messages(room: str):
#     return list(messages_collection.find({"room": room}, {"_id": 0}))
# - Listing all rooms that currently exist.
# - Listing all users in a given room.
# - The number of messages in each room.
# - The number of messages sent by each user overall (across all rooms).