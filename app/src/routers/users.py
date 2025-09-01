from fastapi import APIRouter
from db.mongo import db

router = APIRouter(prefix="/users", tags=["auth"])

@router.get("/users/messages/count")
async def count_messages_by_user():
    """Get the number of messages sent by each user across all rooms."""
    pipeline = [
        {"$group": {"_id": "$user", "count": {"$sum": 1}}}
    ]
    results = await db.messages.aggregate(pipeline).to_list(None)
    return {r["_id"]: r["count"] for r in results}