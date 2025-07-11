from django.shortcuts import render, get_object_or_404
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
