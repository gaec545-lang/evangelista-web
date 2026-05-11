# Premium Corporate Typography

Typography that conveys authority, sophistication, and trustworthiness for C-level audiences.

## When to Use This Skill

- Designing corporate consulting websites
- Creating executive-facing interfaces
- Any B2B premium service positioning
- Professional services (finance, consulting, legal)

## Core Typography Principles

### 1. Serif for Authority, Sans for Clarity

**Serif (Headlines, Accents):**
- Conveys tradition, authority, permanence
- Best for: H1, H2, pull quotes, eyebrows
- Recommended: Playfair Display, Lora, Crimson Text, Cormorant Garamond

**Sans-Serif (Body, UI):**
- Conveys clarity, modernity, efficiency
- Best for: Body text, navigation, buttons, captions
- Recommended: Inter, Work Sans, DM Sans, Manrope

### 2. Font Pairing Formula

**The McKinsey Pattern:**
```
Headlines: Serif (elegant, authoritative)
Body: Sans-serif (clean, readable)
Accents: Serif italic (emphasis)
UI Elements: Sans-serif medium weight
```

**Example pairing:**
```css
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Inter:wght@400;500;600;700&display=swap');

h1, h2, h3 {
    font-family: 'Cormorant Garamond', serif;
    font-weight: 300; /* Light weight for elegance */
}

.accent-italic {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    font-weight: 300;
    color: var(--accent-olive);
}

body, p, a, button {
    font-family: 'Inter', sans-serif;
}
```

### 3. Size Scale (Major Third: 1.250)
```css
:root {
    --text-xs: 0.64rem;    /* 10px */
    --text-sm: 0.8rem;     /* 13px */
    --text-base: 1rem;     /* 16px */
    --text-lg: 1.25rem;    /* 20px */
    --text-xl: 1.563rem;   /* 25px */
    --text-2xl: 1.953rem;  /* 31px */
    --text-3xl: 2.441rem;  /* 39px */
    --text-4xl: 3.052rem;  /* 49px */
    --text-5xl: 3.815rem;  /* 61px */
    --text-6xl: 4.768rem;  /* 76px */
}

/* Usage */
h1 { font-size: var(--text-6xl); } /* 76px */
h2 { font-size: var(--text-4xl); } /* 49px */
h3 { font-size: var(--text-3xl); } /* 39px */
p  { font-size: var(--text-base); } /* 16px */
```

### 4. Weight Hierarchy
```css
.eyebrow {
    font-weight: 600; /* Semi-bold for labels */
    font-size: var(--text-xs);
    text-transform: uppercase;
    letter-spacing: 0.15em;
}

h1 {
    font-weight: 300; /* Light for large headlines */
}

h2 {
    font-weight: 400; /* Regular */
}

.accent {
    font-weight: 300; /* Light italic for emphasis */
    font-style: italic;
}

p {
    font-weight: 400; /* Regular for body */
}

button {
    font-weight: 600; /* Semi-bold for CTAs */
}
```

### 5. Line Height (Leading)
```css
h1, h2 {
    line-height: 1.1; /* Tight for impact */
}

h3 {
    line-height: 1.3;
}

p {
    line-height: 1.7; /* Generous for readability */
}

.small-text {
    line-height: 1.5;
}
```

### 6. Letter Spacing (Tracking)
```css
h1 {
    letter-spacing: -0.02em; /* Tighten large text */
}

.eyebrow {
    letter-spacing: 0.15em; /* Wide spacing for small caps */
    text-transform: uppercase;
}

p {
    letter-spacing: 0.01em; /* Slightly open */
}

button {
    letter-spacing: 0.03em; /* Slightly wide for emphasis */
}
```

## Premium Typography Patterns

### Pattern 1: Hero Headline
```html
<h1 class="hero-headline">
    Donde los datos
    <span class="accent-italic">se convierten</span>
    en decisiones.
</h1>
```
```css
.hero-headline {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.5rem, 6vw, 4.768rem);
    font-weight: 300;
    line-height: 1.1;
    letter-spacing: -0.02em;
    color: var(--text-dark);
}

.accent-italic {
    font-style: italic;
    color: var(--accent-olive);
    font-weight: 300;
}
```

