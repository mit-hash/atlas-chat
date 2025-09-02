// const messagesDiv = document.getElementById("messages");
// const chatForm = document.getElementById("chatForm");
// const messageInput = document.getElementById("messageInput");

// let lastTimestamp = null;

// // Helper to append a message
// function appendMessage(msg) {
//   const p = document.createElement("p");
//   p.textContent = `${msg.sender}: ${msg.text}`;

//   if (msg.sender === username) p.classList.add("self");

//   messagesDiv.appendChild(p);
//   messagesDiv.scrollTop = messagesDiv.scrollHeight;
// }

// // Load all messages initially
// async function loadMessages() {
//   const res = await fetch(`/chat/${room}/messages`);
//   const messages = await res.json();

//   messagesDiv.innerHTML = '';
//   messages.forEach(appendMessage);

//   if (messages.length > 0) {
//     lastTimestamp = messages[messages.length - 1].timestamp;
//   }
// }

// // Load only new messages
// async function loadNewMessages() {
//   let url = `/chat/${room}/messages`;
//   if (lastTimestamp) url += `?since=${encodeURIComponent(lastTimestamp)}`;

//   const res = await fetch(url);
//   const messages = await res.json();

//   if (messages.length > 0) {
//     messages.forEach(appendMessage);
//     lastTimestamp = messages[messages.length - 1].timestamp;
//   }
// }

// // Send new message
// chatForm.addEventListener("submit", async (e) => {
//   e.preventDefault();
//   const text = messageInput.value.trim();
//   if (!text) return;

//   await fetch(`/chat/${room}/messages`, {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ text })
//   });

//   messageInput.value = '';
//   loadNewMessages();
// });

// // Initial load + auto-refresh
// loadMessages();
// setInterval(loadNewMessages, 2000);

const messagesDiv = document.getElementById("messages");
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");

// Get username & room from URL
// const urlParams = new URLSearchParams(window.location.search);
// const username = urlParams.get("username");
// const room = urlParams.get("room");

if (!username || !room) {
  alert("Missing username or room!");
  window.location.href = "/login.html";
}

let lastTimestamp = null;

// Helper to append a message
function appendMessage(msg) {
  const p = document.createElement("p");
  p.textContent = `${msg.sender}: ${msg.text}`;
  if (msg.sender === username) p.classList.add("self");
  messagesDiv.appendChild(p);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

// Load all messages initially
async function loadMessages() {
  const res = await fetch(`/chat/${room}/messages`);
  const messages = await res.json();

  messagesDiv.innerHTML = '';
  messages.forEach(appendMessage);

  if (messages.length > 0) {
    lastTimestamp = messages[messages.length - 1].timestamp;
  }
}

// Load only new messages
async function loadNewMessages() {
  let url = `/chat/${room}/messages`;
  if (lastTimestamp) url += `?since=${encodeURIComponent(lastTimestamp)}`;

  const res = await fetch(url);
  const messages = await res.json();

  if (messages.length > 0) {
    messages.forEach(appendMessage);
    lastTimestamp = messages[messages.length - 1].timestamp;
  }
}

// Send new message
chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const text = messageInput.value.trim();
  if (!text) return;

  await fetch(`/chat/${room}/messages`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sender: username, text })
  });

  messageInput.value = '';
  loadNewMessages();
});

// Initial load + auto-refresh
loadMessages();
setInterval(loadNewMessages, 2000);
