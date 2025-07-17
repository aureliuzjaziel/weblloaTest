from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # URLs principales del blog
    path('', views.blog_list, name='blog_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    
    # URLs de administración
    path('stats/', views.blog_stats, name='blog_stats'),
    path('cleanup/', views.cleanup_old_entries, name='cleanup_old_entries'),
]
