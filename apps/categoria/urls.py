from django.urls import include, path
from .views import CategoriaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet, basename='categoria')

urlpatterns = [
    path('', include(router.urls)),
]
