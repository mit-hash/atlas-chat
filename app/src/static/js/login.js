document.getElementById("loginForm").addEventListener("submit", function (event) {
  event.preventDefault();

  const username = document.getElementById("username").value;
  const room = document.getElementById("room").value;

  // Redirect to chat page with params in the URL
  window.location.href = `/chat?username=${encodeURIComponent(username)}&room=${encodeURIComponent(room)}`;
});
