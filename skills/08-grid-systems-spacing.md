# Grid Systems & Spacing for Premium Layouts

Mathematical precision in layout through consistent grids and spacing systems.

## When to Use This Skill

- Creating structured, aligned layouts
- Ensuring visual consistency across pages
- Building responsive designs that scale elegantly
- Establishing rhythm through spacing

## Core Principles

### 1. The 8pt Grid System

All spacing and sizing based on multiples of 8px.

**Why 8pt?**
- Divisible by 2, 4 (easy scaling)
- Works perfectly with common screen resolutions
- Creates visual rhythm and consistency

**Base scale:**
```css
:root {
    --space-1: 8px;    /* 1 unit */
    --space-2: 16px;   /* 2 units */
    --space-3: 24px;   /* 3 units */
    --space-4: 32px;   /* 4 units */
    --space-5: 40px;   /* 5 units */
    --space-6: 48px;   /* 6 units */
    --space-8: 64px;   /* 8 units */
    --space-10: 80px;  /* 10 units */
    --space-12: 96px;  /* 12 units */
    --space-15: 120px; /* 15 units */
    --space-20: 160px; /* 20 units */
}
```

### 2. Container Widths

**Standard breakpoints:**
```css
.container {
    width: 100%;
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 var(--space-4); /* 32px sides */
}

/* Responsive containers */
@media (max-width: 768px) {
    .container {
        padding: 0 var(--space-3); /* 24px on mobile */
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 var(--space-2); /* 16px on small mobile */
    }
}
```

**Content widths:**
```css
.container-narrow {
    max-width: 800px;  /* For text-heavy content */
}

.container-medium {
    max-width: 1200px; /* For mixed content */
}

.container-wide {
    max-width: 1600px; /* For wide layouts */
}

.container-full {
    max-width: 100%;   /* Full bleed */
}
```

### 3. Column Grid

**12-column system:**
```css
.grid {
    display: grid;
    grid-template-columns: repeat(12, 1fr);
    gap: var(--space-4); /* 32px gap */
}

/* Common layouts */
.col-12 { grid-column: span 12; } /* Full width */
.col-6 { grid-column: span 6; }   /* Half */
.col-4 { grid-column: span 4; }   /* Third */
.col-3 { grid-column: span 3; }   /* Quarter */

/* Responsive */
@media (max-width: 768px) {
    .col-6, .col-4, .col-3 {
        grid-column: span 12; /* Stack on mobile */
    }
}
```

**CSS Grid for complex layouts:**
```css
.advanced-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    grid-template-rows: auto auto;
    gap: var(--space-8);
}

.item-1 { grid-column: 1 / 2; grid-row: 1 / 3; }
.item-2 { grid-column: 2 / 3; grid-row: 1 / 2; }
.item-3 { grid-column: 2 / 3; grid-row: 2 / 3; }
```

## Spacing Systems

### 1. Vertical Rhythm

**Section spacing:**
```css
/* Between major sections */
.section {
    padding: var(--space-20) 0; /* 160px vertical */
}

/* Between subsections */
.subsection {
    margin-bottom: var(--space-12); /* 96px */
}

/* Between elements */
h2 {
    margin-bottom: var(--space-6); /* 48px */
}

p {
    margin-bottom: var(--space-4); /* 32px */
}

/* Tight grouping */
.meta-info {
    margin-bottom: var(--space-2); /* 16px */
}
```

**Responsive vertical spacing:**
```css
.section {
    padding: var(--space-20) 0;
}

@media (max-width: 768px) {
    .section {
        padding: var(--space-12) 0; /* 96px on tablet */
    }
}

@media (max-width: 480px) {
    .section {
        padding: var(--space-8) 0; /* 64px on mobile */
    }
}
```

### 2. Horizontal Spacing

**Element gaps:**
```css
/* Between cards/items */
.grid {
    gap: var(--space-4); /* 32px */
}

/* Tighter spacing */
.compact-grid {
    gap: var(--space-3); /* 24px */
}

/* Generous spacing */
.spacious-grid {
    gap: var(--space-6); /* 48px */
}
```

### 3. Component Padding

**Buttons:**
```css
.btn {
    padding: var(--space-2) var(--space-4); /* 16px 32px */
}

.btn-large {
    padding: var(--space-3) var(--space-6); /* 24px 48px */
}

.btn-small {
    padding: var(--space-1) var(--space-3); /* 8px 24px */
}
```

**Cards:**
```css
.card {
    padding: var(--space-6); /* 48px all sides */
}

.card-compact {
    padding: var(--space-4); /* 32px */
}
```

**Containers:**
```css
.content-wrapper {
    padding: var(--space-8) var(--space-6); /* 64px 48px */
}
```

## Layout Patterns

### 1. Split Layout (60/40)
```css
.split-layout {
    display: grid;
    grid-template-columns: 60% 40%;
    gap: var(--space-8);
    align-items: center;
}

@media (max-width: 968px) {
    .split-layout {
        grid-template-columns: 1fr;
        gap: var(--space-6);
    }
}
```

