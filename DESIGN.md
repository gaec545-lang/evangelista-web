# Sistema de Diseño — Evangelista & Co.

## Contexto del Producto
- **Qué es:** Plataforma corporativa para una firma élite de inteligencia estratégica y operativa.
- **Para quién es:** C-Level (CEOs, COOs, Directores de Finanzas).
- **Industria/Espacio:** Consultoría de Negocios, Business Intelligence Forense, "Seguros contra el Caos".
- **Tipo de proyecto:** Sitio corporativo / Marketing B2B de alto nivel.

## Dirección Estética
- **Dirección:** "New York Advisory" (Refinado / Editorial / Lujo Corporativo).
- **Nivel de decoración:** Mínimo. La tipografía, los espacios en blanco y el contraste de colores hacen todo el trabajo.
- **Mood (Sensación):** Autoridad, intelecto, seriedad, elegancia forense. No somos instaladores de software; somos estrategas financieros y operativos.

## Tipografía
- **Display/Hero (Titulares):** `Fraunces` (o `Playfair Display` como alternativa).
  - *Razón:* Una serifa clásica y elegante que proyecta el peso y la tradición de una firma consultora de Wall Street.
- **Cuerpo (Textos largos):** `DM Sans`.
  - *Razón:* Una fuente sin remates muy limpia y legible que moderniza el diseño sin caer en lo genérico del "SaaS tech".
- **UI/Etiquetas:** `DM Sans` (en mayúsculas con espaciado amplio para metadatos).
- **Datos/Tablas:** `DM Sans` (soporta números tabulares para reportes financieros).

## Color
- **Enfoque:** Restringido. Alto contraste.
- **Fondo Principal:** Beige `#F4F1EA` (El "papel" base, aporta lujo y calidez).
- **Texto Principal y Contraste:** Carbón `#1C1C1C` (Autoridad absoluta, máxima legibilidad).
- **Acento y Marca:** Oliva `#5A6352` (Un color maduro, forense y elegante para elementos interactivos sutiles y detalles gráficos).

## Espaciado
- **Unidad Base:** 8px.
- **Densidad:** Espaciosa (Lujo). Las áreas de descanso visual son fundamentales.
- **Escala:**
  - `xs`: 4px
  - `sm`: 8px
  - `md`: 16px
  - `lg`: 24px
  - `xl`: 32px
  - `2xl`: 48px
  - `3xl`: 64px
  - `hero`: 120px+

## Layout (Composición)
- **Enfoque:** Disciplinado por grid, pero con licencias editoriales (asimetrías en secciones de texto).
- **Ancho máximo de contenido:** 1200px (para mantener líneas de texto legibles).
- **Bordes:** Nulos o mínimos. Sin radios redondeados (border-radius: 0) para mantener la crudeza y seriedad corporativa, evitando el aspecto "amigable" de las apps.

## Movimiento (Motion)
- **Enfoque:** Funcional y Mínimo.
- **Transiciones:** Suaves (fade-ins, transformaciones muy sutiles de opacidad en hovers).
- **Velocidad:** `medium` (250-400ms). Nada de "rebotes" (springs).

## Registro de Decisiones
| Fecha | Decisión | Razón |
|-------|----------|-------|
| 2026-05-04 | Creación inicial del sistema de diseño | Definido por consultoría para alinear la estética visual con el mensaje de "Firma de Élite C-Level". |
| 2026-05-04 | **Decisión 1B — Sistema Tailwind unificado con tokens de DESIGN.md** | Se actualizó el `tailwind.config` para que `font-serif` resuelva a Fraunces y `font-sans` a DM Sans. Se eliminó la segunda importación de Google Fonts (Cormorant Garamond + Inter). Todo el sitio ahora usa un solo sistema tipográfico. |
| 2026-05-04 | **Decisión 2B — Alternancia blanco/beige entre secciones** | Las secciones `#posicionamiento` y `#modelo-intervencion` conservan `bg-white` para crear ritmo visual editorial. Patrón intencional, no inconsistencia. |
| 2026-05-04 | **Decisión 3A — Reemplazo del círculo SVG por número editorial** | El decorativo crosshair/círculo concéntrico del hero fue sustituido por el número "01" en Fraunces a 4% de opacidad, estilo magazine de lujo. Elimina el patrón identificable de "fintech genérico". |
