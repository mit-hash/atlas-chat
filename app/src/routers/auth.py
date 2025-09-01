from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(username: str, password: str):
    if username == "test" and password == "123":
        return {"status": "ok", "user": username}
    return {"status": "error", "message": "Invalid credentials"}

# @app.post("/login")
# async def login(username: str = Form(...)):
#     # Simple check (no DB for now)
#     if username.strip():
#         # Save the username in session or just pass via query
#         return RedirectResponse(url=f"/chat?user={username}", status_code=303)
#     return RedirectResponse(url="/", status_code=303)

# @app.post("/register")
# def register(user: User):
#     # check if user exists
#     if users_collection.find_one({"username": user.username}):
#         raise HTTPException(status_code=400, detail="User already exists")

#     users_collection.insert_one(user.dict())
#     return {"message": "User registered successfully"}
