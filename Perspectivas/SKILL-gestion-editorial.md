# SKILL: Gestión de la Plataforma Editorial "Perspectivas"
Este documento define el estándar técnico y estético para la actualización de la sección editorial de Evangelista & Co.

## 1. Flujo de Trabajo para Nuevos Análisis
Cuando el usuario proporcione un nuevo archivo PDF, el asistente debe seguir estos pasos:
1.  Asegurarse de que el archivo esté en `Perspectivas/Analisis (pdf)/`.
2.  Identificar el siguiente número de Perspectiva (Ej: #03, #04).
3.  Redactar un título y descripción corta en tono institucional/técnico (C-Level).
4.  Insertar el código de la tarjeta en `Perspectivas/Perspectivas.html` antes de la tarjeta de "Próximamente".

## 2. Estructura de Código (Template)
Utilizar estrictamente este bloque HTML para mantener la consistencia:

```html
<!-- Análisis [ID] -->
<article class="group bg-white border border-[#1C1C1C] overflow-hidden hover:shadow-[12px_12px_0_0_#5A6352] transition-all duration-300 flex flex-col">
    <div class="p-8 flex-grow">
        <div class="flex justify-between items-start mb-6">
            <span class="bg-[#F4F1EA] text-[#5A6352] text-[10px] font-bold tracking-widest uppercase py-1 px-3">Perspectiva #[ID]</span>
            <span class="text-gray-400 text-xs font-sans">[MES AÑO]</span>
        </div>
        <h2 class="text-2xl font-serif text-[#1C1C1C] mb-4 leading-tight group-hover:text-[#5A6352] transition-colors">
            [TÍTULO DEL ANÁLISIS]
        </h2>
        <p class="text-sm text-gray-600 font-sans leading-relaxed mb-8">
            [RESUMEN EJECUTIVO DE 2-3 LÍNEAS]
        </p>
    </div>
    <div class="px-8 pb-8 space-y-3">
        <!-- Link al Visor Nativo -->
        <a href="visor.html?file=Analisis (pdf)/[ARCHIVO].pdf&title=[TÍTULO ESCAPADO]" class="inline-flex items-center w-full justify-center bg-[#1C1C1C] text-white py-3 px-6 text-[10px] font-bold tracking-widest uppercase hover:bg-[#5A6352] transition-colors duration-300">
            Leer en línea
            <svg class="w-3 h-3 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="square" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path><path stroke-linecap="square" stroke-linejoin="square" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path></svg>
        </a>
        <a href="Analisis (pdf)/[ARCHIVO].pdf" download class="inline-flex items-center w-full justify-center border border-[#1C1C1C] text-[#1C1C1C] py-3 px-6 text-[10px] font-bold tracking-widest uppercase hover:bg-[#F4F1EA] transition-colors duration-300">
            Descargar PDF
            <svg class="w-3 h-3 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="square" stroke-width="2" d="M7 16l5 5m0 0l5-5m-5 5V3"></path></svg>
        </a>
    </div>
</article>
```

## 3. Reglas de Diseño y Estilo
*   **Colores Institucionales:**
    *   Olive (Primario): `#5A6352`
    *   Carbon (Texto/Bordes): `#1C1C1C`
    *   Beige (Fondo): `#F4F1EA`
*   **Tipografía:**
    *   Títulos: Serif (Fraunces/Georgia).
    *   Cuerpo/UI: Sans-serif (DM Sans).
*   **Sombra de Tarjeta:** Siempre debe ser `hover:shadow-[12px_12px_0_0_#5A6352]` para mantener el estilo "brutalista institucional".

## 4. Configuración del Visor
El enlace "Leer en línea" debe usar obligatoriamente `visor.html` con dos parámetros:
1.  `file`: Ruta relativa al PDF desde la carpeta `Perspectivas/`.
2.  `title`: Título del análisis (URL encoded) para que aparezca en el encabezado del visor.

---
*Manual actualizado el 13 de Mayo, 2026.*
