from pydantic import BaseModel

# Define the shape of a user
class User(BaseModel):
    username: str
    #password: 