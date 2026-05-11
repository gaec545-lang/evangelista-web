# Micro-Interactions & Subtle Animations

Creating premium feel through subtle, purposeful animations that enhance UX without distraction.

## When to Use This Skill

- Adding polish to corporate sites
- Creating smooth transitions between states
- Providing visual feedback for user actions
- Enhancing perceived performance

## Core Principles

### 1. Subtle, Not Showy

Animations should whisper elegance, not scream for attention.

**Good:** Fade-in opacity from 0.8 to 1 over 0.4s
**Bad:** Bouncing elements, spinning icons, pulsing buttons

### 2. Purposeful, Not Decorative

Every animation should serve a UX purpose:
- Provide feedback (hover states)
- Guide attention (scroll reveals)
- Indicate state change (active/inactive)
- Improve perceived performance (skeleton screens)

### 3. Consistent Timing

Use a timing scale for consistency:
```css
:root {
    --timing-instant: 150ms;
    --timing-quick: 250ms;
    --timing-normal: 350ms;
    --timing-slow: 500ms;
    --timing-slowest: 750ms;
}
```

### 4. Easing Functions
```css
:root {
    --ease-in: cubic-bezier(0.4, 0, 1, 1);
    --ease-out: cubic-bezier(0, 0, 0.2, 1);
    --ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
    --ease-smooth: cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
```

## Essential Micro-Interactions

### 1. Hover States

**Button hover:**
```css
.btn-primary {
    background: var(--accent-gold);
    transform: translateY(0);
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transition: all var(--timing-quick) var(--ease-out);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(212,175,55,0.3);
}

.btn-primary:active {
    transform: translateY(0);
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
}
```

**Link hover:**
```css
.nav-link {
    position: relative;
    color: var(--text-secondary);
    transition: color var(--timing-quick);
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--accent-gold);
    transition: width var(--timing-normal) var(--ease-out);
}

.nav-link:hover {
    color: var(--text-primary);
}

.nav-link:hover::after {
    width: 100%;
}
```

**Card hover:**
```css
.card {
    transition: transform var(--timing-normal) var(--ease-out);
}

.card:hover {
    transform: translateY(-8px);
}
```

### 2. Scroll-Triggered Animations

**Fade in on scroll:**
```css
.fade-in {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity var(--timing-slow) var(--ease-out),
                transform var(--timing-slow) var(--ease-out);
}

.fade-in.visible {
    opacity: 1;
    transform: translateY(0);
}
```

**JavaScript trigger:**
```javascript
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.querySelectorAll('.fade-in').forEach(el => {
    observer.observe(el);
});
```

**Stagger children:**
```css
.stagger-item {
    opacity: 0;
    transform: translateY(30px);
    transition: all var(--timing-slow) var(--ease-out);
}

.stagger-item:nth-child(1) { transition-delay: 0ms; }
.stagger-item:nth-child(2) { transition-delay: 100ms; }
.stagger-item:nth-child(3) { transition-delay: 200ms; }
.stagger-item:nth-child(4) { transition-delay: 300ms; }

.stagger-item.visible {
    opacity: 1;
    transform: translateY(0);
}
```

### 3. Number Counter Animation

For stats/results sections:
```javascript
function animateValue(element, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        const value = Math.floor(progress * (end - start) + start);
        element.textContent = value.toLocaleString();
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

// Usage
const statElement = document.querySelector('.stat-number');
const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
        animateValue(statElement, 0, 2300000, 2000); // $2.3M
        observer.disconnect();
    }
});
observer.observe(statElement);
```

### 4. Loading States

**Skeleton screen:**
```css
.skeleton {
    background: linear-gradient(
        90deg,
        var(--bg-tertiary) 0%,
        var(--bg-secondary) 50%,
        var(--bg-tertiary) 100%
    );
    background-size: 200% 100%;
    animation: skeleton-loading 1.5s ease-in-out infinite;
}

@keyframes skeleton-loading {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
```

**Spinner (minimal):**
```css
.spinner {
    width: 40px;
    height: 40px;
    border: 3px solid var(--bg-tertiary);
    border-top-color: var(--accent-gold);
    border-radius: 50%;
    animation: spinner-rotate 0.8s linear infinite;
}

@keyframes spinner-rotate {
    to { transform: rotate(360deg); }
}
```

### 5. Parallax Scrolling (Subtle)

**Background parallax:**
```css
.parallax-section {
    background-attachment: fixed;
    background-position: center;
    background-size: cover;
}
```

