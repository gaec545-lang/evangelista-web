# Color Psychology for Corporate Premium Sites

Strategic use of color to convey authority, trust, and sophistication.

## When to Use This Skill

- Selecting color palettes for corporate brands
- Creating visual hierarchy through color
- Conveying specific emotions/messages
- Ensuring accessibility and readability

## Color Psychology Fundamentals

### 1. Black - Authority & Sophistication

**Psychological associations:**
- Power, authority, control
- Sophistication, elegance
- Mystery, exclusivity
- Timelessness

**Best for:**
- Luxury brands
- Professional services
- High-end consulting
- Premium products

**Usage:**
```css
:root {
    --bg-primary: #000000;
    --bg-secondary: #0a0a0a;  /* Slightly lifted */
    --bg-tertiary: #1a1a1a;   /* Card backgrounds */
}
```

### 2. Gold - Premium & Success

**Psychological associations:**
- Wealth, prosperity
- Achievement, success
- Quality, premium
- Warmth, optimism

**Best for:**
- CTAs
- Accent elements
- Stats/numbers
- Icons/highlights

**Usage:**
```css
:root {
    --accent-gold: #d4af37;      /* Primary gold */
    --accent-gold-dark: #b8941f;  /* Hover state */
    --accent-gold-light: #f0d87c; /* Highlights */
}
```

### 3. White - Clarity & Purity

**Psychological associations:**
- Clarity, simplicity
- Purity, cleanliness
- Space, openness
- Neutrality

**Best for:**
- Text on dark backgrounds
- Negative space
- Clean sections
- Contrast elements

### 4. Gray - Professionalism & Balance

**Psychological associations:**
- Neutrality, balance
- Professionalism
- Sophistication
- Maturity

**Usage:**
```css
:root {
    --text-primary: #ffffff;
    --text-secondary: #cccccc;
    --text-muted: #999999;
    --text-subtle: #666666;
}
```

## Strategic Color Application

### 1. 60-30-10 Rule

**Proportion:**
- 60% Dominant color (Black background)
- 30% Secondary color (White text)
- 10% Accent color (Gold highlights)

**Example:**
```css
body {
    background: var(--bg-primary);      /* 60% */
    color: var(--text-secondary);       /* 30% */
}

.cta, .accent {
    color: var(--accent-gold);          /* 10% */
}
```

### 2. Hierarchy Through Color

**Priority levels:**
```css
/* Level 1: Primary attention */
.cta-primary {
    background: var(--accent-gold);
    color: #000000;
}

/* Level 2: Secondary attention */
.heading {
    color: var(--text-primary); /* Pure white */
}

/* Level 3: Supporting content */
.body-text {
    color: var(--text-secondary); /* Light gray */
}

/* Level 4: Subtle/metadata */
.caption {
    color: var(--text-muted); /* Medium gray */
}
```

### 3. Semantic Colors

**Meaning through color:**
```css
:root {
    --success: #4caf50;    /* Green - positive */
    --warning: #ff9800;    /* Orange - caution */
    --error: #f44336;      /* Red - danger */
    --info: #2196f3;       /* Blue - neutral info */
}
```

## Color Combinations for Premium Feel

### Palette 1: Monochromatic Elegance
```css
:root {
    --black-pure: #000000;
    --black-90: #1a1a1a;
    --black-80: #333333;
    --black-70: #4d4d4d;
    --black-60: #666666;
    --gold: #d4af37;
    --white: #ffffff;
}
```

### Palette 2: Warm Sophistication
```css
:root {
    --bg-dark: #0a0a0a;
    --bg-warm: #1a1410;       /* Slight brown tint */
    --accent-gold: #d4af37;
    --accent-copper: #b87333;  /* Additional warmth */
    --text-warm: #f5f5dc;      /* Beige white */
}
```

### Palette 3: Cool Authority
```css
:root {
    --bg-dark: #000000;
    --bg-blue: #0d1117;        /* Slight blue tint */
    --accent-silver: #c0c0c0;
    --accent-ice: #89cff0;     /* Subtle blue */
    --text-cool: #e8f4f8;      /* Cool white */
}
```

## Gradients (Subtle Only)

