# Evangelista & Co. — Rediseño Discursivo del Sitio Web
## Brief de Implementación para Agente

> **Alcance**: Cambio de copy (texto) únicamente. El diseño visual, colores, tipografía, imágenes y estructura de layout se mantienen intactos. Solo se reemplazan los textos. Donde se indique, puede haber ajustes menores de estructura (renombrar secciones, ajustar CTAs).

---

## 1. Contexto del Proyecto

Evangelista & Co. es una firma de **Consultoría e Inteligencia de Negocio** organizada por áreas de práctica. La consultoría es el vínculo con el cliente — el diagnóstico, el criterio, la relación. El Business Intelligence es la disciplina técnica central que soporta ese trabajo. Ambas son inseparables en el modelo de la firma.

El modelo funciona por proyecto: el cliente llega con un objetivo o problema, la firma escucha, diagnostica y propone una solución a la medida. La ejecución puede involucrar consultoría pura, diseño e implementación de arquitectura de datos, desarrollo de software, gestión de procesos, o cualquier combinación que el objetivo requiera. Un proyecto puede ser exclusivamente de consultoría; otro puede ser exclusivamente técnico; la mayoría integra ambas disciplinas.

Las cuatro áreas de práctica son:
- Supply Chain & Operations
- Industrial & Manufacturing
- Growth & Commercial Analytics
- Risk & Financial Integrity

El objetivo del rediseño discursivo es comunicar este modelo con claridad, autoridad y persuasión — sin listar entregables específicos (el alcance siempre varía por proyecto) y sin métricas autodeclaradas.

---

## 2. Guía de Tono y Voz

El copy debe combinar dos registros de manera simultánea:

### Persuasivo (estilo Adrià Solà Pastor)
- Abre cada sección con una **observación** que el lector ya tiene en mente pero no ha articulado
- Usa párrafos cortos. Una idea por párrafo
- Nunca vende el servicio directamente — describe la situación del cliente
- El lector debe reconocerse antes de que se le ofrezca algo
- Sin jargon técnico en el copy principal (el detalle técnico va en Metodología)
- Frases que aterrizan como verdades, no como promesas

### Institucional (estilo Deloitte)
- Registro profesional, nunca informal
- "La firma" como entidad, no como individuo
- Estructura clara: secciones bien definidas, jerarquía consistente
- Sin superlativos ni hipérboles
- Las afirmaciones son precisas o no se hacen

### Lo que NUNCA debe aparecer
- Métricas de resultados autodeclaradas (ej: "$3.5M recuperados")
- Listas de entregables específicos por servicio
- Lenguaje de urgencia artificial
- Jerga técnica en el copy de entrada (ETL, DAX, Monte Carlo van solo en Metodología)
- "Protocolo de Vetting" como CTA principal

---

## 3. Cambios Globales — Navegación

Aplicar en **todas las páginas** del sitio.

### Menú principal (desktop y móvil)

| Ítem actual | Ítem nuevo |
|---|---|
| La Firma | La Firma |
| Metodología | Metodología *(sin cambio)* |
| Sectores | Áreas de Práctica |
| Perspectivas | Perspectivas *(sin cambio)* |
| Tableros C-Level | Acceso *(o mantener si es un link externo)* |
| Admisión | Contacto |

### CTA global del nav (botón derecho)
- **Actual**: `Admisión`
- **Nuevo**: `Hablar con la firma`

---

## 4. Página: `index.html` — Homepage

---

### 4.1 — Tag sobre el hero

- **Actual**: `Para Directores Generales`
- **Nuevo**: `Consultoría e Inteligencia de Negocio para empresa privada mexicana`

---

### 4.2 — Hero: Titular principal (H1)

- **Actual**: "Gestionar por intuición es un riesgo que el capital ya no puede financiar."
- **Nuevo**:

```
Toda empresa sabe a dónde quiere llegar.
No todas tienen el criterio y la inteligencia para llegar más rápido.
```

---

