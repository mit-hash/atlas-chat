# atlas-chat

Interview Exercise – Chat Application
Goal
We’d like you to design and implement a simple chat application. The exercise is meant to test your ability to design, structure, and implement a fullstack solution. We’re not looking for a perfect or production-ready app – focus instead on showing good design, clear thinking, and reasonable tradeoffs.
The app should have two parts:
1. Frontend
- A simple web interface with two pages:
  1. Login / Join Room page
     - Enter a username and a room name.
     - On submit, the user is taken to the chat room.
  2. Chat Room page
     - Shows the chat messages for the room.
     - Has an input field to send new messages in.

- No need for fancy styling – simple and functional is fine.
2. Backend (Python, FastAPI)
- A REST API that supports the frontend requirements.
- Data may be stored in an in-memory data structure (e.g. dictionaries, lists).
- (Bonus: you can use a local MongoDB for persistence.)
Requirements for the Backend
The backend should expose endpoints to support at least the following:
- Create / join a room (a user provides a username and a room name).
- Post a message in a room.
- Retrieve messages for a room.
Additional Functionality
- Listing all rooms that currently exist.
- Listing all users in a given room.
- The number of messages in each room.
- The number of messages sent by each user overall (across all rooms).
- (Optional, bonus) Simple authentication 
Deliverables
A working project with:
- Backend code (FastAPI)
- Frontend code (any framework or plain HTML/JS is fine)
- A README.md explaining:
  - How to run the app.
  - The API endpoints (input/output examples).
  - Any design choices you made.
  - Any bonus features you implemented.
Notes
- Keep it simple – we’re more interested in your design and problem-solving approach than in pixel-perfect UI.
- Organize your code as if you were handing it off to a team.


setup:
1. run mongodb
2. install dependencies
3. run: uvicorn main:app --reload 
--or--
3. setup a docker/ container for the app to run