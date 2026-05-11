---
skill_name: corporate-website-clevel
category: web-development
difficulty: intermediate
dependencies: [html, css, javascript]
project: Evangelista & Co.
last_updated: 2026-03-09
version: 1.0
---

# Corporate Website C-Level

Skill especializado para generar código HTML/CSS/JS de alta calidad para el sitio web de Evangelista & Co., orientado a ejecutivos C-level (DG, CFO, Junta Directiva). Aplica los estándares de diseño, copy y arquitectura del proyecto.

## When to Use This Skill

Usar cuando:
- Se solicite crear o modificar secciones del sitio (hero, cards, CTAs, footer, etc.)
- Se pida agregar nuevas páginas internas
- Se requiera refactorizar HTML/CSS existente
- Se quiera mejorar UX/accesibilidad
- Se solicite ajustar copy para tono ejecutivo
- Se necesite verificar consistencia visual o de marca

Triggers:
- "agrega una sección", "crea el HTML de", "escribe el código para"
- "modifica el diseño de", "mejora el copy de"
- "nueva página", "nuevo componente"
- Cualquier tarea de front-end sobre los archivos del proyecto

---

## Core Methodology

### 1. Contexto del proyecto — leer antes de escribir
Revisar siempre:
- **Stack**: HTML + CSS puro (Inter font, variables CSS `--gold`, `--dark-blue`, etc.), JS vanilla, sin frameworks
- **CSS**: todo en `assets/css/main.css`. No usar inline styles salvo excepciones justificadas
- **JS**: `assets/js/main.js` (menú móvil, scroll header) y `assets/js/diagnostico.js` (chatbot). Toda lógica nueva va en un archivo propio o en los existentes
- **Buyer persona**: Director General, CFO, Junta Directiva. Tono formal-directo, nunca operativo ni técnico
- **Paleta**: `#d4af37` gold, `#2c3e50` dark blue, `#4a90e2` light blue, `#7f8c8d` gray, `#f8f9fa` light gray bg

### 2. Copy — reglas absolutas
- **PROHIBIDO**: dashboard, tablero, visualización, limpieza de datos, Business Intelligence, pipeline
- **OBLIGATORIO**: Decision Intelligence, Monte Carlo, ALCOA+, inteligencia forense, certeza estadística
- Títulos de sección: máximo 8 palabras
- Casos de éxito: solo frases + números, sin detallar metodología interna
- **Sin precios visibles** en ninguna página
- Sentinel siempre → `https://montecarlo-evangelistaco.streamlit.app/`
- Calendly siempre → `https://calendly.com/gaec545/30min`

### 3. Estructura HTML — patrón estándar
```html
<!-- Sección nueva -->
<section class="[nombre]-section" id="[anchor]">
    <div class="container">
        <p class="section-label">Etiqueta corta</p>
        <h2 class="section-title">Título ≤ 8 palabras</h2>
        <!-- contenido -->
    </div>
</section>
```

Reglas de estructura:
- Siempre `<section>` con `id` para anchor navigation
- Siempre `<div class="container">` dentro
- `section-label` (dorado, uppercase, 12px) antes del `h2`
- `section-title` para h2 principales
- Nunca anidar `.container` dentro de otro `.container`

### 4. CSS — patrón estándar
```css
/* === NOMBRE COMPONENTE === */
.nombre-section {
    padding: var(--section-padding) 0;
    background: var(--white); /* o dark-blue, light-gray-bg */
}

.nombre-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px;
    margin-top: 48px;
}

.nombre-card {
    padding: 36px;
    background: var(--light-gray-bg);
    border-radius: 12px;
    border-top: 3px solid transparent;
    transition: all 0.3s;
}

.nombre-card:hover {
    transform: translateY(-6px);
    border-top-color: var(--gold);
    box-shadow: 0 20px 40px rgba(0,0,0,0.08);
}

/* Responsive obligatorio */
@media (max-width: 968px) {
    .nombre-grid { grid-template-columns: 1fr; }
}
```

Variables CSS disponibles:
```css
--gold: #d4af37
--dark-blue: #2c3e50
--light-blue: #4a90e2
--gray: #7f8c8d
--white: #ffffff
--light-gray-bg: #f8f9fa
--section-padding: 100px
--container-width: 1200px
--font-primary: 'Inter', sans-serif
```

### 5. Botones — solo estas clases
```html
<!-- CTA principal (fondo dorado) -->
<button onclick="window.openDiagnostico && window.openDiagnostico()" class="btn-primary">
    Texto acción
</button>

<!-- CTA grande para secciones hero -->
<button onclick="window.openDiagnostico && window.openDiagnostico()" class="btn-primary-large">
    Texto acción
</button>

<!-- Secundario sobre fondo oscuro -->
<a href="#seccion" class="btn-outline-light">Texto</a>

<!-- Link Sentinel (siempre target blank) -->
<a href="https://montecarlo-evangelistaco.streamlit.app/" target="_blank" rel="noopener" class="btn-primary">
    Acceder a Sentinel
</a>
```

### 6. Accesibilidad — checklist mínimo
- `alt` descriptivo en todas las `<img>`
- `aria-label` en botones sin texto visible
- `aria-expanded` + `aria-controls` en menú móvil
- `role="dialog"` + `aria-modal="true"` en modales
- Contraste: texto sobre dark-blue ≥ 4.5:1
- Focus visible en todos los elementos interactivos (no quitar outline sin reemplazar)
- Headings en orden lógico: h1 → h2 → h3 (nunca saltar niveles)

