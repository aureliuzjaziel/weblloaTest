from django.contrib import admin
from .models import Place

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'subtitle', 'whatsapp_number', 'created')
    fields = ('title', 'subtitle', 'description', 'image', 'url', 'whatsapp_number', 'created', 'updated')
    
admin.site.register(Place, PlaceAdmin)
