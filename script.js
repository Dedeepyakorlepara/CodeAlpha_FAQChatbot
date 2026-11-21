
async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();

    if (message === "") {
        alert("Please enter a question!");
        return;
    }

    // Display user message
    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.textContent = message;
    chatBox.appendChild(userDiv);

    input.value = "";

    try {
        const response = await fetch("/get", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: message })
        });

        const data = await response.json();

        // Display chatbot answer
        const botDiv = document.createElement("div");
        botDiv.className = "bot-message";
        botDiv.textContent = data.answer;
        chatBox.appendChild(botDiv);

        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        const errorDiv = document.createElement("div");
        errorDiv.className = "bot-message";
        errorDiv.textContent = "Something went wrong. Please try again.";
        chatBox.appendChild(errorDiv);
    }
}

// Send message when Enter key is pressed
document.getElementById("user-input").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});
