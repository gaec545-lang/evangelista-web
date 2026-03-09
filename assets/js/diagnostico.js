/**
 * Diagnóstico Ejecutivo — Evangelista & Co.
 * Chat widget auto-injected: FAB + modal
 * Backend: Railway + Gemini
 */
(function () {
    'use strict';

    const CONFIG = {
        apiEndpoint: 'https://evangelista-web-production.up.railway.app/chat',
        calendlyUrl: 'https://calendly.com/gaec545/30min'
    };

    let state = {
        isOpen: false,
        history: [],
        lead_data: {},
        isTyping: false,
        initialized: false
    };

    // ── DOM injection ──────────────────────────────────────────────────────────

    function injectDOM() {
        // FAB button
        const fab = document.createElement('button');
        fab.id = 'chat-fab';
        fab.className = 'chat-fab';
        fab.setAttribute('aria-label', 'Abrir Diagnóstico Ejecutivo');
        fab.innerHTML = `
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
            </svg>
            <span>Diagnóstico Ejecutivo</span>
        `;

        // Modal
        const modal = document.createElement('div');
        modal.id = 'chat-modal';
        modal.className = 'chat-modal';
        modal.setAttribute('role', 'dialog');
        modal.setAttribute('aria-modal', 'true');
        modal.setAttribute('aria-label', 'Diagnóstico Ejecutivo');
        modal.innerHTML = `
            <div class="chat-modal-header">
                <div class="chat-modal-title">
                    <div class="chat-modal-avatar">E</div>
                    <div>
                        <div style="font-weight:700;font-size:0.875rem;color:#ffffff;">Evangelista &amp; Co.</div>
                        <div style="font-size:0.7rem;color:#d4af37;text-transform:uppercase;letter-spacing:0.08em;">Diagnóstico Ejecutivo</div>
                    </div>
                </div>
                <button id="chat-close-btn" class="chat-close-btn" aria-label="Cerrar">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="18" y1="6" x2="6" y2="18"></line>
                        <line x1="6" y1="6" x2="18" y2="18"></line>
                    </svg>
                </button>
            </div>
            <div id="chat-log" class="chat-log">
                <div class="chat-bubble-bot">
                    Las decisiones estratégicas requieren certeza cuantificada. ¿Cuál es el reto de datos más crítico que enfrenta su organización hoy?
                </div>
            </div>
            <div class="chat-input-area">
                <input
                    id="chat-input"
                    class="chat-input-field"
                    type="text"
                    placeholder="Escriba su respuesta..."
                    autocomplete="off"
                    maxlength="500"
                />
                <button id="chat-send-btn" class="chat-send-btn" aria-label="Enviar">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="22" y1="2" x2="11" y2="13"></line>
                        <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                    </svg>
                </button>
            </div>
        `;

        document.body.appendChild(fab);
        document.body.appendChild(modal);
    }

    // ── Core functions ─────────────────────────────────────────────────────────

    function openChat() {
        state.isOpen = true;
        const modal = document.getElementById('chat-modal');
        const fab = document.getElementById('chat-fab');
        if (modal) modal.classList.add('open');
        if (fab) fab.style.display = 'none';
        const input = document.getElementById('chat-input');
        if (input) setTimeout(() => input.focus(), 300);
    }

    function closeChat() {
        state.isOpen = false;
        const modal = document.getElementById('chat-modal');
        const fab = document.getElementById('chat-fab');
        if (modal) modal.classList.remove('open');
        if (fab) fab.style.display = '';
    }

    function appendMessage(role, text) {
        if (!text) return;
        const log = document.getElementById('chat-log');
        if (!log) return;

        const bubble = document.createElement('div');
        bubble.className = role === 'user' ? 'chat-bubble-user' : 'chat-bubble-bot';

        if (role === 'user') {
            bubble.textContent = text;
            log.appendChild(bubble);
            log.scrollTop = log.scrollHeight;
        } else {
            log.appendChild(bubble);
            typeWriter(bubble, text, () => {
                log.scrollTop = log.scrollHeight;
            });
        }
        log.scrollTop = log.scrollHeight;
    }

    function typeWriter(element, text, onComplete) {
        let i = 0;
        state.isTyping = true;
        element.textContent = '';
        const delay = Math.min(Math.max(text.length * 4, 800), 2000);

        setTimeout(function type() {
            if (i < text.length) {
                const char = text.charAt(i);
                element.textContent += char;
                i++;
                const log = document.getElementById('chat-log');
                if (log) log.scrollTop = log.scrollHeight;
                let next = 25 + (Math.random() * 15 - 7);
                if (char === '.' || char === '?') next += 350;
                else if (char === ',') next += 120;
                setTimeout(type, next);
            } else {
                state.isTyping = false;
                if (onComplete) onComplete();
            }
        }, delay);
    }

    function showLoader() {
        const log = document.getElementById('chat-log');
        if (!log) return null;
        const loader = document.createElement('div');
        loader.className = 'chat-loader';
        loader.innerHTML = '<span></span><span></span><span></span>';
        log.appendChild(loader);
        log.scrollTop = log.scrollHeight;
        return loader;
    }

    function unlockCalendly() {
        const log = document.getElementById('chat-log');
        if (!log) return;
        const cta = document.createElement('div');
        cta.className = 'chat-calendly-unlock';
        cta.innerHTML = `
            <div class="chat-calendly-title">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                Protocolo Foundation Aprobado
            </div>
            <p>Se ha autorizado una ventana de 45 minutos en la agenda de la Dirección.</p>
            <button onclick="window.open('${CONFIG.calendlyUrl}','_blank')" class="btn-primary" style="width:100%;justify-content:center;font-size:0.75rem;">
                Reservar Sesión →
            </button>
        `;
        log.appendChild(cta);
        log.scrollTop = log.scrollHeight;
    }

    async function handleSend() {
        const input = document.getElementById('chat-input');
        if (!input) return;
        const text = input.value.trim();
        if (!text || state.isTyping) return;

        input.value = '';
        appendMessage('user', text);
        state.history.push({ role: 'user', parts: [text] });

        const loader = showLoader();

        try {
            const response = await fetch(CONFIG.apiEndpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: text,
                    history: state.history,
                    lead_data: state.lead_data
                })
            });

            if (loader && loader.parentNode) loader.remove();
            if (!response.ok) throw new Error('Server error ' + response.status);

            const data = await response.json();
            if (data.updated_lead_data) state.lead_data = data.updated_lead_data;

            if (data.response) {
                appendMessage('model', data.response);
                state.history.push({ role: 'model', parts: [data.response] });

                if (data.silent_audit && data.silent_audit.action === 'UNLOCK_CALENDLY') {
                    setTimeout(unlockCalendly, 500);
                }
            }
        } catch (err) {
            if (loader && loader.parentNode) loader.remove();
            appendMessage('model', 'Conexión interrumpida. Por favor verifique e intente de nuevo.');
            state.isTyping = false;
        }
    }

    // ── Init ───────────────────────────────────────────────────────────────────

    function init() {
        if (state.initialized) return;
        state.initialized = true;

        injectDOM();

        const fab = document.getElementById('chat-fab');
        const closeBtn = document.getElementById('chat-close-btn');
        const sendBtn = document.getElementById('chat-send-btn');
        const input = document.getElementById('chat-input');

        if (fab) fab.addEventListener('click', openChat);
        if (closeBtn) closeBtn.addEventListener('click', closeChat);
        if (sendBtn) sendBtn.addEventListener('click', handleSend);
        if (input) {
            input.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') handleSend();
            });
        }

        // Close on Escape
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && state.isOpen) closeChat();
        });
    }

    // Public API
    window.openDiagnostico = openChat;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
