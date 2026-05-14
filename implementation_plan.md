# Plan de Implementación: Rediseño Integral de Lenguaje y Declaración C-Level

Este plan detalla la reestructuración completa de la narrativa, declaraciones y lenguaje del ecosistema digital de Evangelista & Co. Se transiciona de una oferta de servicios hacia una postura de **Inteligencia Forense y Certeza Estratégica**, adoptando un tono "Wartime" diseñado para conectar con Directores Generales y Consejos de Administración.

## User Review Required

> [!IMPORTANT]
> **Pivote Narrativo:** Se eliminará cualquier vestigio de "servicios IT" o "consultoría de software". La nueva declaración se centra en la **Recuperación de Capital** y la **Mitigación de Riesgos Operativos**.

> [!WARNING]
> **Tono Wartime:** El lenguaje será directo y confrontativo (ej: "Sus reportes mienten"). Este cambio es intencional para filtrar prospectos y posicionar a la firma como un aliado de alto nivel en tiempos de crisis de margen.

### 1. Reestructuración de la Declaración Maestra (Home)

#### [MODIFY] [index.html](file:///Volumes/Adriel-SSD/Evangelista%20&%20Co/evangelista-web-main/index.html)
- **Hero:** Cambiar el foco de "Gobernanza" a "Detección de Fugas de Capital".
- **Headline:** "¿Sabe exactamente dónde está perdiendo dinero hoy?" o similar ≤ 8 palabras.
- **Tesis Operativa:** Reforzar el concepto de "Auditoría Forense" vs "Visualización de Datos".

### 2. Profundidad por Sector (Vectores de Ineficiencia)

#### [MODIFY] [index.html](file:///Volumes/Adriel-SSD/Evangelista%20&%20Co/evangelista-web-main/index.html) y [sectores.html](file:///Volumes/Adriel-SSD/Evangelista%20&%20Co/evangelista-web-main/sectores.html)
- Refinar los "Vectores de Ineficiencia" con lenguaje más punzante y números crudos.
- **Manufactura:** "Hemofilia en piso de producción".
- **Retail:** "Capital atrapado en inventario inexistente".

### 3. Rediseño de Páginas de Respaldo

#### [MODIFY] [metodologia.html](file:///Volumes/Adriel-SSD/Evangelista%20&%20Co/evangelista-web-main/metodologia.html)
- Cambiar "Nuestra Metodología" por "Protocolo de Intervención Forense".
- Enfatizar las 3 fases ALCOA+ como un proceso de auditoría, no de desarrollo.

#### [MODIFY] [por-que-nosotros.html](file:///Volumes/Adriel-SSD/Evangelista%20&%20Co/evangelista-web-main/por-que-nosotros.html)
- Redefinir la identidad de la firma: de "Consultores" a "Socios de Inteligencia Estratégica".
- Eliminar descripciones operativas de los pilares.

### 4. Coherencia en CTAs y Micro-copy

#### [MODIFY] Todos los archivos HTML
- Reemplazar todos los "Contacto" o "Agendar" por "Iniciar Evaluación de Vetting" o "Solicitar Diagnóstico Ejecutivo".
- Asegurar que el disclaimer de "Acceso Restringido" esté presente en todos los puntos de conversión.

## Verification Plan

### Automated Tests
- Ejecutar `/qa` para verificar que la navegación y los CTAs del nuevo Vetting Protocol funcionen correctamente.
- Verificar el rendimiento con Lighthouse para asegurar que no hay regresiones por el contenido expandido.

### Manual Verification
- Revisión visual de los nuevos headlines en dispositivos móviles (responsividad de clamp() en h1).
- Verificación del tono del copy contra el documento maestro `skills/10-elite-corporate-voice.md`.