### 7. Responsive — breakpoints del proyecto
```css
@media (max-width: 968px) { /* tablet: colapsar grids de 3 cols a 1 */ }
@media (max-width: 768px) { /* mobile: ocultar .desktop-nav, mostrar .mobile-menu-btn */ }
@media (max-width: 480px) { /* mobile pequeño: ajustes finos */ }
```

### 8. Páginas del proyecto — mapa
| Archivo | Propósito | Secciones clave |
|---------|-----------|-----------------|
| `index.html` | Home | hero, pain points, ecosystem (Foundation/Architecture/Sentinel), caso Textilera, diferenciadores, CTA diagnóstico |
| `por-que-nosotros.html` | Identidad | page-hero, identidad, tres pilares, garantía |
| `metodologia.html` | Proceso | page-hero, el problema, 3 fases ALCOA+, por qué funciona |
| `sectores.html` | Industrias | page-hero, 4 sector-cards, CTA sector-agnóstica |

---

## Best Practices

- **Mobile first en pruebas mentales**: diseñar columna única primero, luego expandir a grid
- **Clases semánticas**: `.hero-headline` no `.h1-big`; `.phase-card-featured` no `.highlighted`
- **Un componente = un bloque CSS**: agregar al final de `main.css` con comentario `=== NOMBRE ===`
- **No duplicar estilos**: antes de crear una clase nueva, verificar si existe en `main.css`
- **CTAs siempre con fallback**: `onclick="window.openDiagnostico && window.openDiagnostico()"` (el `&&` previene error si el script no cargó)
- **Imágenes**: solo logo `assets/logoEvangelistaCo.png` disponible. No agregar imágenes sin confirmar disponibilidad
- **Números en casos**: siempre con signo monetario o porcentaje explícito: `$2.3M`, `340%`, `+18%`

---

## Common Pitfalls to Avoid

- **No agregar precios** — aunque el brief original los mencione, las reglas de Phase 2 los prohíben
- **No usar Tailwind** — el proyecto migró a CSS puro. Cualquier clase de Tailwind quedará sin efecto
- **No usar GSAP** — removido en Phase 2. Animaciones con CSS `transition` / `@keyframes`
- **No romper el chatbot** — `diagnostico.js` auto-inyecta el FAB y modal. No crear HTML manual del chat en las páginas
- **No cambiar el link de Sentinel** — siempre `https://montecarlo-evangelistaco.streamlit.app/`, nunca `sentinel.evangelistaco.com`
- **No saltarse el `<div class="container">`** — sin él el contenido se extiende al ancho completo
- **No usar `target="_blank"` sin `rel="noopener"`** — seguridad básica

---

## Examples

### Example 1: Nueva sección "Clientes" en index.html

**Request**: "Agrega una sección de logos de clientes entre el caso de estudio y los diferenciadores"

**Output esperado**:
```html
<section class="clients-section" id="clientes">
    <div class="container">
        <p class="section-label">Confían en nosotros</p>
        <div class="clients-grid">
            <!-- logos con alt descriptivo -->
        </div>
    </div>
</section>
```
```css
/* === CLIENTS SECTION === */
.clients-section {
    padding: 60px 0;
    background: var(--light-gray-bg);
    border-top: 1px solid rgba(0,0,0,0.06);
}
.clients-grid {
    display: flex;
    gap: 48px;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    margin-top: 32px;
}
```

### Example 2: Modificar copy de hero headline

**Request**: "El hero headline es muy largo, acórtalo a menos de 8 palabras"

**Proceso**:
1. Leer el h1 actual
2. Identificar la idea central: certeza vs. incertidumbre de datos
3. Proponer 2-3 opciones ≤8 palabras en tono C-level
4. Confirmar con usuario antes de editar

**Opciones ejemplo**:
- "Sus datos tienen un problema. Lo encontraremos." (7 palabras)
- "Certeza estratégica donde había incertidumbre operativa." (6 palabras)
- "Decisiones de $10M sin datos auditados: imposible." (8 palabras)

### Example 3: Nueva página "Equipo"

**Request**: "Crea la página equipo.html"

**Proceso**:
1. Copiar estructura de `por-que-nosotros.html` (misma cabecera, footer, scripts)
2. Reemplazar `<main>` con secciones de equipo
3. Agregar link en nav de todas las páginas
4. Agregar CSS nuevo al final de `main.css`
5. Verificar: no precios, no know-how técnico, tono C-level

---

## Quality Checks

Antes de entregar cualquier código, verificar:

- [ ] No aparecen palabras prohibidas (dashboard, tablero, visualización, Business Intelligence)
- [ ] Todas las imágenes tienen `alt` descriptivo
- [ ] Botones con `onclick` usan el patrón seguro con `&&`
- [ ] Sentinel links apuntan a `montecarlo-evangelistaco.streamlit.app`
- [ ] Responsive: breakpoints 968px y 768px cubiertos
- [ ] Headings en orden lógico sin saltar niveles
- [ ] Nuevas clases CSS agregadas en `main.css`, no inline
- [ ] Títulos de sección ≤ 8 palabras
- [ ] Sin precios visibles
- [ ] `rel="noopener"` en todos los `target="_blank"`
- [ ] Copy usa tono ejecutivo-directo, no comercial
