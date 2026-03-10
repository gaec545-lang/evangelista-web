# Editorial Typography for Premium Corporate Sites

Advanced typography techniques that create hierarchy, readability, and sophistication.

## When to Use This Skill

- Designing text-heavy corporate sites
- Creating visual hierarchy
- Mixing serif and sans-serif fonts
- Implementing editorial-style layouts

## Font Pairing Strategies

### 1. The Classic: Serif Headlines + Sans Body

**Recommended pairings:**

**Pair 1: Playfair Display + Inter**
```css
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    font-weight: 400;
}

body, p, a {
    font-family: 'Inter', sans-serif;
}
```

**Pair 2: Lora + Work Sans**
**Pair 3: Crimson Text + DM Sans**
**Pair 4: Cormorant Garamond + Montserrat**

### 2. Sizing Scale (Modular Scale)

Use mathematical ratios for harmony:

**1.618 (Golden Ratio) Scale:**
```css
:root {
    --text-xs: 0.75rem;    /* 12px */
    --text-sm: 0.875rem;   /* 14px */
    --text-base: 1rem;     /* 16px */
    --text-lg: 1.125rem;   /* 18px */
    --text-xl: 1.25rem;    /* 20px */
    --text-2xl: 1.5rem;    /* 24px */
    --text-3xl: 2rem;      /* 32px */
    --text-4xl: 2.5rem;    /* 40px */
    --text-5xl: 3.5rem;    /* 56px */
    --text-6xl: 4.5rem;    /* 72px */
}

h1 { font-size: var(--text-6xl); }
h2 { font-size: var(--text-4xl); }
h3 { font-size: var(--text-3xl); }
p  { font-size: var(--text-lg); }
```

### 3. Weight Hierarchy

Use weight to create emphasis:
```css
h1 {
    font-weight: 300; /* Light for sophistication */
}

h2 {
    font-weight: 400; /* Regular */
}

.accent-text {
    font-weight: 600; /* Semi-bold for emphasis */
}

p {
    font-weight: 400;
}

.caption {
    font-weight: 500; /* Medium for small text */
}
```

## Advanced Typography Techniques

### 1. Italic Accents

Use italics strategically, not everywhere:
```html
<h1>
    Decisiones
    <em class="accent-italic">estratégicas</em>
    basadas en datos.
</h1>
```
```css
.accent-italic {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-weight: 400;
    color: var(--accent-gold);
}
```

### 2. Letter Spacing (Tracking)
```css
h1 {
    letter-spacing: -0.02em; /* Tighten for large text */
}

.eyebrow-text {
    letter-spacing: 0.1em;   /* Wider for small caps */
    text-transform: uppercase;
    font-size: 0.75rem;
}

p {
    letter-spacing: 0.01em;  /* Slightly open for readability */
}
```

### 3. Line Height (Leading)
```css
h1, h2, h3 {
    line-height: 1.2; /* Tight for headlines */
}

p {
    line-height: 1.8; /* Generous for body text */
}

.large-text {
    line-height: 1.6; /* Medium for larger body */
}
```

### 4. Measure (Line Length)

Optimal: 60-75 characters per line
```css
p {
    max-width: 65ch; /* Characters */
}

.narrow-column {
    max-width: 50ch;
}

.wide-column {
    max-width: 80ch;
}
```

## Editorial Layout Patterns

### 1. Drop Caps
```css
.drop-cap::first-letter {
    font-size: 5rem;
    line-height: 1;
    float: left;
    margin-right: 0.5rem;
    font-family: 'Playfair Display', serif;
    color: var(--accent-gold);
}
```

### 2. Pull Quotes
```html
<blockquote class="pull-quote">
    "Si los datos existen, encontraremos la verdad."
</blockquote>
```
```css
.pull-quote {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-style: italic;
    line-height: 1.4;
    margin: 60px 0;
    padding-left: 40px;
    border-left: 4px solid var(--accent-gold);
    color: var(--text-muted);
}
```

### 3. Eyebrow Text

Small label above headline:
```html
<p class="eyebrow">METODOLOGÍA</p>
<h2>Un proceso claro, resultados predecibles</h2>
```
```css
.eyebrow {
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.15em;
    color: var(--accent-gold);
    font-weight: 600;
    margin-bottom: 12px;
}
```

### 4. Number Styles
```css
.stat-number {
    font-family: 'Playfair Display', serif;
    font-size: 4rem;
    font-weight: 300;
    line-height: 1;
    color: var(--accent-gold);
}

.ordinal-number {
    font-feature-settings: "ordn"; /* Use OpenType ordinals */
}
```

## Responsive Typography

### 1. Fluid Type

Scale font size with viewport:
```css
h1 {
    font-size: clamp(2.5rem, 5vw, 4.5rem);
}

p {
    font-size: clamp(1rem, 1.5vw, 1.125rem);
}
```

### 2. Breakpoint-Based
```css
h1 {
    font-size: 2.5rem;
}

@media (min-width: 768px) {
    h1 {
        font-size: 3.5rem;
    }
}

@media (min-width: 1200px) {
    h1 {
        font-size: 4.5rem;
    }
}
```

## Accessibility

### 1. Contrast Ratios

- Large text (18px+): Minimum 3:1
- Body text: Minimum 4.5:1
- Dark backgrounds: Test with WebAIM tool

### 2. Font Size Minimums

- Body text: Never below 16px
- Small text: Never below 14px
- Mobile: Increase base size to 18px

## Quality Checklist

- [ ] Serif + sans-serif pairing implemented
- [ ] Modular scale for font sizes
- [ ] Line height: 1.2 headlines, 1.8 body
- [ ] Letter spacing adjusted for size
- [ ] Max-width 65ch for readability
- [ ] Responsive scaling (clamp or breakpoints)
- [ ] Contrast ratios meet WCAG AA
- [ ] No text smaller than 14px
- [ ] Italic accents used strategically
- [ ] Font weights create clear hierarchy