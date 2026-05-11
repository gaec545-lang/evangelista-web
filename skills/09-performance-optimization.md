# Performance Optimization for Corporate Sites

Fast-loading, efficient sites that respect executive time and project authority.

## When to Use This Skill

- Optimizing site speed and load times
- Reducing file sizes and requests
- Implementing lazy loading and caching
- Ensuring smooth animations and interactions

## Core Principles

### 1. Performance = Professionalism

Slow sites signal carelessness.

**Target metrics:**
- First Contentful Paint: <1.8s
- Largest Contentful Paint: <2.5s
- Time to Interactive: <3.8s
- Total page size: <2MB
- Lighthouse score: 90+

### 2. Measure First, Optimize Second

Use tools before making changes:
- Chrome DevTools (Lighthouse)
- PageSpeed Insights
- WebPageTest
- GTmetrix

## Critical Optimizations

### 1. Image Optimization

**Compression:**
```bash
# Use TinyPNG, Squoosh, or ImageOptim
# Target: <300KB for hero images, <150KB for sections
```

**Modern formats:**
```html
<picture>
    <source srcset="image.webp" type="image/webp">
    <source srcset="image.jpg" type="image/jpeg">
    <img src="image.jpg" alt="Fallback">
</picture>
```

**Responsive images:**
```html
<img 
    src="image-1920.jpg"
    srcset="image-768.jpg 768w,
            image-1200.jpg 1200w,
            image-1920.jpg 1920w"
    sizes="(max-width: 768px) 100vw,
           (max-width: 1200px) 80vw,
           1200px"
    loading="lazy"
    alt="Description"
>
```

**Lazy loading:**
```html
<!-- Native lazy loading -->
<img src="image.jpg" loading="lazy" alt="Description">

<!-- Above-fold images: eager -->
<img src="hero.jpg" loading="eager" alt="Hero">
```

### 2. Font Optimization

**Subset fonts:**
```html
<!-- Load only Latin characters if Spanish-only site -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap&subset=latin" rel="stylesheet">
```

**Font loading strategy:**
```css
/* 1. Use font-display: swap */
@font-face {
    font-family: 'Inter';
    src: url('inter.woff2') format('woff2');
    font-display: swap; /* Shows fallback immediately */
}

/* 2. Preload critical fonts */
<link rel="preload" href="inter-bold.woff2" as="font" type="font/woff2" crossorigin>
```

**Fallback stack:**
```css
body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 
                 'Segoe UI', Roboto, sans-serif;
}
```

### 3. CSS Optimization

**Critical CSS:**
```html
<!-- Inline critical CSS for above-fold content -->
<style>
    /* Only styles needed for initial render */
    body { margin: 0; background: #000; }
    .hero { min-height: 100vh; }
</style>

<!-- Defer non-critical CSS -->
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="styles.css"></noscript>
```

**Minify CSS:**
```bash
# Use cssnano, clean-css, or build tools
# Remove: comments, whitespace, redundant rules
```

**Avoid CSS imports:**
```css
/* Bad - blocks rendering */
@import url('another.css');

/* Good - concatenate files */
/* Include directly in main CSS */
```

### 4. JavaScript Optimization

**Defer non-critical JS:**
```html
<!-- Defer execution until DOM ready -->
<script src="script.js" defer></script>

<!-- Async for independent scripts -->
<script src="analytics.js" async></script>
```

**Code splitting:**
```javascript
// Load only when needed
button.addEventListener('click', async () => {
    const module = await import('./heavy-feature.js');
    module.init();
});
```

**Minimize libraries:**
```javascript
// Bad - entire library for one function
import _ from 'lodash'; // 70KB

// Good - import only what you need
import debounce from 'lodash/debounce'; // 2KB
```

### 5. Resource Hints

**Preconnect to external domains:**
```html
<!-- Establish early connections -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://api.anthropic.com">
```

**DNS prefetch:**
```html
<link rel="dns-prefetch" href="https://analytics.google.com">
```

**Prefetch next pages:**
```html
<!-- For likely navigation targets -->
<link rel="prefetch" href="/metodologia.html">
```

## Caching Strategies

### 1. Browser Caching
```html
<!-- In .htaccess or server config -->
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType text/html "access plus 1 hour"
</IfModule>
```

### 2. Service Worker (PWA)
```javascript
// Cache static assets
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open('v1').then(cache => {
            return cache.addAll([
                '/',
                '/styles.css',
                '/script.js',
                '/logo.png'
            ]);
        })
    );
});
```

### 3. CDN Usage
```html
<!-- Use CDN for libraries -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.0/gsap.min.js"></script>
```

## Rendering Optimization

### 1. Critical Rendering Path

**Optimize order:**
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- 1. Preconnect to external domains -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    
    <!-- 2. Preload critical fonts -->
    <link rel="preload" href="inter-bold.woff2" as="font" crossorigin>
    
    <!-- 3. Inline critical CSS -->
    <style>/* Critical CSS here */</style>
    
    <!-- 4. Defer non-critical CSS -->
    <link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'">
