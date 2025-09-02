from pydantic import BaseModel

# Define the shape of a message
class User(BaseModel):
    username: str
    #password: 