### 1. Background Gradients
```css
.hero-gradient {
    background: linear-gradient(
        135deg,
        #000000 0%,
        #1a1a1a 100%
    );
}

.warm-gradient {
    background: linear-gradient(
        to bottom,
        rgba(0,0,0,0.9),
        rgba(26,20,16,0.95)
    );
}
```

### 2. Text Gradients (Accents Only)
```css
.gradient-text {
    background: linear-gradient(
        90deg,
        #d4af37 0%,
        #f0d87c 100%
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
```

### 3. Overlay Gradients
```css
.image-overlay::before {
    content: '';
    background: linear-gradient(
        to bottom,
        rgba(0,0,0,0.3) 0%,
        rgba(0,0,0,0.7) 100%
    );
}
```

## Accessibility & Contrast

### 1. WCAG Contrast Ratios

**Requirements:**
- Large text (18px+): Minimum 3:1
- Normal text: Minimum 4.5:1
- Enhanced (AAA): 7:1

**Test combinations:**
```css
/* Good contrast */
background: #000000;
color: #ffffff;          /* 21:1 ratio */

background: #000000;
color: #d4af37;          /* 8.2:1 ratio */

/* Poor contrast (avoid) */
background: #000000;
color: #666666;          /* 5.7:1 - borderline */
```

### 2. Testing Tools

- WebAIM Contrast Checker
- Chrome DevTools (Lighthouse)
- Contrast Ratio calculator

### 3. Color Blindness Considerations

**Safe color pairs:**
- Black + Gold ✅
- Black + White ✅
- Black + Blue ✅

**Avoid:**
- Red + Green (common colorblindness)
- Blue + Purple (hard to distinguish)
- Relying on color alone for meaning

## Dark Mode Specifics

### 1. True Black vs. Dark Gray
```css
/* True black - AMOLED screens */
--bg-true-black: #000000;

/* Dark gray - LCD screens (less harsh) */
--bg-dark-gray: #121212;
```

### 2. Reducing Eye Strain
```css
body {
    background: #000000;
    color: #e0e0e0;  /* Not pure white - easier on eyes */
}

/* Avoid pure white text on pure black */
p {
    color: #cccccc;  /* Slightly muted */
}
```

### 3. Elevation Through Color
```css
.surface-1 { background: #0a0a0a; }
.surface-2 { background: #1a1a1a; }
.surface-3 { background: #2a2a2a; }
```

## Color Application Patterns

### 1. Hero Section
```css
.hero {
    background: linear-gradient(135deg, #000 0%, #1a1a1a 100%);
    color: #ffffff;
}

.hero-accent {
    color: var(--accent-gold);
    font-style: italic;
}
```

### 2. Stats/Numbers
```css
.stat-number {
    color: var(--accent-gold);
    font-size: 4rem;
}

.stat-label {
    color: var(--text-muted);
}
```

### 3. Cards
```css
.card {
    background: var(--bg-secondary);
    border-top: 2px solid var(--accent-gold);
}

.card:hover {
    border-top-color: var(--accent-gold-light);
}
```

### 4. CTAs
```css
.cta-primary {
    background: var(--accent-gold);
    color: #000000;  /* Dark text on light gold */
}

.cta-secondary {
    background: transparent;
    color: var(--accent-gold);
    border: 2px solid var(--accent-gold);
}
```

## Common Mistakes

❌ **Too many accent colors** - Looks chaotic
✅ **One primary accent** - Gold only

❌ **Pure white on pure black** - Eye strain
✅ **Off-white on black** - Comfortable

❌ **Colorful for the sake of it** - Unprofessional
✅ **Strategic color use** - Purposeful

❌ **Low contrast** - Accessibility fail
✅ **4.5:1 minimum** - WCAG compliant

## Quality Checklist

- [ ] Maximum 4 colors in palette
- [ ] Gold used strategically (10% or less)
- [ ] Text contrast meets WCAG AA (4.5:1)
- [ ] No pure white text on pure black
- [ ] Semantic colors for states (success/error)
- [ ] Gradients subtle and purposeful
- [ ] Tested for color blindness
- [ ] Elevation through color (if needed)
- [ ] Hover states use color variation
- [ ] Consistent color application