### 4.3 — Hero: Subtítulo / párrafo de apoyo

- **Actual**: "Donde termina la consultoría de gestión tradicional, comienza la eficiencia del capital. Reemplazamos la incertidumbre operativa con un escrutinio institucional auditable que protege su margen neto ante el Consejo de Administración."
- **Nuevo**:

```
Las decisiones que definen el rumbo de su empresa se toman todos los días.
Algunas se toman bien. Otras se toman con información incompleta,
con criterio insuficiente, o sin los datos que las respalden.

Evangelista & Co. es la firma que aporta ambas cosas:
el criterio consultivo para diagnosticar el problema real,
y la inteligencia de negocio para resolverlo con precisión.
```

---

### 4.4 — Hero: CTAs

| CTA actual | CTA nuevo |
|---|---|
| `Iniciar Protocolo de Vetting` (primario) | `Hablar con la firma` (primario) |
| `Conocer Metodología` (secundario) | `Conocer nuestra metodología` (secundario) |

---

### 4.5 — Hero: Métricas / estadísticas

**Eliminar completamente** el bloque de métricas actual:
- ~~$3.5M+ Margen Recuperado~~
- ~~100% Rigor ALCOA+~~
- ~~<10 días Primer Dictamen~~

No reemplazar con otras métricas. Si el layout requiere un elemento en ese espacio, usar la siguiente línea de texto simple:

```
Proyectos a la medida · Equipo propio · Resultado verificable
```

---

### 4.6 — Sección "La Firma" (descripción central)

**Título actual**: *(variaciones de "Orquestación única para problemas estructurales")*
**Título nuevo**:

```
Consultoría que diagnostica.
Inteligencia que lo resuelve.
```

**Cuerpo actual**: *(texto sobre "arquitectura de inteligencia", "mandato de responsabilidad", etc.)*
**Cuerpo nuevo**:

```
La mayoría de los problemas operativos que llegan a la Dirección General
tienen dos capas. La primera es visible: el inventario no cuadra,
el margen bajó, la planta no produce lo que debería.

La segunda no: por qué ocurre, dónde exactamente, y qué decisión
lo puede resolver antes de que cueste más.

La consultoría encuentra las dos capas. El Business Intelligence
le da a la empresa la capacidad de actuar sobre ellas — hoy y en adelante.

Eso es lo que hacemos.
```

---

### 4.7 — Sección "Modelo de Intervención"

**Renombrar sección a**: `Cómo trabajamos`

#### Paso 01

- **Título actual**: `Diagnóstico / Hemofilia Operativa`
- **Título nuevo**: `Diagnóstico`
- **Cuerpo nuevo**:

```
El cliente llega con un objetivo o un problema.
Nosotros escuchamos, hacemos las preguntas que nadie más ha hecho,
y determinamos la brecha entre dónde está la empresa y dónde necesita estar.

Esto es consultoría en su forma más pura: criterio antes que solución.
El diagnóstico define el alcance. El alcance define el trabajo.
```

#### Paso 02

- **Título actual**: `Extracción / Integración Legacy`
- **Título nuevo**: `Diseño e implementación`
- **Cuerpo nuevo**:

```
Con el diagnóstico claro, diseñamos la solución.
Dependiendo del proyecto, esto puede ser asesoría estratégica,
arquitectura de datos, desarrollo de herramientas, reestructuración de procesos,
o cualquier combinación que el objetivo requiera.

Trabajamos junto al equipo del cliente con nuestros propios consultores.
Cuando el proyecto lo exige, incorporamos recursos especializados
bajo el mismo esquema de responsabilidad única.
```

#### Paso 03

- **Título actual**: `Gobernanza / Certeza Directiva`
- **Título nuevo**: `Transferencia y control`
- **Cuerpo nuevo**:

```
El proyecto tiene un cierre. Ese cierre es el momento en que el cliente
opera con autonomía total sobre lo que construimos juntos —
ya sea un nuevo proceso, una arquitectura de datos, o ambos.

Documentamos, capacitamos y transferimos.
El objetivo no es crear dependencia. Es que la empresa opere mejor
desde el primer día después de que nos retiramos.
```

