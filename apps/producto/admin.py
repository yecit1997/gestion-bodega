from django.contrib import admin
from . models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'proveedor', 'precio', 'stock', 'fecha_creacion')
    search_fields = ('nombre', 'categoria__nombre', 'proveedor__nombre')
    list_filter = ('categoria', 'proveedor', 'fecha_creacion')
    ordering = ('id',)
