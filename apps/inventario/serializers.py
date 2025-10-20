from rest_framework import serializers
from .models import Inventario, DetalleInventario, Kardex

class DetalleInventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleInventario
        fields = '__all__'

class InventarioSerializer(serializers.ModelSerializer):
    detalles = DetalleInventarioSerializer(many=True, read_only=True)

    class Meta:
        model = Inventario
        fields = '__all__'

class KardexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kardex
        fields = '__all__'
