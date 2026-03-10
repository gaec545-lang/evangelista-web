# Visual Assets & Imagery for Premium Corporate Sites

How to source, optimize, and implement high-quality images that elevate corporate websites.

## When to Use This Skill

- Sourcing professional imagery for corporate sites
- Optimizing images for web performance
- Creating image overlays and effects
- Implementing hero backgrounds and section visuals

## Image Sourcing Strategies

### 1. Free High-Quality Sources

**Recommended sites for corporate imagery:**
- **Unsplash** (unsplash.com) - Best for abstract, architectural
- **Pexels** (pexels.com) - Good for business contexts
- **Pixabay** (pixabay.com) - Alternative options

**Search keywords for corporate sites:**
- "architecture minimal"
- "data visualization abstract"
- "modern office building"
- "geometric patterns"
- "minimalist workspace"
- "technology abstract"

**Avoid these clichés:**
- Handshakes in suits
- Stock smiling business people
- Generic conference rooms
- Cheesy team photos

### 2. Search Strategy
```javascript
// Example: Searching Unsplash via URL
https://unsplash.com/s/photos/architecture-minimal-dark

// Download high-res (1920px+)
// Right-click > Save As > image-name.jpg
```

### 3. Image Specifications

**Hero backgrounds:**
- Minimum: 1920x1080px
- Recommended: 2560x1440px
- Format: JPG (for photos)
- Compression: 70-80% quality

**Section images:**
- Minimum: 1200x800px
- Format: JPG or WebP
- Compression: 75-85% quality

## Image Optimization

### 1. Compression Tools

**Online tools:**
- TinyPNG (tinypng.com) - Smart compression
- Squoosh (squoosh.app) - Advanced control
- ImageOptim (imageoptim.com) - Mac app

**Target file sizes:**
- Hero images: <300KB
- Section images: <150KB
- Thumbnails: <50KB

### 2. Responsive Images
```html
<!-- Single source with srcset -->
<img 
    src="image-1920.jpg" 
    srcset="image-768.jpg 768w,
            image-1200.jpg 1200w,
            image-1920.jpg 1920w"
    sizes="100vw"
    alt="Descriptive alt text"
>
```

### 3. WebP Format

Modern format with better compression:
```html
<picture>
    <source srcset="image.webp" type="image/webp">
    <source srcset="image.jpg" type="image/jpeg">
    <img src="image.jpg" alt="Fallback">
</picture>
```

## Image Effects & Overlays

### 1. Dark Overlay for Text Legibility
```css
.hero-image {
    position: relative;
}

.hero-image::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(
        to bottom,
        rgba(0,0,0,0.3),
        rgba(0,0,0,0.7)
    );
    z-index: 1;
}

.hero-content {
    position: relative;
    z-index: 2;
}
```

### 2. Subtle Parallax Effect
```css
.parallax-bg {
    background-attachment: fixed;
    background-position: center;
    background-size: cover;
}
```

### 3. Grayscale with Color on Hover
```css
.image-hover {
    filter: grayscale(100%);
    transition: filter 0.5s ease;
}

.image-hover:hover {
    filter: grayscale(0%);
}
```

## Strategic Image Placement

### 1. Hero Section

**Best practices:**
- Full-width background
- Dark overlay (0.4-0.6 opacity)
- Centered or left-aligned text
- Subtle texture or gradient
```css
.hero {
    min-height: 100vh;
    background-image: url('hero-bg.jpg');
    background-size: cover;
    background-position: center;
    position: relative;
}
```

### 2. Section Breaks

Use images to create visual rhythm:
- Every 2-3 sections
- Alternate text-only and image sections
- Use negative space strategically

### 3. Background Patterns

Subtle geometric patterns for texture:
```css
.section {
    background-image: url('data:image/svg+xml,<svg width="60" height="60">...</svg>');
    background-size: 60px 60px;
    opacity: 0.05;
}
```

## Image Types for Different Sections

### Hero
- Architectural
- Abstract data viz
- Minimalist workspaces
- Dark moody photography

### About/Services
- Geometric patterns
- Technology abstracts
- Clean office environments
- Team at work (candid, not posed)

### Stats/Results
- Data visualization
- Graphs and charts (stylized)
- Abstract representations

### Contact/CTA
- Warm, inviting spaces
- Subtle lighting
- Architectural details

## Performance Optimization

### 1. Lazy Loading
```html
<img src="image.jpg" loading="lazy" alt="Description">
```

### 2. Image Sprites

Combine small icons into one file:
```css
.icon-email {
    background: url('icons-sprite.png') 0 0;
}

.icon-phone {
    background: url('icons-sprite.png') -50px 0;
}
```

### 3. CSS Gradients Instead of Images

When possible, use CSS:
```css
.gradient-bg {
    background: linear-gradient(135deg, #000 0%, #1a1a1a 100%);
}
```

## Quality Checklist

- [ ] All images optimized (<300KB for heroes)
- [ ] WebP format with JPG fallback
- [ ] Responsive srcset implemented
- [ ] Lazy loading on below-fold images
- [ ] Dark overlays for text legibility
- [ ] No stock photo clichés
- [ ] Alt text on all images
- [ ] Proper aspect ratios maintained