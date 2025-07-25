function toggleChatbot() {
  const bot = document.getElementById("chatbot");
  bot.style.display = bot.style.display === "flex" ? "none" : "flex";
}

function handleEnter(event) {
  if (event.key === "Enter") {
    sendMessage();
  }
}

function sendMessage(text = null) {
  const input = document.getElementById("user-input");
  const message = text || input.value.trim();
  if (!message) return;

  appendMessage("user", message);
  input.value = "";

  fetch("/api/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mensaje: message })
  })
    .then(res => res.json())
    .then(data => {
      appendMessage("bot", data.respuesta);
      speakText(data.respuesta);
    })
    .catch(() => {
      appendMessage("bot", "❌ Error al contactar el servidor.");
    });
}

function appendMessage(sender, text) {
  const chat = document.getElementById("chat-body");
  const div = document.createElement("div");
  div.className = sender === "bot" ? "bot-message" : "user-message";
  div.textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

// 🎤 Reconocimiento de voz
let recognition;
function startListening() {
  if (!("webkitSpeechRecognition" in window)) {
    alert("Tu navegador no soporta reconocimiento de voz.");
    return;
  }

  recognition = new webkitSpeechRecognition();
  recognition.lang = "es-DO";
  recognition.continuous = false;
  recognition.interimResults = false;

  recognition.onstart = () => {
    appendMessage("bot", "🎙️ Escuchando...");
  };

  recognition.onresult = event => {
    const result = event.results[0][0].transcript;
    sendMessage(result);
  };

  recognition.onerror = event => {
    appendMessage("bot", "❌ No se pudo escuchar. Inténtalo de nuevo.");
  };

  recognition.start();
}

// 🗣️ Voz de salida
function speakText(text) {
  if ("speechSynthesis" in window) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "es-DO";
    speechSynthesis.speak(utterance);
  }
}
