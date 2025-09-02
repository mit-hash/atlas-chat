# FastAPI Chat App

A real-time chat application built with FastAPI and MongoDB, supporting multiple rooms, message history, and per-user message counts. Designed with simplicity, efficiency, and maintainability in mind.

---

## Design Decisions & Trade-offs

- **Jinja2 templates**: Chosen for server-side rendering of chat pages. Simpler than a full frontend framework and keeps the app lightweight.
- **Message counter per user**: Stored in MongoDB to reduce repeated computation for `/users/{username}/count` requests. This precomputation trades a small amount of storage for faster reads.
- **Polling for new messages**: Implemented via repeated fetch requests. Simpler than WebSockets for a minimal implementation and avoids extra complexity. Could be replaced with WebSockets in future iterations for true real-time updates.

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

---

## Running Locally

### Option 1: Docker (recommended)

```bash
docker-compose up --build
````

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

* Switch from polling to WebSockets for real-time updates
* Add authentication and session management for multi-user security
* Optimize message queries with indexes
* Enhance UI/UX with a frontend framework

---

## API & Chat Endpoints

### Authentication & Users

| Method | Endpoint                  | Description                                      |
| ------ | ------------------------- | ------------------------------------------------ |
| POST   | `/auth/login`             | Log in a user (creates session cookie).          |
| POST   | `/auth/logout`            | Log out the user (deletes session cookie).       |
| GET    | `/auth/me`                | Get the current logged-in username.              |
| GET    | `/users/{username}/count` | Get the total number of messages sent by a user. |

### Chat Rooms & Messages

| Method | Endpoint                | Description                                                                                            |
| ------ | ----------------------- | ------------------------------------------------------------------------------------------------------ |
| GET    | `/chat/`                | List all existing rooms.                                                                               |
| GET    | `/chat/{room}/messages` | Fetch messages for a room. Supports optional query `since` (ISO timestamp) to get only newer messages. |
| POST   | `/chat/{room}/messages` | Post a new message to a room. Request body: `{ sender: string, text: string }`.                        |
| GET    | `/chat/{room}/users`    | List all users in a given room.                                                                        |

---

### Message Counter Example

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

---

### Notes & Trade-offs

* Messages are sorted by timestamp and limited to recent entries for performance.
* Message counts are precomputed per user to avoid repeated expensive aggregation queries.
* Rooms and messages are stored in MongoDB, which allows flexible document schemas.
