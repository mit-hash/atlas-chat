from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routers import chat, auth, users

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(chat.router)
app.include_router(auth.router)
app.include_router(users.router)

@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request, username: str, room: str):
    return templates.TemplateResponse("chat.html", {"request": request, "username": username, "room": room})

@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})
