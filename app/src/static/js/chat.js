const messagesDiv = document.getElementById("messages");
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");

if (!messagesDiv || !chatForm || !messageInput) {
  console.error("Chat elements missing");
}

if (!username || !room) {
  alert("Missing username or room!");
  window.location.href = "/login.html";
}

//Timestamp to filter messages
let lastTimestamp = null;

/**
 * Add message to MessagesDiv
 */
function appendMessage(msg) {
  if (!msg || !msg.sender || !msg.text) {
    console.warn("Invalid message skipped:", msg);
    return;
  }

  const p = document.createElement("p");
  p.textContent = `${msg.sender}: ${msg.text}`;
  if (msg.sender === username) p.classList.add("self");

  messagesDiv.appendChild(p);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

/**
 * Fetch all messages
 */
async function loadMessages() {
  try {
    const res = await fetch(`/chat/${room}/messages`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const messages = await res.json();

    messagesDiv.innerHTML = '';
    messages.forEach(appendMessage);

    if (messages.length > 0) {
      lastTimestamp = messages[messages.length - 1].timestamp;
    }
  } catch (err) {
    console.error("Error loading messages:", err);
  }
}

/**
 * Load new messages filtered by since recent lastTimestamp value
 */
async function loadNewMessages() {
  try {
    let url = `/chat/${room}/messages`;
    if (lastTimestamp) url += `?since=${encodeURIComponent(lastTimestamp)}`;

    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const messages = await res.json();

    if (messages.length > 0) {
      messages.forEach(appendMessage);
      lastTimestamp = messages[messages.length - 1].timestamp;
    }
  } catch (err) {
    console.error("Error loading new messages:", err);
  }
}

/**
 * Fetch counter of sent messages for given user
 */
async function countMessages() {
  try {
    const res = await fetch(`/users/${encodeURIComponent(username)}/count`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();

    if (typeof data.message_count === "number") {
      console.log(`User ${username} has sent ${data.message_count} messages`);
    } else {
      console.warn("Unexpected response format:", data);
    }
  } catch (err) {
    console.error("Error fetching message count:", err);
  }
}

/**
 * Post new message 
 */
chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = messageInput.value.trim();
  if (!text) return;

  try {
    const res = await fetch(`/chat/${room}/messages`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sender: username, text })
    });

    if (!res.ok) throw new Error(`HTTP ${res.status}`);

    messageInput.value = '';
    await countMessages();
    await loadNewMessages();
  } catch (err) {
    console.error("Error sending message:", err);
  }
});

/**
 * Fetch all chat rooms.
 */
async function listRooms() {
  try {
    const response = await fetch(`/`);
    if (!response.ok) {
      throw new Error(`Failed to fetch rooms: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching rooms:", error);
    return [];
  }
}

/**
 * Fetch all users in a given room
 */
async function listUsersInRoom(roomName) {
  try {
    const response = await fetch(`/${encodeURIComponent(roomName)}/users`);
    if (!response.ok) {
      throw new Error(`Failed to fetch users in room '${roomName}': ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error(`Error fetching users in room ${roomName}:`, error);
    return [];
  }
}

// Initial load + refresh every 2 seconds interval
loadMessages();
setInterval(loadNewMessages, 2000);
