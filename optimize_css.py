#!/usr/bin/env python3
"""
Script completo para optimizar y limpiar el CSS
"""

import re

def optimize_css():
    # Leer el archivo CSS actual
    with open('core/static/core/assets/css/templatemo-style.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    original_length = len(css_content)
    
    print("=== OPTIMIZACIONES APLICADAS ===")
    
    # 1. Eliminar clases no utilizadas
    unused_classes = [
        'contador-visitas-sidebar',  # No se usa en el HTML
    ]
    
    for class_name in unused_classes:
        pattern = rf'\.{re.escape(class_name)}\s*{{[^}}]*}}'
        before = css_content
        css_content = re.sub(pattern, '', css_content, flags=re.MULTILINE | re.DOTALL)
        if len(css_content) != len(before):
            print(f"✓ Eliminada clase no utilizada: .{class_name}")
    
    # 2. Eliminar comentarios innecesarios pero conservar los importantes
    important_comments = [
        'Sentra Template',
        'Paleta de colores',
        'Modal pantalla completa',
        'Responsive Navigation',
        'Sidebar Style',
        'Slider Style',
        'Featured Style',
        'Slick Slider Css',
        'Modal en dos columnas'
    ]
    
    # Eliminar comentarios que no sean importantes
    def should_keep_comment(comment):
        return any(important in comment for important in important_comments)
    
    # Encontrar y filtrar comentarios
    comment_pattern = r'/\*.*?\*/'
    comments = re.findall(comment_pattern, css_content, flags=re.DOTALL)
    comments_removed = 0
    
    for comment in comments:
        if not should_keep_comment(comment) and len(comment.strip()) < 100:
            css_content = css_content.replace(comment, '')
            comments_removed += 1
    
    print(f"✓ Eliminados {comments_removed} comentarios menores")
    
    # 3. Optimizar espacios en blanco
    # Eliminar espacios al final de líneas
    css_content = re.sub(r'[ \t]+$', '', css_content, flags=re.MULTILINE)
    
    # Eliminar líneas vacías múltiples
    css_content = re.sub(r'\n\s*\n\s*\n+', '\n\n', css_content)
    
    # Eliminar espacios innecesarios alrededor de llaves
    css_content = re.sub(r'\s*{\s*', ' {\n', css_content)
    css_content = re.sub(r'\s*}\s*', '\n}\n', css_content)
    
    print("✓ Optimizados espacios en blanco")
    
    # 4. Optimizar propiedades CSS redundantes
    # Buscar propiedades con valores por defecto innecesarios
    redundant_properties = [
        r'position:\s*static;',  # static es el valor por defecto
        r'display:\s*block;\s*(?=.*display:\s*flex)',  # display block seguido de flex
    ]
    
    properties_removed = 0
    for pattern in redundant_properties:
        before = css_content
        css_content = re.sub(pattern, '', css_content, flags=re.IGNORECASE)
        if len(css_content) != len(before):
            properties_removed += 1
    
    if properties_removed > 0:
        print(f"✓ Eliminadas {properties_removed} propiedades redundantes")
    
    # 5. Corregir formato de propiedades para consistencia
    # Asegurar que las propiedades tengan espacios consistentes
    css_content = re.sub(r'([a-zA-Z-]+):\s*([^;]+);', r'\1: \2;', css_content)
    
    print("✓ Formato de propiedades estandarizado")
    
    # 6. Eliminar líneas vacías al final del archivo
    css_content = css_content.rstrip() + '\n'
    
    # Estadísticas finales
    final_length = len(css_content)
    reduction_bytes = original_length - final_length
    reduction_percent = (reduction_bytes / original_length) * 100
    
    # Guardar el archivo optimizado
    with open('core/static/core/assets/css/templatemo-style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print(f"\n=== RESULTADOS ===")
    print(f"Tamaño original: {original_length:,} bytes")
    print(f"Tamaño optimizado: {final_length:,} bytes")
    print(f"Reducción: {reduction_bytes:,} bytes ({reduction_percent:.1f}%)")
    print(f"✓ Archivo CSS optimizado y guardado")

if __name__ == '__main__':
    optimize_css()