---

### 4.8 — Sección "Impacto Transversal" → renombrar a "Áreas de Práctica"

**Título de sección actual**: `Arbitraje de ineficiencias por sector`
**Título nuevo**: `Cuatro dominios. Proyectos a la medida de cada objetivo.`

**Párrafo introductorio nuevo** (agregar antes de las tarjetas):

```
Las áreas de práctica son los territorios desde donde se originan los proyectos.
Dentro de cada una, el trabajo puede involucrar consultoría, arquitectura de datos,
desarrollo de herramientas o gestión de procesos — según lo que el objetivo requiera.
```

#### Área 1: Supply Chain & Operations

- **Título actual**: `Manufactura e Industria`
- **Título nuevo**: `Supply Chain & Operations`

- **Subtítulo "Vectores de Ineficiencia" — eliminar etiqueta**, reemplazar contenido por:

```
Hay un momento que conoce cualquier Director General de manufactura
o comercialización.

Ventas confirma un pedido. El almacén dice que no puede responder.
El sistema dice algo distinto. Nadie tiene la misma versión de lo que hay disponible.
```

- **Subtítulo "Resultado de Escrutinio" — cambiar etiqueta a**: `Lo que resolvemos`
- **Contenido**:

```
Trabajamos aquí cuando el objetivo es que su cadena de suministro opere
con una sola versión de la realidad — y que las decisiones de inventario,
abastecimiento y distribución estén respaldadas por información precisa, en tiempo.
```

#### Área 2: Industrial & Manufacturing

- **Título actual**: `Retail y Comercialización`
- **Título nuevo**: `Industrial & Manufacturing`

- **Contenido superior**:

```
Una planta que no mide lo que importa no puede mejorar lo que importa.
```

- **Contenido "Lo que resolvemos"**:

```
Trabajamos aquí cuando el objetivo es elevar la eficiencia operativa:
entender qué produce cada línea, qué detiene cada turno,
y dónde se pierde lo que no debería perderse.
```

#### Área 3: Growth & Commercial Analytics

- **Título actual**: `Construcción y Real Estate`
- **Título nuevo**: `Growth & Commercial Analytics`

- **Contenido superior**:

```
Crecer en ventas no siempre significa crecer en rentabilidad.
La diferencia está en los datos que la mayoría de las empresas
no ha calculado todavía.
```

- **Contenido "Lo que resolvemos"**:

```
Trabajamos aquí cuando el objetivo es entender exactamente qué productos,
clientes y canales generan valor real — y construir la inteligencia comercial
para actuar sobre eso.
```

#### Área 4: Risk & Financial Integrity

- **Título actual**: `Servicios Corporativos`
- **Título nuevo**: `Risk & Financial Integrity`

- **Contenido superior**:

```
Las empresas que más riesgo corren no siempre son las que más problemas tienen.
Son las que menos visibilidad tienen sobre los que ya tienen.
```

- **Contenido "Lo que resolvemos"**:

```
Trabajamos aquí cuando el objetivo es que la Dirección General tenga certeza
sobre la integridad de su información financiera y operativa.
```

---

### 4.9 — Sección "Escrutinio de Impacto" → renombrar a "El resultado"

**Título nuevo**: `Consultoría e Inteligencia al servicio de una sola cosa: su decisión.`

**Eliminar** todas las métricas autodeclaradas:
- ~~$2.3M Recuperado~~
- ~~+18% Margen Bruto~~
- ~~340% ROI~~
- ~~89% Certeza Directiva~~

**Reemplazar con el siguiente bloque de texto**:

```
La consultoría le dice qué está pasando y por qué.
El Business Intelligence le da la infraestructura para saberlo siempre,
no solo cuando contrata un proyecto.

El resultado es Decision Intelligence: su empresa toma decisiones más rápidas,
más informadas y más alineadas con su realidad operativa.

Ese es el objetivo de cada proyecto que tomamos.
```

