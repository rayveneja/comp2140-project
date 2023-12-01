function attemptLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const loginMessage = document.getElementById("loginMessage");

    // Simple validation for demonstration
    if (username === "user123" && password === "password") {
        loginMessage.style.color = "#28a745";
        loginMessage.textContent = "Login successful!";
    } else {
        loginMessage.style.color = "#dc3545";
        loginMessage.textContent = "Invalid username or password. Please try again.";
    }
}
