from rest_framework import viewsets
from .models import Inventario, DetalleInventario, Kardex
from .serializers import InventarioSerializer, DetalleInventarioSerializer, KardexSerializer

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class DetalleInventarioViewSet(viewsets.ModelViewSet):
    queryset = DetalleInventario.objects.all()
    serializer_class = DetalleInventarioSerializer

class KardexViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Kardex.objects.all()
    serializer_class = KardexSerializer
