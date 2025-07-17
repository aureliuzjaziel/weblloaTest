from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse
from .models import BlogEntry

# Create your views here.

def blog_list(request):
    """Vista para mostrar todas las entradas del blog publicadas"""
    blog_entries = BlogEntry.objects.filter(is_published=True)
    return render(request, 'blog/blog_list.html', {'blog_entries': blog_entries})

def blog_detail(request, pk):
    """Vista para mostrar una entrada específica del blog"""
    blog_entry = get_object_or_404(BlogEntry, pk=pk, is_published=True)
    return render(request, 'blog/blog_detail.html', {'blog_entry': blog_entry})

@staff_member_required
def blog_stats(request):
    """Vista para mostrar estadísticas del blog"""
    published_count = BlogEntry.objects.filter(is_published=True).count()
    unpublished_count = BlogEntry.objects.filter(is_published=False).count()
    total_count = BlogEntry.objects.count()
    
    # Obtener las entradas más recientes
    recent_published = BlogEntry.objects.filter(
        is_published=True
    ).order_by('-published_date', '-created_date')[:5]
    
    # Verificar si hay entradas que excedan el límite
    excess_entries = BlogEntry.objects.filter(
        is_published=True
    ).order_by('-published_date', '-created_date')[5:]
    
    context = {
        'published_count': published_count,
        'unpublished_count': unpublished_count,
        'total_count': total_count,
        'recent_published': recent_published,
        'excess_entries': excess_entries,
        'limit_reached': published_count >= 5,
        'over_limit': published_count > 5,
    }
    
    return render(request, 'blog/blog_stats.html', context)

@staff_member_required
def cleanup_old_entries(request):
    """Vista AJAX para limpiar entradas antiguas"""
    if request.method == 'POST':
        try:
            # Obtener entradas que exceden el límite
            published_entries = BlogEntry.objects.filter(
                is_published=True
            ).order_by('-published_date', '-created_date')
            
            if published_entries.count() <= 3:
                return JsonResponse({
                    'success': True,
                    'message': 'No hay entradas que eliminar.',
                    'deleted_count': 0
                })
            
            entries_to_delete = published_entries[5:]
            deleted_count = 0
            deleted_titles = []
            
            for entry in entries_to_delete:
                title = entry.title
                # Eliminar imagen asociada
                if entry.image:
                    entry.image.delete(save=False)
                entry.delete()
                deleted_count += 1
                deleted_titles.append(title)
            
            return JsonResponse({
                'success': True,
                'message': f'Se eliminaron {deleted_count} entradas exitosamente.',
                'deleted_count': deleted_count,
                'deleted_titles': deleted_titles
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error al eliminar entradas: {str(e)}'
            })
    
    return JsonResponse({'success': False, 'message': 'Método no permitido'})
