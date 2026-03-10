# Information Architecture for Corporate Sites

How to structure content for clarity, scannability, and conversion.

## When to Use This Skill

- Organizing complex corporate information
- Creating clear navigation hierarchies
- Structuring service offerings
- Designing content flows for decision-makers

## Core IA Principles for C-Level

### 1. The Inverted Pyramid

Most important information first:
```
1. WHAT (headline)
2. WHY (value proposition)
3. HOW (methodology)
4. PROOF (case studies)
5. ACTION (CTA)
```

### 2. The 3-Click Rule

Critical information within 3 clicks from homepage.

**Example structure:**
```
Home
├── Services
│   ├── Foundation
│   ├── Architecture
│   └── Sentinel
├── Methodology
├── Sectors
└── Contact
```

### 3. F-Pattern Scanning

Users scan in an F-shape:
- Horizontal at top
- Horizontal in middle
- Vertical down left side

**Design for it:**
```html
<section>
    <h2>Most important text</h2>  <!-- Top horizontal -->
    <p>Supporting text...</p>
    <h3>Secondary point</h3>       <!-- Middle horizontal -->
    <p>More details...</p>
    <ul>                           <!-- Left vertical -->
        <li>Bullet point</li>
        <li>Bullet point</li>
    </ul>
</section>
```

## Navigation Patterns

### 1. Sticky Header

Always accessible:
```css
header {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: rgba(0,0,0,0.95);
    backdrop-filter: blur(10px);
}
```

### 2. Clear Hierarchy
```html
<nav>
    <a href="#services">Services</a>  <!-- Primary -->
    <a href="#about">About</a>        <!-- Secondary -->
    <a href="#contact" class="cta">Contact</a> <!-- CTA -->
</nav>
```

### 3. Breadcrumbs (for deep sites)
```html
<nav aria-label="Breadcrumb">
    <ol>
        <li><a href="/">Home</a></li>
        <li><a href="/services">Services</a></li>
        <li aria-current="page">Foundation</li>
    </ol>
</nav>
```

## Content Chunking

### 1. The Rule of 3

Present information in groups of 3:
- 3 services
- 3 benefits
- 3 case studies

**Why:** Brain processes 3-4 items optimally.

### 2. Progressive Disclosure

Show summary first, details on demand:
```html
<div class="service-card">
    <h3>Foundation</h3>
    <p>Auditoría forense de datos...</p>
    <button class="expand">Leer más →</button>
    <div class="details hidden">
        <!-- Detailed content -->
    </div>
</div>
```

### 3. Scannable Blocks
```css
.content-block {
    margin-bottom: 80px; /* Clear separation */
}

h2 {
    margin-bottom: 24px;
}

p {
    margin-bottom: 20px;
    max-width: 65ch;
}
```

## Page Structure Templates

### Homepage Structure
```
1. Hero (value proposition)
2. Problem statement
3. Solution overview (3 services)
4. Social proof (stats/logos)
5. How it works (process)
6. Case study highlight
7. CTA (diagnostic)
```

### Service Page Structure
```
1. Hero (service name + tagline)
2. The problem we solve
3. How we solve it (methodology)
4. Deliverables
5. Case examples
6. FAQ
7. CTA (schedule consultation)
```

### About Page Structure
```
1. Mission statement
2. Our story
3. Values/Principles
4. Team (if relevant)
5. Differentiators
6. CTA
```

## Hierarchy Techniques

### 1. Visual Weight
```css
/* Primary content */
h1 {
    font-size: 4rem;
    font-weight: 300;
}

/* Secondary content */
h2 {
    font-size: 2.5rem;
    font-weight: 400;
}

/* Supporting content */
p {
    font-size: 1.125rem;
    color: var(--text-muted);
}
```

### 2. Color Hierarchy
```css
:root {
    --text-primary: #ffffff;      /* Headlines */
    --text-secondary: #cccccc;    /* Body */
    --text-tertiary: #999999;     /* Captions */
    --text-accent: #d4af37;       /* CTAs */
}
```

### 3. Spacing Hierarchy
```css
.section-gap-large { margin-bottom: 120px; }
.section-gap-medium { margin-bottom: 80px; }
.section-gap-small { margin-bottom: 40px; }
```

## Call-to-Action Placement

### 1. Above the Fold

Always have one primary CTA visible without scrolling.

### 2. Repeated CTAs

- Hero: Primary CTA
- Mid-page: Secondary CTA (after proof)
- Footer: Final CTA

### 3. CTA Hierarchy
```html
<!-- Primary CTA -->
<a href="#" class="cta-primary">Agendar Diagnóstico</a>

<!-- Secondary CTA -->
<a href="#" class="cta-secondary">Conocer Metodología</a>

<!-- Tertiary CTA (text link) -->
<a href="#" class="cta-text">Leer más →</a>
```

## Mobile-First IA

### 1. Priority Content First
```html
<!-- Mobile: Stack vertically, most important first -->
<section>
    <h2>Headline</h2>      <!-- 1st -->
    <p>Key point</p>       <!-- 2nd -->
    <img src="visual.jpg"> <!-- 3rd -->
</section>
```

### 2. Hamburger Menu (when needed)
```html
<button class="menu-toggle" aria-label="Open menu">
    <span></span>
    <span></span>
    <span></span>
</button>
```

### 3. Touch Targets

Minimum 44x44px for tap targets:
```css
.mobile-cta {
    min-height: 44px;
    min-width: 44px;
    padding: 12px 24px;
}
```

## Quality Checklist

- [ ] Most important info above the fold
- [ ] Clear visual hierarchy (size, weight, color)
- [ ] Content chunked in groups of 3
- [ ] Navigation within 3 clicks
- [ ] Primary CTA on every page
- [ ] Mobile-first responsive structure
- [ ] Scannable F-pattern layout
- [ ] Progressive disclosure for complex content
- [ ] Clear breadcrumbs (if applicable)
- [ ] Sticky navigation on scroll