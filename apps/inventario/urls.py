from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventarioViewSet, DetalleInventarioViewSet, KardexViewSet

router = DefaultRouter()
router.register(r'inventarios', InventarioViewSet)
router.register(r'detalles-inventario', DetalleInventarioViewSet)
router.register(r'kardex', KardexViewSet)

urlpatterns = [
    path('', include(router.urls))
]
