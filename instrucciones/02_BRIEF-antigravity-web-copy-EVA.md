# BRIEF DE COPY — Reestructuración de evangelistaco.com
## Para Antigravity · Referencia de voz: Adrià Solà Pastor + tono boutique corporativo

**Fecha:** 2026-06-12 · **Alcance:** copy de todas las páginas del sitio actual + nueva sección EVA

---

## 0. REGLAS DE ESCRITURA (aplicar a cada línea de copy)

Antigravity debe aplicar el skill `/humanizer` a todo texto generado antes de entregarlo. Las reglas adicionales específicas para esta firma:

1. **Oraciones cortas con peso propio.** Si una oración necesita una coma para terminar la idea, divide en dos. El modelo es Adrià Solà Pastor: observación primero, implicación después.
2. **Sin adjetivos vacíos.** "Robusto", "holístico", "transformador", "innovador", "de vanguardia" — prohibidos. Si el adjetivo no puede medirse o demostrarse, no va.
3. **Sin regla de tres decorativa.** Tres puntos seguidos que no sean hechos distintos se cortan a uno.
4. **Específico sobre general.** "Diagnóstico en 15 días hábiles con línea base certificada" > "diagnóstico rápido y preciso".
5. **Tono de firma, no de agencia.** El referente es una firma de abogados o una boutique de banca de inversión: confianza sin esfuerzo, sin exclamaciones, sin verbos de marketing.
6. **EVA no se explica — se enuncia.** El referente de copy es como Anthropic presenta Claude o McKinsey menciona a Lilli's: capacidad declarada, sin manuales de uso. Cero menciones de RAG, LangGraph, vectores, Qdrant, modelos de lenguaje, ni arquitectura técnica interna.

---

## 1. ESTRUCTURA DEL SITIO (lo que cambia)

| Sección actual | Estado | Acción |
|---|---|---|
| Navbar | 🔧 | Agregar "EVA" como ítem de navegación entre "Metodología" y "Perspectivas" |
| Hero principal | 🔧 | Reescribir con Software-Led Consulting |
| "La Firma" (bloque de diagnóstico) | 🔧 | Reescribir con 2 ofertas + mención de EVA |
| Metodología (3 pasos) | 🔧 | Ajustar para incluir la capa tecnológica |
| 4 Áreas de Práctica | 🔧 | Reemplazar por 2 especializaciones |
| Nueva página: EVA | 🕳️ | Crear desde cero |
| Perspectivas | ✅ | Sin cambios |
| Footer | 🔧 | Actualizar áreas de práctica a especializaciones |

---

## 2. COPY NUEVO — PÁGINA PRINCIPAL (index.html)

### Hero

**Headline:**
```
Toda empresa tiene datos.
Pocas tienen la inteligencia para actuar sobre ellos antes de que cuesten más.
```

**Subhead:**
```
Evangelista & Co. combina criterio consultivo con un agente de inteligencia
entrenado para la operación manufacturera mexicana. El resultado no es
un reporte. Es una decisión con evidencia detrás.
```

**CTA primario:** `Iniciar diagnóstico`
**CTA secundario:** `Conocer a EVA →`

**Tagline bajo CTAs:**
```
Diagnóstico en 15 días · Resultado verificable · Software-Led Consulting
```

---

### Bloque "La Firma" — copy reescrito

**Título:**
```
Consultoría que diagnostica.
Inteligencia que certifica.
```

**Cuerpo:**
```
La mayoría de los problemas que llegan a la Dirección General ya llevan
meses costando. El margen cayó. La planta no produce lo que debería.
El proveedor falla de forma que nadie puede documentar.

El diagnóstico no es el problema. El problema es no tener la evidencia
para actuar sobre él con certeza.

Trabajamos con dos especializaciones: operaciones con sangrado activo
y preparación para operar como proveedor Tier 2 o Tier 3 en cadenas
de suministro internacionales. En ambos casos, el proceso termina con
una línea base certificada, un delta verificado a 90 días, y la
capacidad instalada para que la Dirección no dependa de nosotros
para mantenerlo.

EVA, nuestro agente de inteligencia, opera en cada proyecto desde
el día uno.
```

