from django.contrib import admin
from .models import Place

# Register your models here.
class PlaceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(Place, PlaceAdmin)
