/**
 * EVANGELISTA & CO. - VETTING GATE MODULE v1.0
 * Arquitectura: Revealing Module Pattern
 * Dependencias: GSAP (Global), Tailwind CSS
 */

const VettingGate = (() => {
    // --- ESTADO PRIVADO ---
    const CONFIG = {
        apiEndpoint: 'http://localhost:8002/chat', // Cambiaremos esto en producción
        typingSpeed: 30, // ms por caracter
    };

    let state = {
        isOpen: false,
        history: [], // Historial de conversación para el modelo
        isTyping: false,
        ipScore: 0.0 // Score de prioridad inicial
    };

    // --- SELECTORES DOM ---
    const dom = {
        modal: document.getElementById('vetting-modal'),
        triggerBtn: document.getElementById('btn-open-chat'),
        closeBtn: document.getElementById('btn-close-chat'),
        log: document.getElementById('chat-log'),
        input: document.getElementById('chat-input'),
        sendBtn: document.getElementById('btn-send-chat'),
        calendlyBar: document.getElementById('calendly-unlock')
    };

    // --- MÉTODOS PRIVADOS ---

    /// 1. Manejo de Interfaz (VERSIÓN REFORZADA)
    const toggleChat = (forceState = null) => {
        state.isOpen = forceState !== null ? forceState : !state.isOpen;
        
        if (state.isOpen) {
            // ABRIR CHAT
            // 1. Subir el modal
            gsap.to(dom.modal, { y: "0%", opacity: 1, duration: 0.5, ease: "power3.out" });
            
            // 2. ESCONDER EL BOTÓN (Critical Fix)
            gsap.to(dom.triggerBtn, { 
                y: "200%", // Lo bajamos más para asegurar que no estorbe
                opacity: 0, 
                duration: 0.3, 
                pointerEvents: "none" // Desactivamos su clic para que no moleste
            });
            
            dom.input.focus();
        } else {
            // CERRAR CHAT
            // 1. Bajar el modal
            gsap.to(dom.modal, { y: "120%", opacity: 0, duration: 0.4, ease: "power3.in" });
            
            // 2. RECUPERAR EL BOTÓN
            gsap.to(dom.triggerBtn, { 
                y: "0%", 
                opacity: 1, 
                duration: 0.3, 
                delay: 0.4, // Esperamos un poco a que baje el chat
                pointerEvents: "all" // Reactivamos el clic
            });
        }
    };

    // 2. Renderizado de Mensajes
    const appendMessage = (role, text, isSystem = false) => {
        const msgDiv = document.createElement('div');
        msgDiv.className = `flex flex-col gap-1 items-${role === 'user' ? 'end' : 'start'} opacity-0`;
        
        // Estilos condicionales según rol
        const bubbleClass = role === 'user' 
            ? 'bg-evBone text-evBlack rounded-tl-lg rounded-bl-lg rounded-br-lg' 
            : 'bg-evOlive/10 text-evBone/90 rounded-tr-lg rounded-br-lg rounded-bl-lg border-l-2 border-evOlive';

        const label = role === 'user' ? 'Usted' : 'Socio Digital';
        
        msgDiv.innerHTML = `
            <span class="text-[8px] text-evOlive/50 uppercase tracking-widest">${label}</span>
            <div class="${bubbleClass} p-3 text-xs leading-relaxed max-w-[90%] font-light shadow-sm">
                ${role === 'user' ? text : ''} </div>
        `;

        dom.log.appendChild(msgDiv);
        
        // Animación de entrada
        gsap.to(msgDiv, { opacity: 1, y: -5, duration: 0.3 });
        scrollToBottom();

        if (role === 'model') {
            typeWriterEffect(msgDiv.querySelector('div'), text);
        }
    };

    // 3. Efecto de Escritura (Realismo)
    const typeWriterEffect = (element, text) => {
        let i = 0;
        state.isTyping = true;
        element.innerHTML = ''; // Limpiar para escribir
        
        const interval = setInterval(() => {
            element.innerHTML += text.charAt(i);
            i++;
            scrollToBottom(); // Mantener scroll abajo mientras escribe

            if (i >= text.length) {
                clearInterval(interval);
                state.isTyping = false;
            }
        }, CONFIG.typingSpeed);
    };

    const scrollToBottom = () => {
        dom.log.scrollTop = dom.log.scrollHeight;
    };

    // 4. Lógica de Envío (CORE)
    const handleSend = async () => {
        const text = dom.input.value.trim();
        if (!text || state.isTyping) return;

        // Limpiar input y mostrar mensaje usuario
        dom.input.value = '';
        appendMessage('user', text);
        state.history.push({ role: "user", parts: [text] });

        // Indicador de "Pensando..."
        const loadingId = showLoading();

        try {
            // --- CONEXIÓN AL BACKEND ---
            const response = await fetch(CONFIG.apiEndpoint, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ 
                    message: text, 
                    history: state.history 
                })
            });

            if (!response.ok) throw new Error('Error en el servidor de IA');

            const data = await response.json();
            
            // Remover loading
            removeLoading(loadingId);

            // Mostrar respuesta IA
            appendMessage('model', data.response);
            state.history.push({ role: "model", parts: [data.response] });

            // --- AUDITOR SILENCIOSO ---
            // Si el backend detecta un lead de alto valor, desbloquea Calendly
            if (data.silent_audit && data.silent_audit.action === 'UNLOCK_CALENDLY') {
                unlockCalendly(data.silent_audit.score);
            }

        } catch (error) {
            removeLoading(loadingId);
            console.error('Falla en Vetting Gate:', error);
            // Fallback elegante (No mostrar error técnico)
            appendMessage('model', "Conexión inestable con el servidor seguro. Para garantizar la integridad del diagnóstico, por favor proceda directamente a nuestro canal prioritario: board@evangelista.co");
        }
    };

    // 5. Utilidades UI
    const showLoading = () => {
        const id = 'loader-' + Date.now();
        const loader = document.createElement('div');
        loader.id = id;
        loader.className = 'flex items-center gap-2 p-3 opacity-50';
        loader.innerHTML = `
            <div class="w-1.5 h-1.5 bg-evOlive rounded-full animate-bounce"></div>
            <div class="w-1.5 h-1.5 bg-evOlive rounded-full animate-bounce" style="animation-delay: 0.1s"></div>
            <div class="w-1.5 h-1.5 bg-evOlive rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
        `;
        dom.log.appendChild(loader);
        scrollToBottom();
        return id;
    };

    const removeLoading = (id) => {
        const el = document.getElementById(id);
        if (el) el.remove();
    };

    // 6. Desbloqueo de Calendly (The Goal)
    const unlockCalendly = (score) => {
        if (dom.calendlyBar.classList.contains('hidden')) {
            dom.calendlyBar.classList.remove('hidden');
            
            // Animación de celebración sutil
            gsap.from(dom.calendlyBar, { height: 0, opacity: 0, duration: 0.6, ease: "back.out" });
            
            // Inyectar enlace real
            dom.calendlyBar.onclick = () => {
                window.open('https://calendly.com/TU_LINK', '_blank');
            };
            
            console.log(`Lead Calificado (Score: ${score}). Agenda desbloqueada.`);
        }
    };

    // --- INICIALIZACIÓN ---
    const init = () => {
        if (!dom.modal) return; // Guard clause

        // Listeners
        dom.triggerBtn.addEventListener('click', () => toggleChat(true));
        dom.closeBtn.addEventListener('click', () => toggleChat(false));
        
        dom.sendBtn.addEventListener('click', handleSend);
        dom.input.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') handleSend();
        });

        // Debug Log
        console.log('Evangelista Vetting Gate v1.0: ONLINE');
    };

    // API Pública
    return {
        init: init
    };

})();

// Arrancar al cargar el DOM
document.addEventListener('DOMContentLoaded', VettingGate.init);