---

### 4.10 — Testimonio

**Mantener** el formato visual del testimonio. Reemplazar solo el texto:

```
"Durante años tomé decisiones con reportes que mi equipo validaba cada mes.
El problema no era la información — era que nadie tenía el mandato de
verificar si esa información era correcta. Evangelista & Co. fue
la primera firma que llegó a decirnos lo que realmente estaba pasando."

— Director General, grupo comercial, Puebla
```

---

### 4.11 — Sección final de contacto / CTA

**Título actual**: `Sometemos su operación a un escrutinio institucional.`
**Título nuevo**: `Cuéntenos su objetivo.`

**Cuerpo actual**: *(texto sobre "acceso restringido", "riesgo fiduciario", etc.)*
**Cuerpo nuevo**:

```
No necesita tener el problema perfectamente definido.
Necesita saber hacia dónde quiere llevar su empresa.

A partir de ahí, construimos juntos el camino.
```

**CTA actual**: `Iniciar Protocolo de Vetting`
**CTA nuevo**: `Hablar con la firma`

**Texto de apoyo actual**: `Proceso estrictamente confidencial · Sujeto a aprobación directiva`
**Texto nuevo**: `Confidencial · Sin compromiso`

---

### 4.12 — Sección "Oficina Administrativa"

**Título actual**: `Relaciones Corporativas`
**Título nuevo**: `Contacto institucional`

**Cuerpo actual**: *(texto sobre propuestas de alianzas y proveedores)*
**Cuerpo nuevo**:

```
Canal reservado para propuestas de alianzas estratégicas,
asuntos legales y relaciones con proveedores.
Las solicitudes de consultoría por esta vía no serán atendidas.
```

Datos de contacto (email, ubicación, horario): **mantener sin cambios**.

---

## 5. Página: `por-que-nosotros.html` — La Firma

---

### 5.1 — Hero: Titular principal

- **Actual**: `La intuición es un riesgo que el capital no puede financiar.`
- **Nuevo**:

```
Fundamos esta firma sobre una observación
que vimos repetirse en demasiadas empresas.
```

---

### 5.2 — Hero: Subtítulo

- **Actual**: *(texto sobre "árbitro implacable entre lo que sus sistemas reportan")*
- **Nuevo**:

```
Los datos existían. Las herramientas existían.
Pero la consultoría llegaba sin inteligencia, o la inteligencia llegaba sin consultoría.

Ninguna de las dos sola resuelve el problema real.
```

---

### 5.3 — Sección "Nuestra Tesis"

**Título actual**: `El software es un commodity. La certeza es el activo.`
**Título nuevo**: `La consultoría sin inteligencia adivina. La inteligencia sin consultoría no pregunta lo correcto.`

**Cuerpo actual**: *(texto sobre "agencias que instalan licencias", "arquitectura de datos como reestructuración")*
**Cuerpo nuevo**:

```
Hay dos tipos de firma en el mercado.

Las que asesoran: llegan, analizan, entregan un reporte y se van.
El cliente queda con recomendaciones, pero sin la capacidad operativa de ejecutarlas.

Las que implementan: instalan sistemas, construyen dashboards y configuran herramientas.
El cliente queda con tecnología, pero sin el criterio para saber si resuelve el problema real.

Evangelista & Co. no es ninguna de las dos.

Somos la firma que diagnostica con criterio consultivo y ejecuta con rigor técnico.
El proyecto termina cuando el cliente tiene ambas cosas: claridad sobre su operación
y la inteligencia instalada para mantenerla.
```

---

### 5.4 — Sección "Filtro de Admisión" → renombrar a "Cómo operamos"

**Título actual**: `Operamos bajo una estricta gobernanza de la verdad.`
**Título nuevo**: `Una firma. Un equipo. Un responsable.`

**Párrafo introductorio nuevo**:

