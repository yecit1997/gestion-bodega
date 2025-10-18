from django.urls import path, include
from .views import MovimientoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'movimientos', MovimientoViewSet, basename='movimiento')

urlpatterns = [
    path('', include(router.urls)),
]
