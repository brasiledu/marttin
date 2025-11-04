// filepath: /Users/eduardovinicius/Faculdade/marttin/marttin/agent/static/agent/js/chat.js
let conversationHistory = [];

function autoResize(textarea) {
  if (!textarea) return;
  textarea.style.height = 'auto';
  textarea.style.height = Math.min(textarea.scrollHeight, 200) + 'px';
}

function addMessage(content, isUser = false, isHtml = false) {
  const messagesContainer = document.getElementById('chatMessages');
  const emptyState = document.getElementById('emptyState');
  if (!messagesContainer) return;

  if (emptyState && emptyState.style.display !== 'none') {
    emptyState.style.display = 'none';
  }

  const messageDiv = document.createElement('div');
  messageDiv.className = `message ${isUser ? 'user' : 'assistant'}`;

  const wrapperDiv = document.createElement('div');
  wrapperDiv.className = 'message-content-wrapper';

  const avatarDiv = document.createElement('div');
  avatarDiv.className = 'message-avatar';
  avatarDiv.innerHTML = isUser ? '<i class="bi bi-person"></i>' : '<i class="bi bi-cpu"></i>';

  const contentDiv = document.createElement('div');
  contentDiv.className = 'message-content';
  if (isHtml) {
    contentDiv.innerHTML = content;
  } else {
    contentDiv.textContent = content;
  }

  wrapperDiv.appendChild(avatarDiv);
  wrapperDiv.appendChild(contentDiv);
  messageDiv.appendChild(wrapperDiv);

  const typingIndicator = document.getElementById('typingIndicator');
  if (typingIndicator && typingIndicator.nextSibling) {
    messagesContainer.insertBefore(messageDiv, typingIndicator);
  } else {
    messagesContainer.appendChild(messageDiv);
  }

  requestAnimationFrame(() => {
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
  });
}

function showTyping() {
  const el = document.getElementById('typingIndicator');
  const messagesContainer = document.getElementById('chatMessages');
  if (!el || !messagesContainer) return;
  el.classList.add('show');
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function hideTyping() {
  const el = document.getElementById('typingIndicator');
  if (!el) return;
  el.classList.remove('show');
}

async function sendMessage() {
  const input = document.getElementById('messageInput');
  const sendButton = document.getElementById('sendButton');
  const container = document.getElementById('chatContainer');
  if (!input || !sendButton || !container) return;

  const message = input.value.trim();
  if (!message) return;

  input.disabled = true;
  sendButton.disabled = true;

  addMessage(message, true);
  conversationHistory.push({ role: 'user', content: message });

  input.value = '';
  autoResize(input);

  showTyping();

  try {
    const apiUrl = container.dataset.apiUrl;
    const resp = await fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-CSRFToken': window.csrfToken || (document.querySelector('[name=csrfmiddlewaretoken]')?.value || '') },
      body: JSON.stringify({ message, conversation_history: conversationHistory })
    });
    const data = await resp.json();

    hideTyping();

    if (data.success) {
      const html = data.response_html || '';
      const fallback = data.response || '';
      addMessage(html || fallback, false, Boolean(html));
      conversationHistory.push({ role: 'assistant', content: data.response });
    } else {
      addMessage('Desculpe, ocorreu um erro: ' + (data.error || 'Tente novamente.'), false);
    }
  } catch (e) {
    hideTyping();
    addMessage('Erro de conexão. Verifique sua internet e tente novamente.', false);
  } finally {
    input.disabled = false;
    sendButton.disabled = false;
    input.focus();
  }
}

// Init
document.addEventListener('DOMContentLoaded', () => {
  const input = document.getElementById('messageInput');
  const sendButton = document.getElementById('sendButton');
  const suggestions = document.querySelectorAll('.js-suggestion');

  if (input) {
    input.addEventListener('input', () => autoResize(input));
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
      }
    });
    input.focus();
  }
  if (sendButton) {
    sendButton.addEventListener('click', sendMessage);
  }
  suggestions.forEach(el => el.addEventListener('click', () => {
    if (!input) return;
    input.value = el.dataset.suggestion || '';
    sendMessage();
  }));

  const viewport = document.querySelector('meta[name=viewport]');
  if (!viewport) {
    const meta = document.createElement('meta');
    meta.name = 'viewport';
    meta.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no';
    document.head.appendChild(meta);
  }

  window.addEventListener('resize', () => {
    const chatMessages = document.getElementById('chatMessages');
    if (chatMessages) {
      setTimeout(() => {
        chatMessages.scrollTop = chatMessages.scrollHeight;
      }, 100);
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      input?.blur();
    }
  });
});
