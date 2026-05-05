# Manual de Operaciones: Comandos gstack

Esta guía detalla la funcionalidad y el alcance de cada comando (o "skill") disponible en el ecosistema `gstack`. Estos comandos no son simples scripts; son agentes especializados de Inteligencia Artificial diseñados para mantener el rigor institucional, actuando como miembros de un equipo de desarrollo de software de alto rendimiento.

El proyecto organiza estos roles siguiendo el flujo de trabajo de un "sprint" de desarrollo: **Pensar → Planear → Construir → Revisar → Probar → Lanzar → Reflexionar**.

---

## 📅 1. Planificación y Definición del Producto

*   **`/office-hours`** | **Consultoría Estratégica**: Actúa como un socio de Y Combinator. Te hace preguntas difíciles para redefinir y enfocar la idea de tu producto antes de escribir código.
*   **`/plan-ceo-review`** | **Validación de Negocio (CEO/Fundador)**: Revisa tu plan de diseño y ajusta el alcance del proyecto (expansión o reducción) bajo la óptica de un CEO.
*   **`/plan-eng-review`** | **Manager de Ingeniería**: Define la arquitectura, el flujo de datos, los casos extremos y las pruebas.
*   **`/plan-design-review`** | **Diseñador Senior**: Califica y mejora las decisiones de diseño planificadas.
*   **`/plan-devex-review`** | **Líder de DX**: Evalúa la experiencia del desarrollador (DX) si estás construyendo APIs o herramientas para otros programadores.
*   **`/autoplan`** | **Revisión Automática**: Ejecuta todo el proceso de revisión (CEO, diseño, ingeniería) en un solo paso automático.

---

## 🎨 2. Diseño UI/UX

*   **`/design-consultation`** | **Socio de Diseño**: Crea un sistema de diseño desde cero, propone riesgos creativos y hace mockups.
*   **`/design-shotgun`** | **Generación de Alternativas**: Genera múltiples variantes de interfaces usando IA para que elijas la dirección correcta y la IA aprenda tus gustos.
*   **`/design-html`** | **Ingeniero Front-End**: Convierte los mockups visuales en código HTML/CSS listo para producción y adaptable.

---

## 🔍 3. Revisión de Código y Seguridad

*   **`/review`** | **Auditoría de Código (Staff Engineer)**: Busca fallas ocultas que pasarían las pruebas automáticas, e incluso las arregla.
*   **`/cso`** | **Director de Seguridad**: Auditorías OWASP y modelos de amenazas (STRIDE).
*   **`/investigate`** | **El Depurador**: Encuentra la causa raíz de un problema antes de intentar arreglarlo al azar.
*   **`/design-review` / `/devex-review`** | **Escrutinio Visual y DX**: Revisan lo ya implementado para asegurar calidad visual y de experiencia.

---

## 🧪 4. Pruebas (QA) y Navegación

*   **`/qa` / `/qa-only`** | **Líder de QA**: Controla un navegador real para probar tu aplicación en vivo.
*   **`/browse`** | **Navegación Asistida**: Le da "ojos" al agente IA usando un navegador Chromium real.
*   **`/setup-browser-cookies`** | **Importación de Sesión**: Importa tus cookies (sesiones iniciadas) al navegador del bot.

---

## 🚀 5. Lanzamiento y Mantenimiento

*   **`/ship`** | **Simulación de Producción y Envío**: Sincroniza la rama principal, corre pruebas, audita y abre un Pull Request (PR).
*   **`/land-and-deploy`** | **Aterrizaje y Despliegue**: Fusiona el código y verifica que el despliegue fue exitoso en producción.
*   **`/canary`** | **Vigilancia SRE**: Vigila la aplicación justo después de ser lanzada.
*   **`/benchmark`** | **Pruebas de Rendimiento**: Compara el rendimiento antes y después de los cambios.
*   **`/document-release`** | **Acta de Entrega**: Actualiza automáticamente los archivos de documentación del proyecto.

---

## 🛠 6. Herramientas de Control y Memoria

*   **`/learn`** | **Memoria del Sistema**: Guarda lo que la IA ha aprendido sobre tu proyecto.
*   **`/retro`** | **Análisis de Desempeño**: Retrospectiva semanal con datos de commits, velocidad y salud del código.
*   **`/careful` / `/freeze` / `/guard`** | **Controles de Seguridad**: Evitan que la IA ejecute comandos destructivos o edite archivos fuera del alcance.
*   **`/pair-agent`** | **Colaboración Multi-Agente**: Permite que varios agentes de IA colaboren en el mismo navegador.
*   **`/context-save`** | **Snapshot de Sesión**: Guarda decisiones tomadas para mantener el contexto en futuras sesiones.

---
---

