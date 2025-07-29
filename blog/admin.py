from django.contrib import admin
from django.contrib import messages
from .models import BlogEntry

@admin.register(BlogEntry)
class BlogEntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'published_date', 'is_published', 'get_published_count']
    list_filter = ['is_published', 'created_date', 'published_date']
    search_fields = ['title', 'content']
    prepopulated_fields = {}
    date_hierarchy = 'published_date'
    ordering = ['-created_date']
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('title', 'excerpt', 'content', 'image', 'url')
        }),
        ('Publicación', {
            'fields': ('is_published', 'published_date'),
            'classes': ('collapse',),
            'description': 'NOTA: Solo se mantienen las 3 publicaciones más recientes. Las anteriores se eliminan automáticamente.'
        }),
    )
    
    actions = ['make_published', 'make_unpublished']
    
    def get_published_count(self, obj):
        """Muestra el número actual de entradas publicadas"""
        count = BlogEntry.objects.filter(is_published=True).count()
        if count >= 3:
            return f"{count}/3 (LÍMITE ALCANZADO)"
        return f"{count}/3"
    get_published_count.short_description = "Publicadas (Límite: 3)"
    
    def save_model(self, request, obj, form, change):
        """Sobrescribe el guardado para mostrar mensajes informativos"""
        published_count = BlogEntry.objects.filter(is_published=True).count()
        
        # Si se está publicando una nueva entrada y ya hay 3 publicadas
        if obj.is_published and not change and published_count >= 3:
            messages.warning(
                request, 
                f"AVISO: Ya hay {published_count} entradas publicadas. "
                "Las entradas más antiguas se eliminarán automáticamente para mantener el límite de 3."
            )
        elif obj.is_published and change and published_count >= 3:
            # Si se está editando una entrada existente para publicarla
            old_obj = BlogEntry.objects.get(pk=obj.pk)
            if not old_obj.is_published:
                messages.warning(
                    request, 
                    f"AVISO: Ya hay {published_count} entradas publicadas. "
                    "Las entradas más antiguas se eliminarán automáticamente para mantener el límite de 3."
                )
        
        super().save_model(request, obj, form, change)
        
        # Mensaje de confirmación después del guardado
        new_count = BlogEntry.objects.filter(is_published=True).count()
        if obj.is_published:
            messages.success(
                request,
                f"Entrada guardada exitosamente. Entradas publicadas actuales: {new_count}/3"
            )
    
    def make_published(self, request, queryset):
        published_count = BlogEntry.objects.filter(is_published=True).count()
        entries_to_publish = queryset.filter(is_published=False).count()
        
        if published_count + entries_to_publish > 3:
            messages.warning(
                request,
                f"AVISO: Publicar {entries_to_publish} entradas excederá el límite de 3. "
                "Las entradas más antiguas se eliminarán automáticamente."
            )
        
        for obj in queryset:
            if not obj.is_published:
                obj.publish()
        
        messages.success(request, f"Entradas publicadas. Total actual: {BlogEntry.objects.filter(is_published=True).count()}/3")
    make_published.short_description = "Publicar entradas seleccionadas"
    
    def make_unpublished(self, request, queryset):
        queryset.update(is_published=False)
        new_count = BlogEntry.objects.filter(is_published=True).count()
        messages.success(request, f"Entradas despublicadas. Total actual: {new_count}/3")
    make_unpublished.short_description = "Despublicar entradas seleccionadas"