```
Cada proyecto de Evangelista & Co. opera bajo un único esquema
de responsabilidad. Nuestros consultores trabajan en conjunto con
el equipo del cliente. Cuando el proyecto requiere capacidades
especializadas, las incorporamos bajo el mismo marco de trabajo.

El cliente no gestiona múltiples proveedores ni coordina equipos
que no se conocen. Trabaja con una firma que toma la responsabilidad
completa del resultado.
```

---

### 5.5 — Los cuatro principios

Mantener la estructura visual de los cuatro bloques. Reemplazar títulos y cuerpos:

#### Principio 01

- **Título actual**: `Honestidad Radical`
- **Título nuevo**: `Honestidad sobre el diagnóstico`
- **Cuerpo nuevo**:

```
Si el problema que el cliente nos presenta no es el problema real,
lo decimos. La solución correcta empieza por el diagnóstico correcto.
```

#### Principio 02

- **Título actual**: `Rigor Secuencial`
- **Título nuevo**: `Rigor antes que velocidad`
- **Cuerpo nuevo**:

```
No construimos sobre bases que no hemos verificado.
Si la integridad del dato no está garantizada, el proyecto no avanza.
Los cimientos siempre preceden a la estrategia.
```

#### Principio 03

- **Título actual**: `Arbitraje Objetivo`
- **Título nuevo**: `Independencia de criterio`
- **Cuerpo nuevo**:

```
No somos parte del equipo del cliente. Somos su contraparte técnica.
Eso nos permite ver lo que la operación diaria no permite ver.
```

#### Principio 04

- **Título actual**: `Soberanía del Cliente`
- **Título nuevo**: `Inteligencia transferida`
- **Cuerpo nuevo**:

```
Cada proyecto termina con el cliente en control total.
No creamos dependencias. Creamos capacidades.
```

---

### 5.6 — Sección del Fundador

**Título actual**: `El Managing Partner`
**Título nuevo**: `El Managing Partner` *(sin cambio)*

**Cita actual**: `"Para decidir, hay que saber; y para saber, hay que observar con rigor implacable. Nosotros somos el escrutinio que expone su verdad operativa."`

**Cita nueva**:

```
"La consultoría te dice qué está mal. La inteligencia te dice por qué,
y te da la capacidad de verlo siempre. Construimos esta firma
para que nuestros clientes tengan las dos cosas."

— Adriel Evangelista, Managing Partner
```

**Cuerpo actual**: *(texto sobre "falla sistémica", "agencia tecnológica", "erradicar la entropía")*
**Cuerpo nuevo**:

```
Fundé Evangelista & Co. al identificar una brecha sistemática en el mercado:
las firmas de consultoría llegaban con criterio pero sin capacidad técnica.
Las empresas de tecnología llegaban con herramientas pero sin criterio de negocio.

El resultado en ambos casos era el mismo: el cliente gastaba,
pero el problema seguía ahí o regresaba en seis meses.

La firma nació para cerrar esa brecha. Consultoría e Inteligencia de Negocio
no son dos servicios que ofrecemos — son dos disciplinas que operamos
de manera integrada en cada proyecto que tomamos.
```

**CTA al final de la página**:
- **Actual**: `Iniciar Proceso de Admisión`
- **Nuevo**: `Hablar con la firma`

---

## 6. Página: `metodologia.html` — Metodología

---

### 6.1 — Tag sobre el hero

- **Actual**: `Protocolo de Intervención`
- **Nuevo**: `Cómo trabajamos`

---

### 6.2 — Hero: Titular principal

- **Actual**: `El rigor técnico detrás de la rentabilidad.`
- **Nuevo**:

```
Consultoría que diagnostica.
Inteligencia que ejecuta.
Un solo proceso.
```

---

### 6.3 — Hero: Subtítulo

- **Actual**: *(texto sobre "certidumbre financiera como resultado de diseño estructural")*
- **Nuevo**:

