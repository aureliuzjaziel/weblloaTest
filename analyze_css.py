#!/usr/bin/env python3
"""
Script para analizar el uso de clases CSS en el proyecto
"""

import re
import os

def extract_css_classes(css_file):
    """Extrae todas las clases CSS del archivo"""
    with open(css_file, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Buscar clases CSS (selectores que empiecen con .)
    classes = set()
    
    # Patrones para encontrar clases
    patterns = [
        r'\.([a-zA-Z][a-zA-Z0-9_-]*)',  # .class-name
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, css_content)
        classes.update(matches)
    
    return classes

def extract_html_classes(html_file):
    """Extrae todas las clases usadas en el HTML"""
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Buscar class="..." en el HTML
    classes = set()
    pattern = r'class=["\']([^"\']+)["\']'
    matches = re.findall(pattern, html_content)
    
    for match in matches:
        # Dividir por espacios para clases múltiples
        classes.update(match.split())
    
    return classes

def extract_js_classes(js_file):
    """Extrae clases referenciadas en JavaScript"""
    with open(js_file, 'r', encoding='utf-8') as f:
        js_content = f.read()
    
    classes = set()
    
    # Buscar diferentes patrones de clases en JS
    patterns = [
        r'\.([a-zA-Z][a-zA-Z0-9_-]*)',  # .className
        r'["\']([a-zA-Z][a-zA-Z0-9_-]*)["\']',  # "className"
        r'addClass\(["\']([^"\']+)["\']\)',  # addClass('className')
        r'removeClass\(["\']([^"\']+)["\']\)',  # removeClass('className')
        r'hasClass\(["\']([^"\']+)["\']\)',  # hasClass('className')
        r'toggleClass\(["\']([^"\']+)["\']\)',  # toggleClass('className')
    ]
    
    for pattern in patterns:
        matches = re.findall(pattern, js_content)
        classes.update(matches)
    
    return classes

def main():
    # Archivos a analizar
    css_file = 'core/static/core/assets/css/templatemo-style.css'
    html_file = 'core/templates/core/index.html'
    js_file = 'core/static/core/js/main.js'
    
    print("=== ANÁLISIS DE USO DE CLASES CSS ===\n")
    
    # Extraer clases de cada archivo
    css_classes = extract_css_classes(css_file)
    html_classes = extract_html_classes(html_file)
    js_classes = extract_js_classes(js_file)
    
    # Clases usadas en HTML o JS
    used_classes = html_classes | js_classes
    
    print(f"Clases definidas en CSS: {len(css_classes)}")
    print(f"Clases usadas en HTML: {len(html_classes)}")
    print(f"Clases usadas en JS: {len(js_classes)}")
    print(f"Total clases utilizadas: {len(used_classes)}")
    print()
    
    # Clases CSS no utilizadas
    unused_css_classes = css_classes - used_classes
    
    print("=== CLASES CSS POSIBLEMENTE NO UTILIZADAS ===")
    if unused_css_classes:
        for cls in sorted(unused_css_classes):
            print(f"  .{cls}")
    else:
        print("  Todas las clases CSS están siendo utilizadas")
    
    print()
    
    # Clases HTML que no tienen estilos definidos
    undefined_classes = used_classes - css_classes
    
    print("=== CLASES USADAS SIN ESTILOS DEFINIDOS ===")
    if undefined_classes:
        print("(Estas pueden estar definidas en Bootstrap u otros frameworks)")
        for cls in sorted(undefined_classes):
            print(f"  .{cls}")
    else:
        print("  Todas las clases usadas tienen estilos definidos")
    
    print()
    
    # Estadísticas
    print("=== ESTADÍSTICAS ===")
    print(f"Uso de CSS: {len(css_classes - unused_css_classes)}/{len(css_classes)} ({((len(css_classes - unused_css_classes))/len(css_classes)*100):.1f}%)")
    
    # Mostrar algunas clases comunes que pueden ser frameworks
    framework_classes = [cls for cls in undefined_classes if cls.startswith(('col-', 'fa-', 'btn-', 'form-', 'nav', 'hidden-', 'clearfix', 'container'))]
    if framework_classes:
        print(f"Clases de frameworks detectadas: {len(framework_classes)}")

if __name__ == '__main__':
    main()
