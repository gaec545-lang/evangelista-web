/**
 * Diagnóstico Ejecutivo — Evangelista & Co.
 * Chatbot de scoping: evalúa perfil C-level, NO revela precios.
 * Modal HTML esperado en el DOM con IDs: diagnostico-modal, chat-messages, user-input, send-btn
 */
(function () {
    'use strict';

    // ── Estado ─────────────────────────────────────────────────────────────────
    let chatState = {
        step: 'welcome',
        userData: {},
        messages: []
    };

    // ── Abrir / cerrar modal ───────────────────────────────────────────────────
    function openDiagnostico() {
        const modal = document.getElementById('diagnostico-modal');
        if (!modal) return;
        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';
        if (chatState.messages.length === 0) initChat();
        setTimeout(function () {
            const input = document.getElementById('user-input');
            if (input) input.focus();
        }, 300);
    }

    function closeDiagnostico() {
        const modal = document.getElementById('diagnostico-modal');
        if (!modal) return;
        modal.style.display = 'none';
        document.body.style.overflow = '';
    }

    function resetChat() {
        chatState = { step: 'welcome', userData: {}, messages: [] };
        const log = document.getElementById('chat-messages');
        if (log) log.innerHTML = '';
    }

    // ── Mensajes ───────────────────────────────────────────────────────────────
    function addMessage(sender, text) {
        const log = document.getElementById('chat-messages');
        if (!log) return;

        const wrap = document.createElement('div');
        wrap.className = 'chat-msg chat-msg-' + sender;

        const bubble = document.createElement('div');
        bubble.className = sender === 'bot' ? 'chat-bubble-bot' : 'chat-bubble-user';

        if (sender === 'bot') {
            // Typewriter para el bot
            log.appendChild(wrap);
            wrap.appendChild(bubble);
            typeWriter(bubble, text);
        } else {
            bubble.textContent = text;
            wrap.appendChild(bubble);
            log.appendChild(wrap);
        }

        log.scrollTop = log.scrollHeight;
        chatState.messages.push({ sender, text });
    }

    function typeWriter(element, text) {
        let i = 0;
        const delay = Math.min(Math.max(text.length * 3, 600), 1800);
        element.textContent = '';

        setTimeout(function type() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                const log = document.getElementById('chat-messages');
                if (log) log.scrollTop = log.scrollHeight;
                let next = 22 + (Math.random() * 12 - 6);
                if (text.charAt(i - 1) === '.') next += 300;
                else if (text.charAt(i - 1) === ',') next += 100;
                setTimeout(type, next);
            }
        }, delay);
    }

    // ── Init ───────────────────────────────────────────────────────────────────
    function initChat() {
        resetChat();
        addMessage('bot',
            'Bienvenido. Soy el Socio Digital de Evangelista & Co.\n\n' +
            'Nadie busca una firma de arquitectura de datos cuando todo funciona. ' +
            'Generalmente llegan cuando descubren que una decisión estratégica se basó en datos que resultaron estar equivocados.\n\n' +
            '¿Qué decisión reciente le hizo dudar de la confiabilidad de sus datos?'
        );
    }

    // ── Lógica de scoping ──────────────────────────────────────────────────────
    function processInput(input) {
        input = input.trim();
        if (!input) return;

        addMessage('user', input);

        const input_lower = document.getElementById('user-input');
        if (input_lower) input_lower.value = '';

        setTimeout(function () { handleStep(input); }, 900);
    }

    function handleStep(input) {
        switch (chatState.step) {

            case 'welcome':
                chatState.userData.problema = input;
                chatState.step = 'facturacion';
                addMessage('bot',
                    'Entiendo. Para evaluar si podemos ayudar, necesito contexto.\n\n' +
                    '¿Cuál es la facturación anual aproximada de su empresa?\n\n' +
                    'a) Menos de $50M MXN\n' +
                    'b) $50M — $200M MXN\n' +
                    'c) Más de $200M MXN'
                );
                break;

            case 'facturacion':
                chatState.userData.facturacion = input;
                chatState.step = 'cargo';
                addMessage('bot',
                    '¿Qué cargo ocupa usted?\n\n' +
                    'a) Director General / CEO\n' +
                    'b) CFO / Director Financiero\n' +
                    'c) COO / Director de Operaciones\n' +
                    'd) Otro'
                );
                break;

            case 'cargo':
                chatState.userData.cargo = input;
                if (califica()) {
                    chatState.step = 'servicio';
                    addMessage('bot',
                        'Su perfil califica para nuestro servicio.\n\n' +
                        'Evangelista & Co. opera con tres intervenciones secuenciales:\n\n' +
                        'FOUNDATION — Auditoría forense de datos operativos. Identificamos dónde sus datos le están mintiendo y cuantificamos el costo anual.\n\n' +
                        'ARCHITECTURE — Infraestructura de inteligencia para decisiones de alto impacto. Success fee solo si hay resultados comprobables.\n\n' +
                        'SENTINEL — Plataforma SaaS con simulación Monte Carlo. 10,000 escenarios por cada decisión estratégica.\n\n' +
                        '¿Cuál de estas intervenciones describe mejor su necesidad?\n\n' +
                        'a) Foundation — Necesito saber qué datos son confiables\n' +
                        'b) Architecture — Necesito certeza para decisiones de alto impacto\n' +
                        'c) Sentinel — Necesito monitoreo continuo\n' +
                        'd) No estoy seguro, necesito asesoría'
                    );
                } else {
                    chatState.step = 'no_califica';
                    addMessage('bot',
                        'Gracias por su interés.\n\n' +
                        'Actualmente Evangelista & Co. enfoca sus recursos en empresas con facturación >$50M MXN y equipos directivos de nivel C.\n\n' +
                        'Si su perfil cambia, estaremos disponibles. Puede explorar nuestra metodología en evangelistaco.com/metodologia.html'
                    );
                }
                break;

            case 'servicio':
                chatState.userData.servicio = input;
                chatState.step = 'contacto';
                addMessage('bot',
                    'Perfecto. El siguiente paso es una sesión de 45 minutos con un Socio Senior para analizar su caso específico.\n\n' +
                    'Por favor proporcione:\n' +
                    '— Nombre completo\n' +
                    '— Email corporativo\n' +
                    '— Teléfono\n' +
                    '— Empresa\n\n' +
                    '(Puede escribirlos en un solo mensaje separados por comas)'
                );
                break;

            case 'contacto':
                chatState.userData.contacto = input;
                chatState.step = 'fin';
                enviarContacto(chatState.userData);
                addMessage('bot',
                    'Hemos recibido su información.\n\n' +
                    'Un miembro del equipo Evangelista & Co. lo contactará en las próximas 24 horas para coordinar la sesión de diagnóstico.\n\n' +
                    'Gracias por su interés.'
                );
                break;

            default:
                break;
        }
    }

    function califica() {
        const f = chatState.userData.facturacion.toLowerCase();
        const c = chatState.userData.cargo.toLowerCase();

        const facturacionOk = /[bc]|50|200|más/.test(f);
        const cargoOk = /[abc]|director|ceo|cfo|coo|general|financier/.test(c);

        return facturacionOk && cargoOk;
    }

    function enviarContacto(data) {
        // Placeholder: integrar con webhook / CRM
        console.log('[Evangelista & Co.] Nuevo lead:', data);
        /*
        fetch('https://hook.make.com/tu-webhook', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        */
    }

    // ── Event listeners ────────────────────────────────────────────────────────
    function bindEvents() {
        const sendBtn = document.getElementById('send-btn');
        const input = document.getElementById('user-input');
        const modal = document.getElementById('diagnostico-modal');

        if (sendBtn) {
            sendBtn.addEventListener('click', function () {
                const inp = document.getElementById('user-input');
                if (inp) processInput(inp.value);
            });
        }

        if (input) {
            input.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') processInput(input.value);
            });
        }

        // Cerrar con Escape
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && modal && modal.style.display === 'flex') {
                closeDiagnostico();
            }
        });

        // Cerrar al hacer click en el overlay (fuera del panel)
        if (modal) {
            modal.addEventListener('click', function (e) {
                if (e.target === modal) closeDiagnostico();
            });
        }
    }

    // ── API pública ────────────────────────────────────────────────────────────
    window.openDiagnostico = openDiagnostico;
    window.closeDiagnostico = closeDiagnostico;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', bindEvents);
    } else {
        bindEvents();
    }
})();