```
Cada proyecto integra dos disciplinas desde el primer día:
el criterio consultivo para entender el problema real,
y la inteligencia de negocio para resolverlo con precisión.
El alcance varía. El proceso, no.
```

---

### 6.4 — Fase 01: Foundation → renombrar

- **Nombre actual**: `Foundation / Auditoría Forense`
- **Nombre nuevo**: `01 — Diagnóstico`

- **Cuerpo de mecánica técnica — mantener estructura visual**, reemplazar texto introductorio:

```
Todo proyecto comienza con una conversación.
El cliente nos cuenta su objetivo o su problema.
Nosotros hacemos las preguntas que nadie más ha hecho.

De ahí surge el diagnóstico: una lectura precisa de la brecha
entre dónde está la empresa hoy y dónde necesita estar.
El diagnóstico define el alcance. El alcance define el trabajo.
```

- Los bullet points técnicos internos (Dictamen de madurez, Mapeo de topología, ALCOA+) **pueden mantenerse o eliminarse** según el diseño. Si se mantienen, cambiar la etiqueta de `Mecánica Técnica` a `Lo que implica`.

---

### 6.5 — Fase 02: Architecture → renombrar

- **Nombre actual**: `Architecture / Gobierno de Datos`
- **Nombre nuevo**: `02 — Diseño e implementación`

- **Cuerpo introductorio nuevo**:

```
Una vez definido el diagnóstico, diseñamos la solución.
Esto puede involucrar arquitectura de datos, desarrollo de herramientas,
reestructuración de procesos, o cualquier combinación que el objetivo requiera.

Trabajamos junto al equipo del cliente. Aportamos nuestros consultores y,
cuando el proyecto lo exige, incorporamos recursos especializados
bajo el mismo esquema de responsabilidad única.
```

---

### 6.6 — Fase 03: Sentinel → renombrar

- **Nombre actual**: `Sentinel / Inteligencia Activa`
- **Nombre nuevo**: `03 — Transferencia y control`

- **Cuerpo introductorio nuevo**:

```
El cierre de un proyecto no es la entrega de un reporte.
Es el momento en que el cliente tiene el control total
de la inteligencia que construimos juntos.

Documentamos, capacitamos y transferimos.
El objetivo no es que el cliente nos necesite para siempre.
Es que opere mejor desde el primer día después de que nos retiramos.
```

- **Nota**: Si el diseño actual muestra referencias a "alertas push/mail" o "Monte Carlo" como bullet técnicos de Sentinel, estos pueden mantenerse como detalle técnico dentro de la sección, bajo la etiqueta `Capacidades disponibles` en lugar de `Mecánica Técnica`.

---

### 6.7 — Sección ALCOA+

**Título actual**: `El protocolo de precisión ALCOA+.`
**Título nuevo**: `El estándar que garantiza la integridad de cada proyecto.`

**Cuerpo introductorio actual**: *(texto sobre FDA y ensayos clínicos)*
**Cuerpo nuevo**:

```
ALCOA+ es el protocolo de integridad de datos desarrollado originalmente
por la FDA para garantizar la validez de la información en ensayos clínicos.
Lo adoptamos como nuestro estándar de referencia para cualquier proyecto
que involucre arquitectura o auditoría de datos.

La razón es directa: una decisión de negocio es tan buena como
la información en que se basa. Si el dato no es íntegro,
la inteligencia que construimos sobre él tampoco lo es.
```

- **El desglose de letras (A, L, C, O, A+)**: mantener estructura visual y definiciones. Solo ajustar si alguna definición usa lenguaje demasiado técnico para el contexto.

---

### 6.8 — CTA final de la página

- **Actual**: `Iniciar Evaluación de Admisión`
- **Nuevo**: `Hablar con la firma`

---

## 7. Página: `sectores.html` → renombrar página a "Áreas de Práctica"

> Actualizar también el `<title>` del HTML y cualquier referencia interna.

---

### 7.1 — Hero: Tag

