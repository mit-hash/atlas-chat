from datetime import datetime, timezone
from db.mongo import db
from fastapi import APIRouter, HTTPException, Query
from models.message import Message

router = APIRouter(prefix="/chat", tags=["chat"])

@router.get("/{room}/messages")
async def get_messages(room: str, since: str = Query(None)):
    """Get messages by timestamp filter init messages view w/o query"""
    query = {"room": room}
    if since:
        try:
            since_dt = datetime.fromisoformat(since)
            query["timestamp"] = {"$gt": since_dt}
        except ValueError:
            pass  # ignore

    messages_cursor = db.rooms.find(query).sort("timestamp", 1)
    messages = await messages_cursor.to_list(length=50)

    return [
        {"sender": m["sender"], "text": m["text"], "timestamp": m.get("timestamp", datetime.now(timezone.utc)).isoformat()}
        for m in messages
    ]

@router.post("/{room}/messages")
async def post_message(room: str, message: Message):
    """Post new message."""
    await db.rooms.insert_one({
        "room": room,
        "sender": message.sender, 
        "text": message.text, 
        "timestamp": datetime.now(timezone.utc)})
    
    await db.users.update_one(
        {"username": message.sender},
        {"$inc": {"message_count": 1}},
        upsert=True  # creates user doc
    )

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

