from django.contrib import admin
from .models import Place

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'whatsapp_number', 'has_menu', 'menu_type', 'created')
    list_filter = ('created', 'updated')
    search_fields = ('title', 'subtitle', 'description')
    fields = ('title', 'subtitle', 'description', 'image', 'url', 'whatsapp_number', 'menu_file', 'created', 'updated')
    
    def has_menu(self, obj):
        return bool(obj.menu_file)
    has_menu.boolean = True
    has_menu.short_description = 'Tiene Menú'
    
    def menu_type(self, obj):
        if not obj.menu_file:
            return '-'
        elif obj.is_menu_image():
            return '🖼️ Imagen'
        elif obj.is_menu_pdf():
            return '📄 PDF'
        else:
            return '📁 Archivo'
    menu_type.short_description = 'Tipo de Menú'
    
admin.site.register(Place, PlaceAdmin)
