from pydantic import BaseModel

# Define the shape of a message
class Message(BaseModel):
    sender: str
    text: str