# 🚀 Uso Avanzado de las Skills de gstack

> Esta sección detalla los comportamientos avanzados, modos especiales y flujos encadenados basados en la documentación oficial de gstack.

---

## 🧠 El Gran Ciclo: Cómo Encadenar Skills

Las skills de gstack **se alimentan entre sí**. El output de una es el input de la siguiente. Este es el flujo completo:

```
/office-hours  →  genera design doc
/plan-ceo-review  →  lee ese design doc, ajusta el alcance
/plan-eng-review  →  escribe plan técnico + test plan
/plan-design-review  →  audita el plan visualmente
[Implementación del código]
/review  →  audita el código terminado
/qa  →  toma el test plan de /plan-eng-review automáticamente y prueba en browser
/ship  →  corre pruebas, abre PR, verifica cobertura
/land-and-deploy  →  fusiona, despliega, verifica en producción
/canary  →  monitorea la app en vivo post-deploy
/document-release  →  actualiza todo el README, CHANGELOG, ARCHITECTURE
/retro  →  análisis de la semana completa
```

No son herramientas independientes; son **fases de una línea de ensamblaje de software**.

---

## 🔬 Uso Avanzado por Skill

### `/office-hours` — Dos modos según tu contexto

| Modo | Cuándo usarlo | Qué hace |
|---|---|---|
| **Startup** | Fundando un producto real | 6 preguntas de YC que cuestionan la demanda, el status quo y el wedge mínimo viable |
| **Builder** | Hackathon, proyecto personal | Colaborador entusiasta que busca el ángulo más interesante y rápido de construir |

El design doc resultante se guarda en `~/.gstack/projects/` y es leído automáticamente por `/plan-ceo-review`.

---

### `/plan-ceo-review` — Los 4 modos de alcance

```
SCOPE EXPANSION      → Propone la versión ambiciosa. Ideal para una primera ronda.
SELECTIVE EXPANSION  → Conserva el alcance base pero muestra oportunidades adicionales.
HOLD SCOPE           → Máximo rigor sobre el plan actual. Sin expansiones.
SCOPE REDUCTION      → Encuentra el MVP mínimo. Recorta todo lo demás.
```

**Truco avanzado:** Las decisiones se guardan en `~/.gstack/projects/` y pueden promoverse a `docs/designs/` del repo para que todo el equipo las vea.

---

### `/plan-eng-review` — El flujo Plan-to-QA

Cuando `/plan-eng-review` termina, escribe automáticamente un **test plan** en `~/.gstack/projects/`. Cuando después ejecutes `/qa`, lo recoge sin que tengas que hacer nada. Tu revisión de ingeniería alimenta directamente las pruebas de QA.

También incluye el **Review Readiness Dashboard**:

```
+===================================================+
|           REVIEW READINESS DASHBOARD              |
+===================================================+
| Review          | Runs | Last Run   | Status      |
|-----------------|------|------------|-------------|
| Eng Review      |  1   | 2026-05-04 | CLEAR       |
| CEO Review      |  1   | 2026-05-04 | CLEAR       |
| Design Review   |  0   | —          | —           |
+---------------------------------------------------+
| VERDICT: CLEARED — Eng Review passed              |
+===================================================+
```

---

### `/plan-design-review` — Auditoría en 7 pasadas

Hace 7 pasadas sobre el plan antes de escribir una sola línea de código:

1. **Arquitectura de información** — ¿qué ven primero los usuarios?
2. **Estados de interacción** — loading, error, vacío, éxito
3. **Flujo de usuario** — de dónde viene, a dónde va
4. **AI Slop Risk** — detecta patrones genéricos de IA (gradient heroes, 3-column icon grids)
5. **Alineación con el Design System**
6. **Responsivo y accesibilidad**
7. **Decisiones de diseño sin resolver**

Califica cada dimensión del 0-10. Un `2/10` en "Estados de Interacción" significa que el plan tiene 4 features de UI pero 0 de los 20 estados especificados.

---

### `/design-consultation` — Diseño desde Cero con "Riesgos Creativos"

Va más allá de una paleta de colores. El flujo real:

1. Investiga el mercado — navega y toma screenshots de competidores reales
2. Propone el sistema completo: tipografía, colores, espaciado, movimiento
3. **Separa explícitamente "safe choices" de "creative risks":**

```
SAFE CHOICES (te mantienen legible en tu categoría):
  → Geist para body — tus usuarios ya conocen esta fuente por Vercel

CREATIVE RISKS (donde te diferenciarías):
  → Instrument Serif para headings — nadie en dev tools usa una serif
  → Teal como acento en vez de azul — igual de confiable, más memorable
```

4. Genera una vista previa HTML interactiva de tu producto con el sistema aplicado
5. Escribe `DESIGN.md` y actualiza `CLAUDE.md` — todas las sesiones futuras respetan el sistema

