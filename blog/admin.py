from django.contrib import admin
from .models import BlogEntry

@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'published_date', 'is_published']
    list_filter = ['is_published', 'created_date', 'published_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {}
    date_hierarchy = 'published_date'
    ordering = ['-created_date']
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('title', 'excerpt', 'content', 'image')
        }),
        ('Publicación', {
            'fields': ('is_published', 'published_date'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['make_published', 'make_unpublished']
    
    def make_published(self, request, queryset):
        queryset.update(is_published=True)
        for obj in queryset:
            if not obj.published_date:
                obj.publish()
    make_published.short_description = "Publicar entradas seleccionadas"
    
    def make_unpublished(self, request, queryset):
        queryset.update(is_published=False)
    make_unpublished.short_description = "Despublicar entradas seleccionadas"