</head>
<body>
    <!-- Content -->
    
    <!-- 5. Defer JavaScript -->
    <script src="script.js" defer></script>
</body>
</html>
```

### 2. Minimize Reflows
```javascript
// Bad - triggers multiple reflows
element.style.width = '100px';
element.style.height = '100px';
element.style.background = 'red';

// Good - batch changes
element.style.cssText = 'width: 100px; height: 100px; background: red;';

// Best - use classes
element.classList.add('styled');
```

### 3. Use Transform for Animations
```css
/* Bad - triggers layout */
.element {
    animation: slide 1s;
}

@keyframes slide {
    from { left: 0; }
    to { left: 100px; }
}

/* Good - GPU accelerated */
.element {
    animation: slide 1s;
}

@keyframes slide {
    from { transform: translateX(0); }
    to { transform: translateX(100px); }
}
```

## Third-Party Scripts

### 1. Async Loading
```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXX"></script>
```

### 2. Lazy Load Non-Critical
```javascript
// Load chatbot only on interaction
let chatLoaded = false;
document.querySelector('.chat-button').addEventListener('click', () => {
    if (!chatLoaded) {
        const script = document.createElement('script');
        script.src = 'chatbot.js';
        document.body.appendChild(script);
        chatLoaded = true;
    }
});
```

### 3. Self-Host When Possible
```html
<!-- Instead of external CDN, host locally -->
<link rel="stylesheet" href="/fonts/inter.css">
```

## Mobile Performance

### 1. Reduce Payload
```css
/* Hide heavy elements on mobile */
@media (max-width: 768px) {
    .desktop-only-video {
        display: none;
    }
}
```

### 2. Touch Optimization
```css
/* Faster tap response */
a, button {
    touch-action: manipulation;
}
```

### 3. Reduce JavaScript
```javascript
// Feature detection
if ('IntersectionObserver' in window) {
    // Use modern API
} else {
    // Fallback or skip feature
}
```

## Monitoring & Testing

### 1. Real User Monitoring (RUM)
```javascript
// Track actual user performance
window.addEventListener('load', () => {
    const perfData = window.performance.timing;
    const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
    
    // Send to analytics
    console.log('Page load time:', pageLoadTime);
});
```

### 2. Performance Budget
```
Budget limits:
- Total page size: <2MB
- JavaScript: <400KB
- CSS: <100KB
- Images: <1.5MB
- Fonts: <200KB
- Requests: <50
```

### 3. Lighthouse CI
```bash
# Run Lighthouse in CI/CD
lighthouse https://evangelistaco.com --view

# Minimum scores:
# Performance: 90+
# Accessibility: 95+
# Best Practices: 95+
# SEO: 95+
```

## Common Performance Killers

### ❌ Unoptimized Images

- 5MB hero image → 300KB hero image
- No lazy loading → Lazy load below fold
- No responsive images → srcset implementation

### ❌ Render-Blocking Resources

- Blocking CSS → Critical CSS inline + defer rest
- Blocking JS → Defer/async attributes
- No preconnect → Preconnect external domains

### ❌ Too Many Requests

- 100+ HTTP requests → Combine files
- Every icon as image → SVG sprite or icon font
- Multiple font weights → Load only 2-3 weights

### ❌ Heavy JavaScript

- Entire jQuery library → Vanilla JS
- Unused libraries → Remove or lazy load
- No code splitting → Split by route

## Quick Wins Checklist

- [ ] Enable gzip/brotli compression
- [ ] Minify CSS, JS, HTML
- [ ] Optimize and compress images
- [ ] Use WebP format with JPG fallback
- [ ] Lazy load below-fold images
- [ ] Defer non-critical JavaScript
- [ ] Inline critical CSS
- [ ] Preconnect to external domains
- [ ] Enable browser caching
- [ ] Use CDN for static assets
- [ ] Minimize third-party scripts
- [ ] Remove unused CSS/JS
- [ ] Use system fonts or subset web fonts
- [ ] Implement service worker
- [ ] Monitor with Lighthouse

## Advanced Optimizations

### 1. HTTP/2 Server Push
```
Link: </styles.css>; rel=preload; as=style
Link: </script.js>; rel=preload; as=script
```

### 2. Image Sprites
```css
.icon {
    background: url('icons-sprite.png') no-repeat;
}

.icon-email { background-position: 0 0; }
.icon-phone { background-position: -50px 0; }
```

### 3. Resource Compression
```bash
# Enable in server config
gzip on;
gzip_types text/css application/javascript image/svg+xml;
gzip_min_length 1000;
```

## Quality Checklist

- [ ] Lighthouse score 90+ (all categories)
- [ ] First Contentful Paint <1.8s
- [ ] Total page size <2MB
- [ ] Images optimized (<300KB hero)
- [ ] Lazy loading implemented
- [ ] CSS/JS minified
- [ ] Browser caching enabled
- [ ] Third-party scripts async/deferred
- [ ] Mobile performance tested
- [ ] Real user monitoring set up