---

### `/design-shotgun` — La Memoria de Gustos

El sistema aprende tus preferencias a lo largo del tiempo. Si consistentemente apruebas diseños minimalistas, sesgará futuras generaciones hacia ese estilo. No es una configuración; emerge de tus aprobaciones.

**Pipeline completo:**
```
/design-shotgun  →  apruebas una variante
/design-html     →  convierte esa variante en HTML de producción
                    (texto refleja en resize, alturas se ajustan al contenido)
```

El HTML usa **Pretext** (15KB, cero dependencias) para layout computado dinámico. No es una demo; es código deployable.

---

### `/review` — Fix-First, No Solo Reportar

`/review` no solo lista problemas; **actúa**:

- **`[AUTO-FIXED]`** — arreglos mecánicos obvios (N+1 queries, dead code, comentarios obsoletos)
- **`[ASK]`** — decisiones ambiguas que requieren tu aprobación (seguridad, race conditions, decisiones de diseño)

También rastreo de **Enum Handlers**: si agregas un nuevo tipo o estado, `/review` traza ese valor a través de **todos** los switch statements y listas de permisos del codebase, no solo en los archivos que tocaste.

**Completeness Gaps:** Si elegiste la solución del 80% y la solución del 100% cuesta menos de 30 minutos de trabajo con IA, te lo avisa.

---

### `/qa` — Los 4 Modos de Prueba

```bash
/qa                             # Diff-aware: lee git diff main, prueba solo las páginas afectadas
/qa https://staging.myapp.com   # Full: exploración sistemática, 5-15 min, 5-10 bugs documentados
/qa --quick                     # Smoke test de 30 segundos: homepage + top 5 nav targets
/qa --regression baseline.json  # Compara contra una línea base anterior
```

**Pruebas de regresión automáticas:** Cuando `/qa` arregla un bug y lo verifica, genera automáticamente un test que captura exactamente ese escenario.

**Para páginas con login:**
```
/setup-browser-cookies  →  importa tus sesiones reales de Chrome/Arc/Brave
/qa                     →  prueba páginas autenticadas normalmente
```

---

### `/browse` — Comandos de Power User

El sistema de referencias `@e1, @e2, @c1` evita selectores CSS frágiles. Usa el árbol de accesibilidad de Chromium (resistente a React/Vue/Svelte hydration y CSP).

```bash
$B snapshot -i          # Toma snapshot con refs interactivos (@e)
$B snapshot -i -C       # Agrega refs de elementos con cursor:pointer (@c) — componentes custom
$B click @e3            # Click por ref (no por selector)
$B handoff "razón"      # Abre Chrome visible para resolver CAPTCHA o MFA
$B resume               # Retoma el control después del handoff
$B disconnect           # Vuelve a modo headless desde GStack Browser
```

**Handoff automático:** Si el browse falla 3 veces seguidas, sugiere automáticamente usar `handoff`.

---

### `/ship` — Bootstrap de Tests y Cobertura

Si tu proyecto **no tiene framework de tests**, `/ship` lo configura desde cero:
1. Detecta tu runtime (Node, Python, Go, etc.)
2. Investiga el mejor framework para tu stack
3. Lo instala y escribe 3-5 tests reales sobre tu código actual
4. Configura CI/CD en GitHub Actions
5. Crea `TESTING.md`

Cada ejecución de `/ship` produce un **Coverage Audit**:
```
Tests: 42 → 51 (+9 nuevos)
Coverage: src/billing/ ██████████ 90%  src/auth/ ████░░░░░░ 40%
```

**Review Gate:** Verifica el Review Readiness Dashboard antes de abrir el PR. Si falta el Eng Review, te pregunta pero no te bloquea.

---

### `/codex` — Segunda Opinión Multi-IA

Usa un modelo completamente diferente (OpenAI Codex CLI) para revisar el mismo diff que Claude. El análisis cruzado es la parte poderosa:

```
OVERLAP: Race condition en payment handler   → ambos lo detectaron (alta confianza)
ÚNICO DE CODEX: Timing attack en tokens     → perspectiva diferente
ÚNICO DE CLAUDE: N+1 query en listing photos → punto ciego de Codex
```

**3 modos:**
- `review` — veredicto PASS/FAIL con severidad P1/P2/P3
- `challenge` — modo adversarial, activamente intenta romper tu código (`xhigh` reasoning)
- `consult` — conversación abierta con continuidad de sesión

---

### `/retro` — Análisis con Datos Reales

No es una reflexión subjetiva. Analiza el historial de Git y produce métricas:

