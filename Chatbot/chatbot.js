const input = document.getElementById('chat-input');
const sendBtn = document.getElementById('chat-send');
const messages = document.getElementById('chat-messages');

// Función para agregar mensajes al chat con avatar
function addMessage(text, sender) {
  const div = document.createElement('div');
  div.classList.add('message', sender);

  const avatar = document.createElement('img');
  avatar.classList.add('avatar');
  avatar.src = sender === 'user' ? 'imagenes/usuario.png' : 'imagenes/botxd.jpg';
  avatar.alt = sender === 'user' ? 'Usuario' : 'Chatbot';

  const messageText = document.createElement('div');
  messageText.classList.add('text');
  messageText.innerHTML = text;  // Interpretar HTML

  div.appendChild(avatar);
  div.appendChild(messageText);

  messages.appendChild(div);
  messages.scrollTop = messages.scrollHeight;
}

// Array de saludos y palabras para mostrar menú
const palabrasMenu = [
  'hola', 'buenos días', 'buenas tardes', 'buenas noches', 'hey', 'buen día', 'qué tal', 'buenas',
  'menu', 'menu de opciones', 'opciones', 'tabla'
];

function contienePalabraMenu(texto) {
  return palabrasMenu.some(palabra => texto.includes(palabra));
}

async function getResponse(message) {
  const lower = message.toLowerCase();

  // Mostrar menú si alguna palabra de menú está en el mensaje
  if (contienePalabraMenu(lower)) {
    return `¡Hola! Soy tu asistente virtual para la hackatón de Ingeniería de Sistemas.<br>
¿En qué puedo ayudarte hoy? Selecciona una opción o escribe tu pregunta.<br>
1. Información sobre la hackatón.<br>
2. Asistencia técnica.<br>
3. Recordatorios importantes.<br>
4. Recursos útiles.<br>
5. Preguntas generales.`;
  }

  if (lower === '1' || lower.includes('información sobre la hackatón')) {
    return `La hackatón comienza el 1 de junio y termina el 3 de junio. Los premios son...<br>
¿Te gustaría conocer la agenda del evento?`;
  }

  if (lower === '2' || lower.includes('asistencia técnica')) {
    return '¿En qué lenguaje o tecnología necesitas ayuda? (Ej. Python, JavaScript, APIs)';
  }

  if (lower === '3' || lower.includes('recordatorios')) {
    return 'Recuerda que el plazo de inscripción cierra el 30 de mayo. También, el primer taller será el 1 de junio a las 9:00 AM.';
  }

  if (lower === '4' || lower.includes('recursos')) {
    return 'Aquí tienes un enlace a tutoriales sobre Python: https://www.python.org/about/gettingstarted/';
  }

  if (lower === '5' || lower.includes('preguntas generales')) {
    return 'Puedes preguntarme cosas como: ¿Cómo me registro en la hackatón? o ¿Qué lenguajes puedo usar?';
  }

  if (lower.includes('github')) {
    return 'Para subir tu código a GitHub, primero crea un repositorio, luego usa git add, commit y push. Aquí tienes un tutorial: https://docs.github.com/es/github/using-git';
  }

  // Si no coincide, llama a IA
try {
    const res = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",
        "messages": [
          {
            "role": "user",
            "content": message
          }
        ]
      })
    });

    if (!res.ok) {
      throw new Error(`HTTP error! status: ${res.status}`);
    }

    const data = await res.json();
    return data.choices[0].message.content; // Ajusta según la estructura real de la respuesta
  } catch (error) {
    console.error(error);
    return "Lo siento, no puedo responder ahora. Por favor intenta más tarde.";
  }
}

// Manejar evento de enviar mensaje
sendBtn.addEventListener('click', async () => {
  const text = input.value.trim();
  if (!text) return;
  addMessage(text, 'user');
  input.value = '';

  const response = await getResponse(text);
  addMessage(response, 'bot');
});

// Permitir enviar con tecla Enter
input.addEventListener('keydown', e => {
  if (e.key === 'Enter') sendBtn.click();
});
