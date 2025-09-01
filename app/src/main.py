from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# In-memory storage for simplicity
rooms = {}

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request, username: str, room: str):
    # Pass username and room to template
    return templates.TemplateResponse("chat.html", {"request": request, "username": username, "room": room})

# Backend API for messages
from pydantic import BaseModel
from typing import List

class Message(BaseModel):
    sender: str
    text: str

@app.get("/chat/{room}/messages")
def get_messages(room: str):
    return rooms.get(room, [])

@app.post("/chat/{room}/messages")
def post_message(room: str, message: Message):
    if room not in rooms:
        rooms[room] = []
    rooms[room].append(message.model_dump())
    return {"status": "ok"}
