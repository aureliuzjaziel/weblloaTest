#!/usr/bin/env python3
"""
Script para corregir sintaxis CSS: espacios antes de pseudoselectores
"""

import re

def fix_css_syntax():
    # Leer el archivo CSS
    with open('core/static/core/assets/css/templatemo-style.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    print("=== CORRIGIENDO SINTAXIS CSS ===")
    
    # Corregir espacios antes de pseudoselectores
    patterns = [
        (r'(\w+)\s*:\s*(hover|focus|active|before|after|first-child|last-child|nth-child)', r'\1:\2'),
        (r'([^{:;])\s*:\s*(hover|focus|active|before|after)\s*{', r'\1:\2 {'),
        (r'([^{:;])\s*:\s*(hover|focus|active|before|after)\s*([^{]*){', r'\1:\2\3 {'),
    ]
    
    fixes_made = 0
    for pattern, replacement in patterns:
        before = css_content
        css_content = re.sub(pattern, replacement, css_content, flags=re.IGNORECASE)
        if len(css_content) != len(before):
            fixes_made += 1
    
    # Corregir específicamente los casos problemáticos encontrados
    specific_fixes = [
        ('nav a: hover', 'nav a:hover'),
        ('nav a: before', 'nav a:before'),
        ('nav a: focus', 'nav a:focus'),
        ('nav a: active', 'nav a:active'),
        ('li: hover', 'li:hover'),
        ('item: hover', 'item:hover'),
        ('button: focus', 'button:focus'),
        ('span: hover', 'span:hover'),
        ('logo: hover', 'logo:hover'),
        ('NextArrow: before', 'NextArrow:before'),
        ('PrevArrow: before', 'PrevArrow:before'),
    ]
    
    for old, new in specific_fixes:
        if old in css_content:
            css_content = css_content.replace(old, new)
            fixes_made += 1
            print(f"✓ Corregido: {old} → {new}")
    
    # Guardar el archivo corregido
    with open('core/static/core/assets/css/templatemo-style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    print(f"\n=== RESULTADO ===")
    print(f"✅ {fixes_made} correcciones aplicadas")
    print("✅ Sintaxis CSS corregida - Las animaciones de botones ahora funcionarán correctamente")

if __name__ == '__main__':
    fix_css_syntax()
