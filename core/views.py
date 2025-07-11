from django.shortcuts import render, HttpResponse
from places.models import Place
from blog.models import BlogEntry
from collections import defaultdict
from datetime import datetime
import locale

# Diccionario para traducir meses al español
MONTHS_SPANISH = {
    'January': 'Enero', 'February': 'Febrero', 'March': 'Marzo',
    'April': 'Abril', 'May': 'Mayo', 'June': 'Junio',
    'July': 'Julio', 'August': 'Agosto', 'September': 'Septiembre',
    'October': 'Octubre', 'November': 'Noviembre', 'December': 'Diciembre'
}

# Create your views here.
def home(request): 
    places = Place.objects.all()
    blog_entries = BlogEntry.objects.filter(is_published=True).order_by('-published_date', '-created_date')
    
    # Organizar entradas por mes y año
    months_data = []
    processed_months = set()
    
    for entry in blog_entries:
        # Usar published_date si existe, sino created_date
        date_to_use = entry.published_date if entry.published_date else entry.created_date
        
        # Crear key para el mes (ejemplo: "2025-07" para Julio 2025)
        month_key = date_to_use.strftime("%Y-%m")
        
        # Crear display en español
        month_name_en = date_to_use.strftime("%B")
        month_name_es = MONTHS_SPANISH.get(month_name_en, month_name_en)
        year = date_to_use.year
        month_display = f"{month_name_es} {year}"
        
        if month_key not in processed_months:
            # Obtener todas las entradas de este mes
            month_entries = []
            for e in blog_entries:
                e_date = e.published_date if e.published_date else e.created_date
                if e_date.strftime("%Y-%m") == month_key:
                    month_entries.append(e)
            
            months_data.append({
                'key': month_key,
                'display': month_display,
                'entries': month_entries,
                'date_obj': date_to_use
            })
            processed_months.add(month_key)
    
    # Ordenar meses por fecha (más reciente primero)
    months_data.sort(key=lambda x: x['date_obj'], reverse=True)
    
    return render(request,'core/index.html',{
        'places': places,
        'blog_entries': blog_entries,
        'months_data': months_data
    })
