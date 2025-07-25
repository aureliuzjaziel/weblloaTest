#!/usr/bin/env python3
"""
Script para limpiar el CSS eliminando reglas no utilizadas
"""

import re

def main():
    # Leer el archivo CSS actual
    with open('core/static/core/assets/css/templatemo-style.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Clases que definitivamente no se están usando (basado en el análisis)
    unused_classes = [
        'contador-visitas-sidebar',  # No se usa en el HTML
    ]
    
    # Crear expresiones regulares para eliminar estas clases
    for class_name in unused_classes:
        # Patrón para encontrar la regla CSS completa
        pattern = rf'\.{re.escape(class_name)}\s*{{[^}}]*}}'
        css_content = re.sub(pattern, '', css_content, flags=re.MULTILINE | re.DOTALL)
    
    # Eliminar líneas vacías múltiples
    css_content = re.sub(r'\n\s*\n\s*\n', '\n\n', css_content)
    
    # Eliminar espacios al final de líneas
    css_content = re.sub(r'[ \t]+$', '', css_content, flags=re.MULTILINE)
    
    print("=== CLASES ELIMINADAS ===")
    for class_name in unused_classes:
        print(f"- .{class_name}")
    
    # Guardar el archivo limpio
    with open('core/static/core/assets/css/templatemo-style-clean.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print(f"\nArchivo limpio guardado como: templatemo-style-clean.css")
    
    # Estadísticas
    original_lines = open('core/static/core/assets/css/templatemo-style.css', 'r', encoding='utf-8').readlines()
    clean_lines = css_content.split('\n')
    
    print(f"Líneas originales: {len(original_lines)}")
    print(f"Líneas después de limpiar: {len(clean_lines)}")
    print(f"Líneas reducidas: {len(original_lines) - len(clean_lines)}")

if __name__ == '__main__':
    main()
