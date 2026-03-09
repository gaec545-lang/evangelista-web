/**
 * Evangelista & Co. — Diagnóstico Ejecutivo
 * Chatbot de scoping por pasos. No menciona precios.
 * Modal: #diagnostico-modal (.modal) > .modal-content > #chat-container
 */
(function () {
    'use strict';

    // ── Estado ─────────────────────────────────────────────────────────────────
    var currentStep = 0;
    var userData = {};
    var waitingForInput = false;

    // ── Flujo ──────────────────────────────────────────────────────────────────
    var flow = [
        // Step 0 — Saludo
        {
            type: 'greeting',
            message: 'Hola. Soy el Socio Digital de Evangelista & Co.\n\nEn 90 minutos le daré claridad sobre qué datos posee, qué le falta, y cómo convertirlos en ventaja competitiva real.\n\n¿Listo para comenzar?',
            options: ['Sí, comenzar', 'Necesito más información']
        },
        // Step 1 — Contexto del problema
        {
            type: 'open',
            message: 'Cuénteme sobre una decisión reciente que haya tomado donde dudó si tenía los datos correctos.',
            validate: function (t) { return t.trim().length > 10; },
            validationError: 'Por favor, proporcione más detalle. Esto nos ayuda a personalizar su diagnóstico.'
        },
        // Step 2 — Facturación
        {
            type: 'choice',
            key: 'tier',
            message: '¿Cuál es la facturación anual aproximada de su empresa?',
            options: [
                { label: 'Menos de $50M MXN', value: 'tier1' },
                { label: '$50M – $200M MXN',  value: 'tier2' },
                { label: 'Más de $200M MXN',  value: 'tier3' }
            ]
        },
        // Step 3 — Rol
        {
            type: 'choice',
            key: 'role',
            message: '¿Cuál es su rol en la organización?',
            options: [
                { label: 'Director General / CEO',          value: 'ceo' },
                { label: 'Director Financiero / CFO',       value: 'cfo' },
                { label: 'Director de Operaciones / COO',   value: 'coo' },
                { label: 'Otro cargo',                       value: 'other' }
            ]
        },
        // Step 4 — Calificación + servicio
        {
            type: 'qualify'
        },
        // Step 5 — Datos de contacto
        {
            type: 'form',
            message: 'Para agendar su diagnóstico ejecutivo, necesito los siguientes datos.'
        },
        // Step 6 — Cierre
        {
            type: 'closing',
            message: 'Perfecto. Recibirá confirmación en las próximas horas.\n\nNuestro equipo se pondrá en contacto antes de 24 horas para coordinar su sesión.\n\n¿Hay algo más en lo que pueda orientarle?'
        }
    ];

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
        bubble.textContent = text;

        wrap.appendChild(bubble);
        container.appendChild(wrap);
        scrollToBottom();
    }

    function appendOptions(options, onSelect) {
        var container = getChatContainer();
        if (!container) return;

        var wrap = document.createElement('div');
        wrap.className = 'chat-options';

        options.forEach(function (opt) {
            var btn = document.createElement('button');
            btn.className = 'chat-option-btn';
            btn.textContent = typeof opt === 'string' ? opt : opt.label;
            btn.addEventListener('click', function () {
                // Disable all options after selection
                wrap.querySelectorAll('.chat-option-btn').forEach(function (b) {
                    b.disabled = true;
                    b.style.opacity = '0.4';
                });
                var value = typeof opt === 'string' ? opt : opt.value;
                var label = typeof opt === 'string' ? opt : opt.label;
                appendMessage(label, 'user');
                onSelect(value, label);
            });
            wrap.appendChild(btn);
        });

        container.appendChild(wrap);
        scrollToBottom();
    }

    function appendLinks(links) {
        var container = getChatContainer();
        if (!container) return;

        var wrap = document.createElement('div');
        wrap.className = 'chat-links';

        links.forEach(function (link) {
            var a = document.createElement('a');
            a.className = 'chat-link-btn';
            a.textContent = link.text;
            a.href = link.url;
            wrap.appendChild(a);
        });

        container.appendChild(wrap);
        scrollToBottom();
    }

    function appendContactForm() {
        var container = getChatContainer();
        if (!container) return;

        var form = document.createElement('div');
        form.className = 'chat-form';

        var fields = [
            { name: 'nombre',   placeholder: 'Nombre completo' },
            { name: 'email',    placeholder: 'Email corporativo',  type: 'email' },
            { name: 'telefono', placeholder: 'Teléfono',           type: 'tel' },
            { name: 'empresa',  placeholder: 'Empresa' }
        ];

        fields.forEach(function (f) {
            var input = document.createElement('input');
            input.name = f.name;
            input.placeholder = f.placeholder;
            input.type = f.type || 'text';
            form.appendChild(input);
        });

        var btn = document.createElement('button');
        btn.className = 'chat-form-submit';
        btn.textContent = 'Enviar datos →';
        btn.addEventListener('click', function () {
            var nombre   = form.querySelector('[name=nombre]').value.trim();
            var email    = form.querySelector('[name=email]').value.trim();
            var telefono = form.querySelector('[name=telefono]').value.trim();
            var empresa  = form.querySelector('[name=empresa]').value.trim();

            if (!nombre || !email || !empresa) {
                var err = form.querySelector('.form-error');
                if (!err) {
                    err = document.createElement('p');
                    err.className = 'form-error';
                    err.style.cssText = 'color:#d4af37;font-size:0.78rem;margin-top:4px;';
                    form.appendChild(err);
                }
                err.textContent = 'Por favor complete nombre, email y empresa.';
                return;
            }

            userData.contacto = { nombre: nombre, email: email, telefono: telefono, empresa: empresa };
            btn.disabled = true;
            form.style.opacity = '0.5';

            appendMessage(nombre + ' · ' + email + ' · ' + empresa, 'user');
            enviarDatos(userData);
            currentStep = 6;
            displayStep();
        });

        form.appendChild(btn);
        container.appendChild(form);
        scrollToBottom();
    }

    // ── Lógica de pasos ────────────────────────────────────────────────────────
    function displayStep() {
        var step = flow[currentStep];
        if (!step) return;

        if (step.type === 'greeting') {
            appendMessage(step.message, 'assistant');
            appendOptions(step.options, function (val) {
                userData.greeting = val;
                if (val === 'Necesito más información') {
                    appendMessage('Con gusto. Evangelista & Co. ayuda a Directores Generales, CFOs y COOs a tomar decisiones con certeza estadística, usando metodología forense de datos ALCOA+ y simulación Monte Carlo.\n\nUna vez que esté listo para explorar si podemos ayudarle, podemos continuar.', 'assistant');
                    appendOptions(['Continuar diagnóstico'], function () {
                        currentStep = 1;
                        displayStep();
                    });
                } else {
                    currentStep = 1;
                    displayStep();
                }
            });

        } else if (step.type === 'open') {
            appendMessage(step.message, 'assistant');
            waitingForInput = true;
            enableInput(function (text) {
                if (step.validate && !step.validate(text)) {
                    appendMessage(step.validationError || 'Por favor proporcione más detalle.', 'assistant');
                    return false;
                }
                userData['step' + currentStep] = text;
                currentStep++;
                displayStep();
                return true;
            });

        } else if (step.type === 'choice') {
            appendMessage(step.message, 'assistant');
            appendOptions(step.options, function (value) {
                userData[step.key] = value;
                currentStep++;
                displayStep();
            });

        } else if (step.type === 'qualify') {
            var qualifies = userData.tier !== 'tier1' &&
                            (userData.role === 'ceo' || userData.role === 'cfo' || userData.role === 'coo');

            if (qualifies) {
                appendMessage('Su perfil califica para nuestro servicio.\n\nEvangelista & Co. opera con tres intervenciones:\n\nFOUNDATION — Auditoría forense de datos (4-6 semanas)\nARCHITECTURE — Infraestructura de inteligencia (8-12 semanas)\nSENTINEL — Vigilancia Monte Carlo 24/7 (SaaS)\n\n¿Cuál describe mejor su necesidad?', 'assistant');
                appendOptions(['Foundation', 'Architecture', 'Sentinel', 'Las tres / necesito asesoría'], function (val) {
                    userData.servicio = val;
                    currentStep = 5;
                    displayStep();
                });
            } else {
                appendMessage('Gracias por su interés.\n\nPor el momento, Evangelista & Co. enfoca sus recursos en empresas con facturación superior a $50M MXN y equipos directivos C-level.\n\nLe invito a conocer más sobre nuestra metodología y sectores de impacto.', 'assistant');
                appendLinks([
                    { text: 'Ver Metodología →', url: 'metodologia.html' },
                    { text: 'Ver Sectores →',     url: 'sectores.html' }
                ]);
            }

        } else if (step.type === 'form') {
            appendMessage(step.message, 'assistant');
            appendContactForm();

        } else if (step.type === 'closing') {
            appendMessage(step.message, 'assistant');
        }
    }

    // ── Input libre ────────────────────────────────────────────────────────────
    var pendingInputCallback = null;

    function enableInput(callback) {
        pendingInputCallback = callback;
        var area = document.getElementById('chat-input-area');
        if (area) area.style.display = 'flex';
        var input = document.getElementById('chat-free-input');
        if (input) {
            input.value = '';
            setTimeout(function () { input.focus(); }, 200);
        }
    }

    function disableInput() {
        pendingInputCallback = null;
        var area = document.getElementById('chat-input-area');
        if (area) area.style.display = 'none';
    }

    function handleFreeInputSend() {
        if (!pendingInputCallback) return;
        var input = document.getElementById('chat-free-input');
        if (!input) return;
        var text = input.value.trim();
        if (!text) return;

        var accepted = pendingInputCallback(text);
        if (accepted !== false) {
            appendMessage(text, 'user');
            input.value = '';
            disableInput();
        } else {
            // validation failed — keep input open
        }
    }

    // ── Enviar datos ───────────────────────────────────────────────────────────
    function enviarDatos(data) {
        console.log('[Evangelista & Co.] Lead calificado:', data);
        /*
        fetch('https://hook.make.com/TU_WEBHOOK', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        */
    }

    // ── Modal controls ─────────────────────────────────────────────────────────
    function openDiagnostico() {
        var modal = document.getElementById('diagnostico-modal');
        if (!modal) return;

        modal.style.display = 'flex';
        document.body.style.overflow = 'hidden';

        // Micro-delay to trigger CSS transition
        requestAnimationFrame(function () {
            requestAnimationFrame(function () {
                modal.classList.add('active');
            });
        });

        // Reset and start
        currentStep = 0;
        userData = {};
        var container = document.getElementById('chat-container');
        if (container) container.innerHTML = '';
        disableInput();

        setTimeout(displayStep, 300);
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

        // Close on backdrop click
        if (modal) {
            modal.addEventListener('click', function (e) {
                if (e.target === modal) closeDiagnostico();
            });
        }

        // Free input send button
        var sendBtn = document.getElementById('chat-send-free');
        if (sendBtn) {
            sendBtn.addEventListener('click', handleFreeInputSend);
        }

        // Enter key
        var freeInput = document.getElementById('chat-free-input');
        if (freeInput) {
            freeInput.addEventListener('keypress', function (e) {
                if (e.key === 'Enter') handleFreeInputSend();
            });
        }

        // Escape key
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
