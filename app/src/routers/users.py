from fastapi import APIRouter
from db.mongo import db

router = APIRouter(prefix="/users", tags=["auth"])

@router.get("/{username}/count")
async def get_message_count(username: str):
    user = await db.users.find_one({"username": username}, {"message_count": 1})
    return {"username": username, "message_count": user.get("message_count", 0) if user else 0}
