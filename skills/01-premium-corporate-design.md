# Premium Corporate Design for C-Level Executives

Design principles for creating high-end corporate websites that appeal to Directors, CEOs, and CFOs.

## When to Use This Skill

- Creating websites for professional services firms
- B2B sites targeting C-level decision makers
- Corporate redesigns requiring sophistication and gravitas
- Any site where trust, authority, and premium positioning matter

## Core Design Principles

### 1. Dark Themes with Strategic Contrast

**Why Dark Backgrounds Work for C-Level:**
- Conveys sophistication and exclusivity
- Reduces eye strain for long reading sessions
- Makes content (especially numbers/data) pop dramatically
- Creates focus through negative space

**Implementation:**
```css
/* Primary dark palette */
--bg-primary: #000000;
--bg-secondary: #0a0a0a;
--bg-tertiary: #1a1a1a;

/* Strategic light accents */
--accent-gold: #d4af37;
--accent-light: #ffffff;
--text-muted: #999999;
```

### 2. Generous White Space (Negative Space)

C-level executives scan quickly. Cramped designs = cheap appearance.

**Rules:**
- Section padding: minimum 120px vertical
- Between elements: 60-80px
- Around CTAs: 40px minimum breathing room
- Line height: 1.8-2.0 for body text

**Example:**
```css
.section {
    padding: 140px 0;
}

.section-title {
    margin-bottom: 60px;
}

p {
    line-height: 1.9;
    margin-bottom: 32px;
}
```

### 3. Asymmetric Layouts

Avoid boring centered blocks. Use dynamic asymmetry.

**Patterns:**
- 60/40 split layouts (text left, visual right)
- Diagonal elements breaking the grid
- Overlapping sections for depth
- Offset headings that break alignment

### 4. Serif + Sans-Serif Mixing

**Formula:**
- Headlines: Serif (Playfair Display, Lora, Crimson Text)
- Body: Sans-serif (Inter, Work Sans, DM Sans)
- Accents: Italic serif for emphasis

**Example:**
```css
h1, h2 {
    font-family: 'Playfair Display', serif;
    font-weight: 400; /* Light weight for elegance */
    font-style: italic; /* Accent words */
}

body, p {
    font-family: 'Inter', sans-serif;
    font-weight: 400;
}
```

### 5. Restrained Color Palette

Less is more. Limit to 3-4 colors max.

**Premium Palette Structure:**
- Primary: Black/Very Dark
- Secondary: White/Off-white
- Accent 1: Metallic (Gold #d4af37, Silver #C0C0C0)
- Accent 2 (optional): Muted earth tone

### 6. High-Quality Imagery

**Requirements:**
- Minimum 1920px width
- Professional photography (no stock photo clichés)
- Subtle overlays (dark gradient 0.3-0.5 opacity)
- Strategic placement, not decoration

### 7. Subtle Animations

Animations should whisper, not shout.

**Good animations:**
- Fade-in on scroll (0.6s ease)
- Hover scale (1.05, 0.3s)
- Parallax backgrounds (subtle depth)
- Number counters for stats

**Avoid:**
- Bouncing elements
- Excessive transitions
- Distracting movement
- Auto-playing carousels

## Layout Patterns for C-Level

### Pattern 1: Full-Screen Hero with Minimal Text
```html
<section class="hero-fullscreen">
    <div class="hero-content">
        <h1 class="hero-title">
            Decisiones
            <span class="accent">estratégicas</span>
            basadas en datos.
        </h1>
        <p class="hero-subtitle">Subtle, short description</p>
        <a href="#" class="cta-primary">Single CTA</a>
    </div>
</section>
```

**Styling:**
- Background: Dark with subtle texture
- Title: Large (60-80px), serif + sans mix
- One accent word in gold italic
- Single CTA, not two competing buttons

### Pattern 2: Split-Screen with Visual Anchor
```html
<section class="split-layout">
    <div class="content-left">
        <h2>Feature Title</h2>
        <p>Description with generous spacing...</p>
    </div>
    <div class="visual-right">
        <img src="high-quality-image.jpg" alt="">
    </div>
</section>
```

### Pattern 3: Stats Grid with Dramatic Numbers
```html
<section class="stats-showcase">
    <div class="stat-item">
        <div class="stat-number">$2.3M</div>
        <div class="stat-label">Recuperado</div>
    </div>
</section>
```

**Styling:**
```css
.stat-number {
    font-size: 64px;
    font-weight: 300;
    color: var(--accent-gold);
    font-family: 'Playfair Display', serif;
}
```

## Common Mistakes to Avoid

❌ **Too many colors** - Looks chaotic
✅ **Stick to 3-4 max**

❌ **Centered everything** - Boring, predictable
✅ **Asymmetric layouts** - Dynamic, engaging

❌ **No breathing room** - Looks cheap
✅ **Generous spacing** - Premium feel

❌ **Stock photo clichés** (handshakes, suits)
✅ **Abstract, architectural, or data-viz imagery**

❌ **Multiple CTAs competing**
✅ **One primary CTA per section**

## Quality Checklist

Before finalizing:
- [ ] Sections have 120px+ vertical padding
- [ ] Dark theme with strategic gold accents
- [ ] Serif + sans-serif font pairing
- [ ] Asymmetric layouts, not all centered
- [ ] Subtle animations (fade, scale)
- [ ] High-quality imagery (1920px+)
- [ ] One primary CTA per section
- [ ] Mobile responsive (not just shrunk desktop)
- [ ] Fast loading (<3s)
- [ ] Accessible (WCAG AA minimum)