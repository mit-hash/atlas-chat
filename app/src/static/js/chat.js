const messagesDiv = document.getElementById("messages");
const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");

// Fetch existing messages from backend
async function loadMessages() {
  const res = await fetch(`/chat/${room}/messages`);
  const messages = await res.json();

  messagesDiv.innerHTML = '';
  messages.forEach(msg => {
    const p = document.createElement("p");
    p.textContent = `${msg.sender}: ${msg.text}`;
    messagesDiv.appendChild(p);
  });

  messagesDiv.scrollTop = messagesDiv.scrollHeight; // scroll to bottom
}

// Send new message to backend
chatForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const text = messageInput.value;
  if (!text) return;

  await fetch(`/chat/${room}/messages`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ sender: username, text })
  });

  messageInput.value = '';
  loadMessages();
});

// Optional: auto-refresh every 2 seconds
setInterval(loadMessages, 2000);

// Load messages immediately on page load
loadMessages();
