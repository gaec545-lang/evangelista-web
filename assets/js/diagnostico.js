/**
 * Evangelista & Co. — Adria · Asesor Estratégico
 * Calls FastAPI backend at Railway — never exposes keys.
 * Modal: #diagnostico-modal > .modal-content > #chat-container
 */
(function () {
    'use strict';

    var BACKEND_URL = 'https://evangelista-web-production.up.railway.app/chat';
    var CALENDLY_URL = 'https://calendly.com/evangelistaco/diagnostico-ejecutivo';

    var OPENING_MESSAGE = 'Hola. Soy el Socio Digital de Evangelista\u00a0&\u00a0Co.\n\nEn mi experiencia, nadie busca arquitectura de inteligencia cuando todo va bien.\n\n¿Qué está pasando en su operación que le hizo pensar en buscarnos hoy?';

    // ── Estado ─────────────────────────────────────────────────────────────────
    var history  = [];   // [{role, content}]
    var leadData = {};   // acumulado por backend silent_audit
    var busy     = false;

    // ── DOM helpers ────────────────────────────────────────────────────────────
    function getChatContainer() {
        return document.getElementById('chat-container');
    }

    function scrollToBottom() {
        var el = getChatContainer();
        if (el) el.scrollTop = el.scrollHeight;
    }

    function appendMessage(text, sender) {
        var container = getChatContainer();
        if (!container) return;

        var wrap = document.createElement('div');
        wrap.className = 'chat-message ' + sender;

        var bubble = document.createElement('div');
        bubble.className = 'bubble';
        // Preserve line breaks
        bubble.style.whiteSpace = 'pre-line';
        bubble.textContent = text;

        wrap.appendChild(bubble);
        container.appendChild(wrap);
        scrollToBottom();
        return wrap;
    }

    // ── Typing indicator ───────────────────────────────────────────────────────
    var typingEl = null;

    function showTyping() {
        var container = getChatContainer();
        if (!container || typingEl) return;

        var wrap = document.createElement('div');
        wrap.className = 'chat-message assistant';

        var indicator = document.createElement('div');
        indicator.className = 'typing-indicator';
        indicator.innerHTML = '<span></span><span></span><span></span>';

        wrap.appendChild(indicator);
        container.appendChild(wrap);
        typingEl = wrap;
        scrollToBottom();
    }

    function hideTyping() {
        if (typingEl) {
            typingEl.parentNode && typingEl.parentNode.removeChild(typingEl);
            typingEl = null;
        }
    }

    // ── Calendly CTA ───────────────────────────────────────────────────────────
    function appendCalendlyCTA() {
        var container = getChatContainer();
        if (!container) return;

        var cta = document.createElement('div');
        cta.className = 'calendly-cta';

        var p = document.createElement('p');
        p.textContent = 'Basado en lo que me comparte, creo que merece una conversación directa con nuestro equipo.';

        var a = document.createElement('a');
        a.href = CALENDLY_URL;
        a.target = '_blank';
        a.rel = 'noopener noreferrer';
        a.className = 'calendly-btn';
        a.textContent = 'Agendar Diagnóstico Ejecutivo \u2192';

        cta.appendChild(p);
        cta.appendChild(a);
        container.appendChild(cta);
        scrollToBottom();
    }

    // ── Input controls ─────────────────────────────────────────────────────────
    function enableInput() {
        var area = document.getElementById('chat-input-area');
        if (area) area.style.display = 'flex';
        var input = document.getElementById('chat-free-input');
        if (input) {
            input.disabled = false;
            setTimeout(function () { input.focus(); }, 150);
        }
        var btn = document.getElementById('chat-send-free');
        if (btn) btn.disabled = false;
    }

    function disableInput() {
        var input = document.getElementById('chat-free-input');
        if (input) input.disabled = true;
        var btn = document.getElementById('chat-send-free');
        if (btn) btn.disabled = true;
    }

    // ── Backend call ───────────────────────────────────────────────────────────
    function sendToBackend(userMessage) {
        if (busy) return;
        busy = true;
        disableInput();

        appendMessage(userMessage, 'user');
        history.push({ role: 'user', content: userMessage });

        // Clear input field
        var inputEl = document.getElementById('chat-free-input');
        if (inputEl) inputEl.value = '';

        showTyping();

        fetch(BACKEND_URL, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message:   userMessage,
                history:   history.slice(0, -1), // exclude the just-added message
                lead_data: leadData
            })
        })
        .then(function (res) {
            if (!res.ok) throw new Error('HTTP ' + res.status);
            return res.json();
        })
        .then(function (data) {
            hideTyping();

            var response = (data && data.response) ? data.response : null;

            if (response) {
                appendMessage(response, 'assistant');
                history.push({ role: 'assistant', content: response });
            }

            // Merge updated lead data
            if (data && data.updated_lead_data) {
                Object.assign(leadData, data.updated_lead_data);
            }

            // Check for Calendly unlock
            var action = data && data.silent_audit && data.silent_audit.action;
            if (action === 'UNLOCK_CALENDLY') {
                setTimeout(appendCalendlyCTA, 600);
            }

            busy = false;
            enableInput();
        })
        .catch(function (err) {
            hideTyping();
            console.error('[Adria] Backend error:', err);
            appendMessage(
                'En este momento tengo una dificultad técnica. Por favor escríbanos directamente a contacto@evangelistaco.com o intente de nuevo en un momento.',
                'assistant'
            );
            busy = false;
            enableInput();
        });
    }

    // ── Send handler ───────────────────────────────────────────────────────────
    function handleSend() {
        if (busy) return;
        var input = document.getElementById('chat-free-input');
        if (!input) return;
        var text = input.value.trim();
        if (!text) return;
        sendToBackend(text);
    }

    // ── Modal controls ─────────────────────────────────────────────────────────
    function openDiagnostico() {
        var modal = document.getElementById('diagnostico-modal');
        if (!modal) return;

        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';

        requestAnimationFrame(function () {
            requestAnimationFrame(function () {
                modal.classList.add('active');
            });
        });

        // Reset state
        history  = [];
        leadData = {};
        busy     = false;
        typingEl = null;

        var container = document.getElementById('chat-container');
        if (container) container.innerHTML = '';

        // Show input area from start
        var area = document.getElementById('chat-input-area');
        if (area) area.style.display = 'flex';
        var inputEl = document.getElementById('chat-free-input');
        if (inputEl) inputEl.value = '';
        disableInput();

        // Opening message with typing feel
        setTimeout(function () {
            showTyping();
            setTimeout(function () {
                hideTyping();
                appendMessage(OPENING_MESSAGE, 'assistant');
                history.push({ role: 'assistant', content: OPENING_MESSAGE });
                enableInput();
            }, 1200);
        }, 350);
    }

    function closeDiagnostico() {
        var modal = document.getElementById('diagnostico-modal');
        if (!modal) return;
        modal.classList.remove('active');
        document.body.style.overflow = '';
        setTimeout(function () {
            modal.style.display = 'none';
        }, 350);
    }

    // ── Init ───────────────────────────────────────────────────────────────────
    function bindEvents() {
        var modal = document.getElementById('diagnostico-modal');

        if (modal) {
            modal.addEventListener('click', function (e) {
                if (e.target === modal) closeDiagnostico();
            });
        }

        var sendBtn = document.getElementById('chat-send-free');
        if (sendBtn) {
            sendBtn.addEventListener('click', handleSend);
        }

        var freeInput = document.getElementById('chat-free-input');
        if (freeInput) {
            freeInput.addEventListener('keypress', function (e) {
                if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    handleSend();
                }
            });
        }

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && modal && modal.classList.contains('active')) {
                closeDiagnostico();
            }
        });
    }

    // ── Public API ─────────────────────────────────────────────────────────────
    window.openDiagnostico  = openDiagnostico;
    window.closeDiagnostico = closeDiagnostico;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', bindEvents);
    } else {
        bindEvents();
    }
})();
