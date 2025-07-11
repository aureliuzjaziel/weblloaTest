from django.shortcuts import render, HttpResponse
from places.models import Place
from blog.models import BlogEntry


# Create your views here.
def home(request): 
    places = Place.objects.all()
    blog_entries = BlogEntry.objects.filter(is_published=True)[:6]  # Últimas 6 entradas publicadas
    return render(request,'core/index.html',{
        'places': places,
        'blog_entries': blog_entries
    })
