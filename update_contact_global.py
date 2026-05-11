import os

contact_html = """
<!-- ══════════════════════════════════════════ Sección 5: Contacto (Sólo Info) -->
<section id="contacto" class="border-t border-[#5A6352]/20 bg-[#F4F1EA]">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
    <div class="flex flex-col md:flex-row justify-between items-center gap-8">
      <div>
        <span class="text-[#5A6352] text-xs font-bold tracking-[0.2em] uppercase mb-2 block">Oficina Administrativa</span>
        <h2 class="text-3xl font-serif text-[#1C1C1C]">Relaciones Corporativas.</h2>
      </div>
      <div class="flex flex-col md:flex-row gap-8 md:gap-16 font-sans text-sm">
        <div class="flex flex-col">
          <span class="text-[#5A6352] font-bold uppercase tracking-wide mb-1">Email</span>
          <a href="mailto:info@evangelistaco.com" class="text-gray-800 hover:text-[#5A6352] transition-colors">info@evangelistaco.com</a>
        </div>
        <div class="flex flex-col">
          <span class="text-[#5A6352] font-bold uppercase tracking-wide mb-1">Operación</span>
          <span class="text-gray-800">Puebla, Pue. | Ciudad de México</span>
        </div>
      </div>
    </div>
  </div>
</section>
"""

files = ['index.html', 'metodologia.html', 'por-que-nosotros.html', 'sectores.html']

for filename in files:
    with open(filename, 'r') as f:
        content = f.read()
    
    # Remove old contact/admision sections (common patterns)
    import re
    content = re.sub(r'<!-- ══════════════════════════════════════════ Sección 5: Contacto -->.*?<footer', '<footer', content, flags=re.DOTALL)
    content = re.sub(r'<section id="admision".*?/section>', '', content, flags=re.DOTALL)
    
    # Insert the new clean contact info before footer
    if '<footer' in content:
        content = content.replace('<footer', contact_html + '\n<footer')
    
    # Update footer links to #contacto
    content = content.replace('href="#admision"', 'href="#contacto"')
    content = content.replace('href="index.html#admision"', 'href="index.html#contacto"')
    
    with open(filename, 'w') as f:
        f.write(content)

print("Global contact info updated.")
