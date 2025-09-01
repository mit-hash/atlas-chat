#from db.mongo import messages_collection
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/chat", tags=["chat"])

class Message(BaseModel):
    sender: str
    text: str

rooms = {}

@router.get("/{room}/messages")
def get_messages(room: str):
    return rooms.get(room, [])

@router.post("/{room}/messages")
def post_message(room: str, message: Message):
    if room not in rooms:
        rooms[room] = []
    rooms[room].append(message.model_dump())
    return {"status": "ok"}

# # Get messages for a room
# def get_messages(room: str):
#     return list(messages_collection.find({"room": room}, {"_id": 0}))
