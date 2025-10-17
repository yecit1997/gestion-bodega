from django.contrib import admin
from .models import Proveedor

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'contacto', 'telefono', 'email','fecha_creacion')
    search_fields = ('nombre', 'contacto', 'email')
    list_filter = ('fecha_creacion',)
    ordering = ('id',)