- **Actual**: *(si existe, "Sectores" o similar)*
- **Nuevo**: `Áreas de Práctica`

---

### 7.2 — Hero: Titular principal

- **Nuevo**:

```
Cuatro dominios de especialización.
Un solo modelo de trabajo.
```

---

### 7.3 — Hero: Subtítulo

- **Nuevo**:

```
Cada área de práctica representa un territorio donde el Business Intelligence
tiene impacto directo sobre la eficiencia y la toma de decisiones de la empresa.
Los proyectos se originan en una de estas áreas. El trabajo siempre
es a la medida del objetivo del cliente.
```

---

### 7.4 — Área 1: Supply Chain & Operations

**Nombre**: `Supply Chain & Operations`

**Cuerpo**:

```
La cadena de suministro es uno de los sistemas más complejos de cualquier empresa.
Involucra múltiples áreas, múltiples sistemas y múltiples equipos que rara vez
comparten la misma información en tiempo real.

Cuando esa información está fragmentada, las consecuencias son visibles:
pedidos que no se cumplen, inventarios que no cuadran, decisiones de compra
que se toman con datos que ya no son válidos.

Trabajamos en este dominio con empresas que quieren que su operación logística
responda con precisión: desde el control de inventario y la predicción de demanda,
hasta la sincronización entre compras, producción y distribución.
```

---

### 7.5 — Área 2: Industrial & Manufacturing

**Nombre**: `Industrial & Manufacturing`

**Cuerpo**:

```
La eficiencia de una planta no se mejora observando. Se mejora midiendo lo correcto.

Muchas operaciones industriales tienen indicadores. Pocas tienen los indicadores
que realmente explican por qué una línea produce menos de lo que debería,
por qué un turno rinde diferente al siguiente, o por qué la merma aparece
en el reporte pero nadie sabe exactamente dónde ocurrió.

Trabajamos en este dominio con empresas que quieren visibilidad real
de su operación: eficiencia por línea y turno, trazabilidad de procesos,
control de producción en tiempo real y benchmarking operativo con causa raíz identificada.
```

---

### 7.6 — Área 3: Growth & Commercial Analytics

**Nombre**: `Growth & Commercial Analytics`

**Cuerpo**:

```
El crecimiento comercial tiene dos velocidades: la del volumen y la de la rentabilidad.
Casi siempre se mide la primera y se asume la segunda.

El resultado es que muchas empresas crecen en ventas sin crecer en utilidad,
porque no tienen la inteligencia para saber exactamente qué vender,
a quién venderle, y cuándo el costo de atender a un cliente supera
el margen que genera.

Trabajamos en este dominio con empresas que quieren construir una estrategia
comercial basada en datos reales: rentabilidad por producto y cliente,
inteligencia de mercado, y modelos que permiten anticipar el comportamiento
comercial antes de que se convierta en un problema.
```

---

### 7.7 — Área 4: Risk & Financial Integrity

**Nombre**: `Risk & Financial Integrity`

**Cuerpo**:

```
La información financiera que llega a la Dirección General casi siempre
ha pasado por varias interpretaciones antes de llegar. Cada área presenta
los números que mejor reflejan su desempeño. No por deshonestidad.
Por inercia organizacional.

El resultado es que la imagen que tiene el Director General de su empresa
puede diferir de lo que sus sistemas registran — y lo que sus sistemas
registran puede diferir de lo que realmente ocurrió.

Trabajamos en este dominio con empresas que necesitan certeza:
auditoría de costos, trazabilidad de capital, cumplimiento preventivo
y monitoreo de salud financiera con visibilidad antes de que el problema
sea difícil de revertir.
```

---

### 7.8 — CTA final de la página

- **Nuevo texto**: `¿Su objetivo está en alguno de estos dominios?`
- **CTA**: `Hablar con la firma`
- **Texto de apoyo**: `Confidencial · Sin compromiso`

---

## 8. Footer — Todas las páginas

### Descripción de la firma (pie de página)

