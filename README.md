
# Atlas Chat App

A simplified chat application built with FastAPI and MongoDB, supporting multiple rooms and message history.

---

## Design & Trade-offs

- **Jinja2 templates**: Chosen for server-side rendering of chat pages. Simpler than a full frontend framework and keeps the app lightweight. A production ready app should support a separate frontend FW such as React to maintain full scalability.
- **Message counter per user**: Stored in MongoDB to reduce repeated computation for `/users/{username}/count` requests. This precomputation trades a small amount of storage for faster reads.
- **Polling for new messages**: Implemented via repeated fetch requests to load updating messages from DB. Simpler to implement than WebSockets for a minimal implementation and avoids extra complexity. Should be replaced with WebSockets or similar solutions in future iterations for true real-time updates.

### Predetermined stack

- **FastAPI**: Async, lightweight, integrates well with MongoDB.
- **MongoDB**: Flexible schema for messages, rooms, and users.

---

## Features

- Multiple chat rooms
- Send and view messages
- Message history with timestamps
- Per-user message count
- Minimal, functional UI with Jinja2
- Future bonus, not implemented: user authentication 

---

### Notes & Trade-offs

* Messages are sorted by timestamp and limited to recent entries for performance.
* Message counts are precomputed per user to avoid repeated expensive aggregation queries.
* Rooms and messages are stored in MongoDB, which allows flexible document schemas.

---

## Running Locally

### Option 1: Docker

```bash
docker-compose up --build
```

* FastAPI runs on: [http://localhost:8000](http://localhost:8000)
* MongoDB runs inside the container

### Option 2: Manual setup

1. Install and run MongoDB:

```bash
sudo systemctl start mongod
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Run FastAPI:

```bash
uvicorn main:app --reload
```

---

## Future Improvements

* Switch from polling messages to WebSockets for real-time updates or similar mechanism
* Add authentication and session management for multi-user security
* Optimize message queries
* Enhance UI/UX with a separate service for scalability + frontend framework

---

## API & Chat Endpoints

### Authentication & Users

| Method | Endpoint                  | Description                                      |
| ------ | ------------------------- | ------------------------------------------------ |
| GET    | `/users/{username}/count` | Get the total number of messages sent by a user. |

### Future authentication support 

| Method | Endpoint                  | Description                                      |
| ------ | ------------------------- | ------------------------------------------------ |
| POST   | `/auth/login`             | Log in a user (creates session cookie).          |
| POST   | `/auth/logout`            | Log out the user (deletes session cookie).       |
| GET    | `/auth/me`                | Get the current logged-in username.              |

### Chat Rooms & Messages

| Method | Endpoint                | Description                                                                                            |
| ------ | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| GET    | `/chat/`                | List all existing rooms.                                                                               |
| GET    | `/chat/{room}/messages` | Fetch messages for a room. Supports optional query `since` (ISO timestamp) to get only newer messages. |
| POST   | `/chat/{room}/messages` | Post a new message to a room. Request body: `{ sender: string, text: string }`.                        |
| GET    | `/chat/{room}/users`    | List all users in a given room.                                                                        |

---

### Message Counter API call Example

```javascript
async function countMessages(username) {
  const res = await fetch(`/users/${username}/count`);
  if (!res.ok) {
    console.error("Failed to fetch message count:", res.status);
    return;
  }
  const data = await res.json();
  console.log(`User ${username} has sent ${data.message_count} messages`);
}
```