### 2. Asymmetric Grid
```css
.asymmetric-grid {
    display: grid;
    grid-template-columns: 1fr 2fr 1fr;
    gap: var(--space-6);
}

/* Content in middle column */
.main-content {
    grid-column: 2 / 3;
}
```

### 3. Masonry-Style Grid
```css
.masonry-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-4);
    grid-auto-flow: dense;
}

.masonry-item-large {
    grid-column: span 2;
    grid-row: span 2;
}
```

### 4. Full-Bleed Sections
```css
.full-bleed {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
}

.full-bleed .container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 var(--space-4);
}
```

### 5. Sticky Sidebar
```css
.sidebar-layout {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: var(--space-8);
}

.sidebar {
    position: sticky;
    top: var(--space-4);
    height: fit-content;
}
```

## Alignment Techniques

### 1. Baseline Alignment
```css
.grid-baseline {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    align-items: baseline; /* Align text baselines */
}
```

### 2. Optical Alignment

Sometimes mathematical center isn't visual center:
```css
/* For icons with visual weight */
.icon-container {
    display: flex;
    align-items: center;
    padding-top: 2px; /* Optical adjustment */
}

/* For text with descenders */
.heading {
    margin-top: -0.15em; /* Pull up slightly */
}
```

### 3. Center Alignment (Strategic Use)
```css
/* Only center when it makes sense */
.hero-content {
    text-align: center;
    max-width: 800px;
    margin: 0 auto;
}

/* Don't center body text */
.body-content {
    text-align: left;
    max-width: 65ch;
}
```

## Responsive Grid Strategies

### 1. Mobile-First Approach
```css
/* Mobile: Stack everything */
.grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: var(--space-4);
}

/* Tablet: 2 columns */
@media (min-width: 768px) {
    .grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* Desktop: 3 columns */
@media (min-width: 1024px) {
    .grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

/* Large: 4 columns */
@media (min-width: 1400px) {
    .grid {
        grid-template-columns: repeat(4, 1fr);
    }
}
```

### 2. Auto-Fit Grid
```css
.auto-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-4);
}
```

### 3. Reordering on Mobile
```css
.grid-reorder {
    display: grid;
    grid-template-columns: 1fr;
}

.item-1 { order: 2; } /* Image second on mobile */
.item-2 { order: 1; } /* Text first on mobile */

@media (min-width: 768px) {
    .grid-reorder {
        grid-template-columns: 1fr 1fr;
    }
    .item-1 { order: 1; }
    .item-2 { order: 2; }
}
```

## Common Layout Mistakes

### ❌ Inconsistent Spacing
```css
/* Bad - random numbers */
.section-1 { padding: 75px 0; }
.section-2 { padding: 90px 0; }
.section-3 { padding: 65px 0; }
```
```css
/* Good - consistent 8pt system */
.section {
    padding: var(--space-12) 0; /* 96px */
}
```

### ❌ Ignoring Breakpoints
```css
/* Bad - fixed width */
.container {
    width: 1200px; /* Breaks on small screens */
}
```
```css
/* Good - max-width */
.container {
    max-width: 1200px;
    width: 100%;
    padding: 0 var(--space-4);
}
```

### ❌ Overlapping Gutters
```css
/* Bad - nested margins compound */
.section { margin-bottom: 80px; }
.card { margin-bottom: 40px; }
```
```css
/* Good - single responsibility */
.section { margin-bottom: var(--space-12); }
.card { margin-bottom: 0; }
.card + .card { margin-top: var(--space-6); }
```

## Advanced Techniques

### 1. Subgrid (Modern CSS)
```css
.parent-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-4);
}

.child-grid {
    display: grid;
    grid-template-columns: subgrid; /* Inherits parent columns */
}
```

### 2. Aspect Ratio Containers
```css
.aspect-ratio-16-9 {
    aspect-ratio: 16 / 9;
    overflow: hidden;
}

.aspect-ratio-1-1 {
    aspect-ratio: 1 / 1;
}
```

### 3. Container Queries (Future)
```css
@container (min-width: 600px) {
    .card {
        grid-template-columns: 1fr 1fr;
    }
}
```

## Debugging Grid Issues

### 1. Visual Grid Overlay
```css
/* Development only */
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 1400px;
    height: 100%;
    background-image: repeating-linear-gradient(
        90deg,
        rgba(255,0,0,0.1) 0px,
        rgba(255,0,0,0.1) 1px,
        transparent 1px,
        transparent calc(100% / 12)
    );
    pointer-events: none;
    z-index: 9999;
}
```

### 2. Chrome DevTools
```
Right-click element → Inspect → Grid badge (purple)
Shows grid lines, gaps, and areas visually
```

## Quality Checklist

- [ ] All spacing uses 8pt system (8, 16, 24, 32...)
- [ ] Consistent section padding (120px+ desktop)
- [ ] Max-width containers (not fixed width)
- [ ] Responsive breakpoints (mobile, tablet, desktop)
- [ ] Grid gaps consistent across layout
- [ ] Mobile-first approach
- [ ] No random pixel values
- [ ] Vertical rhythm maintained
- [ ] Text max-width for readability (65ch)
- [ ] Sticky elements have safe top spacing