**Actual**:
> "Intelligence Architecture — la convergencia entre Business Intelligence y Arquitectura de Soluciones..."

**Nuevo**:

```
Evangelista & Co. es una firma de consultoría e inteligencia de negocio
organizada por áreas de práctica. Ayudamos a empresas privadas mexicanas
a alcanzar sus objetivos más rápido mediante criterio consultivo
e inteligencia diseñada para su operación específica.
```

### Links de navegación en footer

Actualizar conforme a los cambios de menú:
- `Sectores` → `Áreas de Práctica`
- `Tableros C-Level` → `Acceso` *(o mantener link externo)*
- Cualquier referencia a "Admisión" → `Contacto`

---

## 9. Lo que NO debe cambiar

- Paleta de colores (charcoal, cream, olive, acentos por área)
- Tipografía (Instrument Serif para headers, Inter para body)
- Layout y estructura de secciones
- Imágenes y fotografías
- Logo e isotipo
- Diseño de tarjetas, botones y componentes visuales
- El link externo al tablero Streamlit (Sentinel/Monte Carlo)
- Información de contacto (email, ubicación, horario)
- El bloque ALCOA+ con sus definiciones letra por letra (solo se ajusta el copy introductorio)

---

## 10. Notas técnicas para el agente

1. **Prioridad de implementación**: Empezar por `index.html`, luego `por-que-nosotros.html`, `metodologia.html`, `sectores.html`.

2. **Consistencia de términos clave**: Los siguientes términos deben aparecer de manera consistente en todo el sitio:
   - "Consultoría e Inteligencia de Negocio" — descriptor principal de la firma
   - "Business Intelligence" — disciplina técnica (no usar como único identificador de la firma)
   - "Decision Intelligence" — el resultado final para el cliente
   - "Áreas de práctica" (no "servicios", no "soluciones")
   - "Proyecto" (no "engagement", no "intervención")
   - "Hablar con la firma" — CTA principal estándar

3. **Eliminación de terminología anterior**: Buscar y reemplazar en todo el sitio:
   - ~~"hemofilia operativa"~~ → eliminar
   - ~~"entropía administrativa"~~ → eliminar
   - ~~"escrutinio institucional auditable"~~ → eliminar
   - ~~"Protocolo de Vetting"~~ → eliminar
   - ~~"ficción contable"~~ → eliminar
   - ~~"árbitro implacable"~~ → eliminar
   - ~~"Intelligence Architecture"~~ → reemplazar por "Consultoría e Inteligencia de Negocio"
   - ~~"Foundation"~~ como nombre de servicio → eliminar (mantener solo en contexto ALCOA+)
   - ~~"Architecture"~~ como nombre de servicio → eliminar
   - ~~"Sentinel"~~ como nombre de servicio → eliminar (mantener el link al tablero si existe)

4. **Renombrar `sectores.html`**: Si es posible sin romper links externos, renombrar a `areas-de-practica.html` y redirigir el anterior. Si no, mantener el filename pero cambiar todo el contenido visible y el `<title>`.

5. **Meta descriptions actualizadas**:
   - `index.html`: *"Evangelista & Co. es una firma de consultoría e inteligencia de negocio para empresa privada mexicana. Criterio consultivo e inteligencia de datos para que su empresa tome mejores decisiones, más rápido."*
   - `por-que-nosotros.html`: *"Conoce la firma, nuestra filosofía y el equipo detrás de cada proyecto de consultoría e inteligencia de negocio."*
   - `metodologia.html`: *"Diagnóstico, diseño e implementación, transferencia. El proceso detrás de cada proyecto de Evangelista & Co."*
   - `sectores.html`: *"Supply Chain, Industrial & Manufacturing, Growth & Commercial Analytics, Risk & Financial Integrity. Las cuatro áreas de práctica de Evangelista & Co."*

---

*Brief generado para implementación de rediseño discursivo. Versión 1.1 — Mayo 2026.*
*Evangelista & Co. — Consultoría e Inteligencia de Negocio*