---

### Bloque Metodología — copy ajustado

**Título:**
```
Un protocolo. Tres fases. Evidencia en cada paso.
```

**Paso 01 — Diagnóstico**
```
Escuchamos. Preguntamos lo que nadie ha preguntado.
Determinamos la brecha entre dónde está la empresa y
dónde necesita estar — con número y fuente.
```

**Paso 02 — Diseño e implementación**
```
Diseñamos la intervención. La ejecutamos junto al equipo del cliente.
EVA asiste el análisis, organiza la evidencia y advierte cuando
los datos no sostienen una hipótesis.
```

**Paso 03 — Transferencia y control**
```
El cliente se queda con la capacidad, no con la dependencia.
Documentamos, capacitamos y certificamos el cierre.
Lo que entregamos tiene hash. Lo que se acordó al inicio
es lo que se mide al final.
```

---

### Bloque Especializaciones (reemplaza las 4 Áreas de Práctica)

**Título:**
```
Dos especializaciones. Un estándar de evidencia.
```

**Especialización A — Operaciones Verificables**
```
Para la empresa manufacturera que pierde margen y sabe que el problema
está en la operación, pero no dónde exactamente.

Trabajamos sobre OEE, merma, capital de trabajo y cadena de suministro.
El diagnóstico certifica la pérdida actual. La intervención tiene
90 días para moverla. El delta se mide con la misma fuente que lo midió
al inicio.
```

**Especialización B — Nearshoring Readiness**
```
Para el proveedor que quiere calificar ante una manufactura internacional,
y para la empresa ancla que necesita que su base de proveedores no falle.

Diseñamos la estructura, acompañamos la certificación y entregamos
un expediente auditable. El Tier 1 puede compartirlo con su cliente.
El Tier 2 puede mostrarlo en su siguiente negociación.
```

**Nota bajo las especializaciones:**
```
El punto de entrada es siempre el mismo: un Snapshot D0.
Diagnóstico de precio fijo. Alcance cerrado. 15 días hábiles.
```

---

### Bloque de cierre / contacto

**Título:**
```
El diagnóstico empieza con una conversación.
```

**Cuerpo:**
```
No enviamos propuestas genéricas. El primer paso es entender
si el problema que tiene su empresa es el tipo de problema
que sabemos resolver.

Si lo es, le decimos cómo y a qué costo.
Si no lo es, se lo decimos igual.
```

**CTA:** `Hablar con la firma`

---

## 3. COPY NUEVO — PÁGINA EVA (página dedicada: /eva)

> Esta es la pieza más importante del brief. El referente de voz es doble:
> — Anthropic al lanzar Claude: capacidad declarada con precisión, sin exceso de promesa
> — McKinsey al hablar de Lilli's: ventaja competitiva interna que se menciona sin documentar su arquitectura
>
> Tono: declarativo, sin artificios. Cada párrafo debe poder leerse en voz alta sin sonar a marketing.

### Hero de la página EVA

**Eyebrow (pequeño, sobre el headline):**
```
Evangelista Intelligence
```

**Headline:**
```
EVA
```

**Subhead:**
```
El agente de inteligencia de Evangelista & Co.
Entrenado sobre la realidad operativa de la empresa manufacturera mexicana.
```

**No hay CTA aquí. La página respira.**

---

### Bloque 1 — Qué es EVA (sin explicar cómo funciona)

**Sin título. Copy directo:**
```
Cada firma tiene criterio. Lo que distingue el criterio de la opinión
es la evidencia que lo respalda.

EVA es el sistema con el que Evangelista & Co. organiza, recupera
y aplica ese conocimiento en cada proyecto. Opera desde el primer
día del diagnóstico. No reemplaza el juicio del consultor.
Lo hace más difícil de refutar.

Cuando EVA cita un benchmark, tiene fuente y fecha.
Cuando advierte sobre una hipótesis, hay datos detrás.
Cuando el proyecto cierra, todo lo que EVA procesó queda
registrado en el expediente.
```

