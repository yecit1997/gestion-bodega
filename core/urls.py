from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.categoria.urls')),
    # path('api/', include('apps.producto.urls')),
    # path('api/', include('apps.movimientos.urls')),
]