```
Week: 47 commits | +3.2k LOC | 38% test ratio | 12 PRs | peak: 10pm | Streak: 47d

## Alice
12 commits en app/services/. Cada PR bajo 200 LOC — disciplinada.
Oportunidad: test ratio en 12% — vale la pena antes de que billing se complique.

## Bob
3 commits — arregló el N+1 del dashboard. Pequeño pero alto impacto.
Oportunidad: solo 1 día activo — ¿está bloqueado en algo?
```

**`/retro global`** — corre a través de todos tus proyectos y herramientas de IA (Claude Code, Codex, Gemini).

Los snapshots se guardan en `.context/retros/` para mostrar tendencias en el siguiente `/retro`.

---

### `/cso` — Auditoría con Zero-Noise

El CSO tiene 17 exclusiones de falsos positivos configuradas y un gate de confianza de 8/10+. Cada hallazgo incluye un **escenario de exploit concreto**, no solo la vulnerabilidad abstracta.

Cubre OWASP Top 10 completo + modelo de amenazas STRIDE:
- Injection, Broken Auth, Sensitive Data Exposure
- XEE, Broken Access Control, Security Misconfiguration
- XSS, Insecure Deserialization, Known Vulnerabilities, Insufficient Logging

---

### `/autoplan` — Los 6 Principios de Decisión Automática

Cuando `/autoplan` toma decisiones sin preguntarte, usa estos principios codificados:

1. **Preferir completeness** — la solución más completa sobre la más rápida
2. **Respetar patrones existentes** — no inventar nuevos patrones si ya hay uno
3. **Elegir opciones reversibles** — si hay duda, la opción que se puede deshacer
4. **Recordar decisiones pasadas** — si elegiste X antes en un contexto similar, elige X
5. **Diferir lo ambiguo** — si no es claro, guardarlo para el gate de aprobación
6. **Escalar seguridad** — cualquier tema de seguridad siempre llega al gate de aprobación

Solo las **decisiones de gusto** (opciones con puntaje similar, expansiones de scope borderline) llegan al gate final donde tú decides.

---

### `/learn` — Memoria Institucional Compuesta

Las learnings se acumulan en `~/.gstack/projects/$SLUG/learnings.jsonl`. Cada una tiene:
- Score de confianza (0-10)
- Atribución de fuente (qué skill la generó)
- Referencias a archivos del proyecto

Otras skills **buscan automáticamente** los learnings antes de hacer recomendaciones y muestran `"Prior learning applied"` cuando aplican un insight previo.

```bash
/learn          # Ver learnings actuales del proyecto
/learn search   # Buscar un patrón específico
/learn prune    # Eliminar learnings que referencian archivos borrados
/learn export   # Exportar para compartir con el equipo
```

---

## ⚡ Flujos de Sprints en Paralelo (Uso Experto)

gstack está diseñado para correr **10-15 sprints en paralelo** usando Conductor:

```
Worker 1: /office-hours → nueva idea
Worker 2: /review → PR en revisión
Worker 3: Implementando feature
Worker 4: /qa → staging
Workers 5-15: otras ramas, otros features
```

El checkpoint mode continuo (`gstack-config set checkpoint_mode continuous`) hace commits automáticos con prefijo `WIP:` que incluyen decisiones tomadas y trabajo pendiente. Sobrevive crashes y cambios de contexto. `/ship` aplana esos WIP commits antes del PR para que `git bisect` siga funcionando.

---

## 🔐 Modelo de Seguridad del Browser

El agente del sidebar de GStack Browser tiene **5 capas de defensa contra prompt injection**:

| Capa | Mecanismo |
|---|---|
| L1-L3 | Marcado de datos, strip de elementos ocultos, blocklist de URLs |
| L4 | Clasificador ML local de 22MB (no requiere red) en cada página visitada |
| L4b | Claude Haiku revisa la forma completa de la conversación |
| L5 | Canary token — si un sitio logra que Claude lo revele, la sesión termina |
| L6 | Requiere acuerdo de 2 clasificadores antes de bloquear (evita falsos positivos) |

El ícono de escudo en el sidebar muestra el estado en tiempo real (verde/ámbar/rojo).

---

## 🔗 Integración con Greptile (Review Automático de PRs)

Cuando Greptile revisa tus PRs automáticamente, gstack hace **triage inteligente** de sus comentarios en `/ship` y `/review`:

```
[VALID]          → Se agrega a los hallazgos críticos y se arregla antes de mergear
[ALREADY FIXED]  → Se auto-responde al PR reconociendo el catch
[FALSE POSITIVE] → Se confirma contigo, se responde al PR explicando por qué está mal
```

Cada falso positivo confirmado se guarda en `~/.gstack/greptile-history.md`. Futuras corridas auto-saltan ese patrón en tu codebase. `/retro` trackea el batting average de Greptile con el tiempo.