---

### Bloque 2 — Lo que EVA hace en un proyecto (sin revelar arquitectura)

**Título:**
```
Inteligencia aplicada, no inteligencia exhibida.
```

**Cuerpo:**
```
EVA no produce reportes. Asiste al consultor en las decisiones
que importan: cuándo una hipótesis tiene suficiente evidencia
para avanzar, cuándo los datos contradicen el diagnóstico inicial,
cuándo el patrón que aparece en este proyecto apareció antes
en otro contexto similar.

Cada conversación con EVA dentro de un proyecto queda registrada.
EVA recuerda lo que se discutió, lo que se descartó y por qué.
Al cierre, ese historial forma parte del expediente que el cliente recibe.

Lo que el cliente ve es el resultado. EVA es la razón
por la que ese resultado llega con evidencia trazable.
```

---

### Bloque 3 — Posicionamiento de mercado (el momento McKinsey/Anthropic)

**Título:**
```
El mercado no necesita más herramientas de IA.
Necesita criterio que las use bien.
```

**Cuerpo:**
```
Las firmas grandes tienen agentes de inteligencia. McKinsey tiene Lilli's.
Operan sobre corpus propietarios construidos en décadas de proyectos.

EVA opera sobre el corpus de operaciones manufactureras en México:
cómo funciona un ERP en una PyME de 200 empleados, qué significa
una variación de merma en una planta textil de Puebla, cómo leer
el estado de cuenta de CONTPAQi cuando el contador lleva diez años
registrando lo mismo de forma distinta.

Ese es el conocimiento que ningún modelo general tiene.
Y es el conocimiento que EVA aplica desde el día uno de cada proyecto.
```

---

### Bloque 4 — Cierre de la página EVA

**Sin título:**
```
EVA no está disponible como producto independiente.
Opera exclusivamente dentro de los proyectos de Evangelista & Co.

Es la razón por la que nuestros diagnósticos tienen fuente
y nuestros resultados tienen hash.
```

**CTA único:**
```
Conocer cómo trabajamos →   [link a /metodologia]
```

---

## 4. AJUSTES DE NAVEGACIÓN

```
Navbar actual:    La Firma / Metodología / Áreas de Práctica / Perspectivas / Acceso
Navbar nuevo:     La Firma / Metodología / EVA / Perspectivas / Acceso
```

Footer — "Áreas de Práctica" se renombra "Especializaciones" con dos ítems:
- Operaciones Verificables
- Nearshoring Readiness

---

## 5. CRITERIOS DE ACEPTACIÓN

### Copy (verificar con humanizer antes de entregar)
- [ ] Cero adjetivos vacíos: "robusto", "holístico", "transformador", "innovador", "de vanguardia", "integral".
- [ ] Cero menciones de tecnología interna de EVA: RAG, LangGraph, Qdrant, vectores, embeddings, LLM, modelo.
- [ ] Cero "regla de tres" decorativa.
- [ ] Cada párrafo del cuerpo: máximo 4 oraciones. Si supera, dividir.
- [ ] El copy de EVA debe poder leerse sin sonar a ficha de producto de software.
- [ ] La frase "Software-Led Consulting" aparece exactamente una vez en el sitio (hero o bloque metodología).

### Estructura
- [ ] Las 4 áreas de práctica reemplazadas por 2 especializaciones en todos los archivos.
- [ ] Página `/eva` creada con las 4 secciones en el orden del brief.
- [ ] Navbar actualizado con "EVA".
- [ ] Links internos del hero a `/eva` funcionando.
- [ ] Footer actualizado.

### Tono (revisión final)
- [ ] Leer el copy de EVA en voz alta. Si suena a landing page de SaaS: reescribir.
- [ ] Leer el hero en voz alta. Si suena a agencia de marketing: reescribir.
- [ ] El copy de la firma completo debe sonar a alguien que no necesita convencerte — solo informarte.
