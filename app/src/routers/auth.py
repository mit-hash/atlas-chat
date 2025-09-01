from fastapi import APIRouter, HTTPException, Response, Form
from db.mongo import db
from models.user import User
import uuid

router = APIRouter(prefix="/auth", tags=["auth"])

sessions = {}  # {token: username}

@router.post("/register")
def register(user: User):
    if db.users.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="User already exists")

    db.users.insert_one(user.model_dump())
    return {"message": "User registered successfully"}


@router.post("/login")
def login(response: Response, username: str = Form(...), password: str = Form(...)):
    db_user = db.users.find_one({"username": username})
    if not db_user or db_user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = str(uuid.uuid4())
    sessions[token] = username

    # Set the session token as a cookie
    response.set_cookie(key="session_token", value=token, httponly=True)
    return {"status": "ok"}


@router.post("/logout")
def logout(response: Response, session_token: str = None):
    if session_token in sessions:
        sessions.pop(session_token)
    response.delete_cookie("session_token")
    return {"status": "ok"}


# Helper to get current user from session cookie
def get_current_user(request):
    token = request.cookies.get("session_token")
    if not token or token not in sessions:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return sessions[token]