**Element parallax (JavaScript):**
```javascript
window.addEventListener('scroll', () => {
    const scrolled = window.pageYOffset;
    const parallaxElements = document.querySelectorAll('.parallax-element');
    
    parallaxElements.forEach(el => {
        const speed = el.dataset.speed || 0.5;
        el.style.transform = `translateY(${scrolled * speed}px)`;
    });
});
```

### 6. Modal/Overlay Animations

**Fade + scale:**
```css
.modal {
    opacity: 0;
    transform: scale(0.95);
    transition: opacity var(--timing-normal),
                transform var(--timing-normal);
    pointer-events: none;
}

.modal.active {
    opacity: 1;
    transform: scale(1);
    pointer-events: auto;
}

.modal-backdrop {
    opacity: 0;
    transition: opacity var(--timing-normal);
}

.modal-backdrop.active {
    opacity: 1;
}
```

### 7. Accordion/Collapse
```css
.accordion-content {
    max-height: 0;
    overflow: hidden;
    transition: max-height var(--timing-slow) var(--ease-out);
}

.accordion-content.open {
    max-height: 1000px; /* Larger than content */
}
```

### 8. Form Input States
```css
.input-field {
    border: 2px solid var(--bg-tertiary);
    transition: border-color var(--timing-quick);
}

.input-field:focus {
    border-color: var(--accent-gold);
    outline: none;
}

.input-label {
    transform: translateY(0);
    font-size: 1rem;
    transition: all var(--timing-quick);
}

.input-field:focus + .input-label,
.input-field:not(:placeholder-shown) + .input-label {
    transform: translateY(-24px);
    font-size: 0.75rem;
    color: var(--accent-gold);
}
```

## Advanced Techniques

### 1. Page Transitions
```css
/* Fade out on navigation */
body {
    transition: opacity var(--timing-slow);
}

body.page-exit {
    opacity: 0;
}
```

### 2. Image Reveal on Load
```css
.image-wrapper {
    position: relative;
    overflow: hidden;
}

.image-wrapper::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: var(--accent-gold);
    transform: translateX(-100%);
    animation: image-reveal 1s var(--ease-out) forwards;
}

@keyframes image-reveal {
    0% { transform: translateX(-100%); }
    50% { transform: translateX(0); }
    100% { transform: translateX(100%); }
}
```

### 3. Text Split Reveal
```javascript
// Split text into spans
function splitText(element) {
    const text = element.textContent;
    element.innerHTML = '';
    text.split('').forEach((char, i) => {
        const span = document.createElement('span');
        span.textContent = char === ' ' ? '\u00A0' : char;
        span.style.animationDelay = `${i * 30}ms`;
        span.classList.add('char');
        element.appendChild(span);
    });
}

// CSS
.char {
    opacity: 0;
    animation: char-fade-in 0.5s forwards;
}

@keyframes char-fade-in {
    to { opacity: 1; }
}
```

## Performance Considerations

### 1. Use Transform & Opacity

These properties don't trigger reflow:
```css
/* Good - GPU accelerated */
.element {
    transform: translateY(10px);
    opacity: 0.5;
}

/* Bad - triggers reflow */
.element {
    top: 10px;
    height: 200px;
}
```

### 2. Will-Change Hint

For complex animations:
```css
.animated-element {
    will-change: transform, opacity;
}

/* Remove after animation */
.animated-element.animation-complete {
    will-change: auto;
}
```

### 3. Reduce Motion for Accessibility
```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}
```

## Common Mistakes to Avoid

❌ **Too fast** - Animations under 200ms feel jarring
✅ **Sweet spot** - 250-500ms for most interactions

❌ **Too many simultaneous** - Overwhelming
✅ **Stagger/sequence** - One at a time or staggered

❌ **Bounce/elastic** - Feels unprofessional
✅ **Smooth ease-out** - Sophisticated

❌ **Infinite animations** - Distracting
✅ **Play once** - User-triggered only

## Quality Checklist

- [ ] All animations under 750ms
- [ ] Consistent easing functions used
- [ ] Hover states on all interactive elements
- [ ] Scroll-triggered reveals for content
- [ ] Number counters for stats
- [ ] Loading states for async content
- [ ] Reduced motion support
- [ ] GPU-accelerated properties (transform/opacity)
- [ ] No bouncing or spinning elements
- [ ] Animations serve UX purpose