### Pattern 2: Eyebrow + Headline
```html
<p class="eyebrow">PARA DIRECTORES GENERALES</p>
<h2 class="section-headline">
    La convergencia entre
    <span class="accent-italic">BI</span>
    y Arquitectura
</h2>
```
```css
.eyebrow {
    font-family: 'Inter', sans-serif;
    font-size: 0.64rem; /* 10px */
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--accent-olive);
    margin-bottom: 1rem;
}

.section-headline {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2rem, 4vw, 3.052rem);
    font-weight: 300;
    line-height: 1.2;
}
```

### Pattern 3: Stats Display
```html
<div class="stat-item">
    <div class="stat-number">$3.5M+</div>
    <div class="stat-label">Recuperado 2025</div>
</div>
```
```css
.stat-number {
    font-family: 'Cormorant Garamond', serif;
    font-size: 3.052rem; /* 49px */
    font-weight: 300;
    line-height: 1;
    color: var(--text-dark);
}

.stat-label {
    font-family: 'Inter', sans-serif;
    font-size: 0.8rem; /* 13px */
    font-weight: 400;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
}
```

### Pattern 4: Body Copy
```css
p {
    font-family: 'Inter', sans-serif;
    font-size: 1rem; /* 16px */
    font-weight: 400;
    line-height: 1.7;
    letter-spacing: 0.01em;
    color: var(--text-body);
    max-width: 65ch; /* Optimal reading length */
}

.lead-text {
    font-size: 1.25rem; /* 20px */
    line-height: 1.6;
    color: var(--text-dark);
}
```

## Responsive Typography

### Mobile-First Approach
```css
/* Mobile base */
h1 {
    font-size: 2.5rem; /* 40px */
}

h2 {
    font-size: 2rem; /* 32px */
}

p {
    font-size: 1rem; /* 16px */
}

/* Tablet */
@media (min-width: 768px) {
    h1 {
        font-size: 3.5rem; /* 56px */
    }
    
    h2 {
        font-size: 2.5rem; /* 40px */
    }
}

/* Desktop */
@media (min-width: 1024px) {
    h1 {
        font-size: 4.768rem; /* 76px */
    }
    
    h2 {
        font-size: 3.052rem; /* 49px */
    }
}
```

### Fluid Typography (Modern Approach)
```css
h1 {
    font-size: clamp(2.5rem, 6vw, 4.768rem);
    /* Min 40px, scales with viewport, max 76px */
}

h2 {
    font-size: clamp(2rem, 4vw, 3.052rem);
}

p {
    font-size: clamp(1rem, 1.5vw, 1.125rem);
}
```

## Color & Typography

### Text Color Hierarchy
```css
:root {
    --text-primary: #1A1A1A;   /* Headlines, important */
    --text-secondary: #2D3319; /* Body text */
    --text-muted: #707070;     /* Captions, labels */
    --text-accent: #6B7B5E;    /* CTAs, highlights */
}

h1, h2 {
    color: var(--text-primary);
}

p {
    color: var(--text-secondary);
}

.caption, .eyebrow {
    color: var(--text-muted);
}

.accent-italic {
    color: var(--text-accent);
}
```

## Accessibility

### Contrast Requirements

- Large text (18px+): Minimum 3:1
- Normal text: Minimum 4.5:1
- Enhanced (AAA): 7:1

**Test combinations:**
```
Background #F5F1E8 (Beige) + Text #1A1A1A (Black) = 14.2:1 ✅
Background #FFFFFF (White) + Text #2D3319 (Dark Green) = 12.8:1 ✅
Background #F5F1E8 + Text #6B7B5E (Olive) = 4.8:1 ✅
```

### Minimum Sizes

- Body text: Never below 16px
- Small text: Never below 13px
- Mobile: Increase base to 16-18px

## Quality Checklist

- [ ] Serif + sans-serif pairing
- [ ] Modular scale (1.250 ratio)
- [ ] Fluid responsive sizing (clamp)
- [ ] Line height: 1.1 headlines, 1.7 body
- [ ] Letter spacing: tighten large, widen small
- [ ] Color contrast meets WCAG AA
- [ ] Max-width 65ch for readability
- [ ] Light weights (300) for large headlines
- [ ] Italic used only for strategic accent
- [ ] No text smaller than 13px