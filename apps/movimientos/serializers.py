# En apps/movimientos/serializers.py (Corregido para la API)

from rest_framework import serializers
from django.db import transaction
from django.db.models import F # Importamos F para operaciones atómicas
from .models import Movimiento
from apps.producto.models import Producto

class MovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movimiento
        fields = '__all__'

    @transaction.atomic
    def create(self, validated_data):
        movimiento = super().create(validated_data) # Usamos super().create para crear el movimiento
        
        tipo = movimiento.tipo
        cantidad = movimiento.cantidad
        
        # Validación de stock para Salida (requiere una lectura previa)
        if tipo == Movimiento.SALIDA:
            producto_actual = Producto.objects.get(pk=movimiento.producto_id)
            if producto_actual.stock < cantidad:
                raise serializers.ValidationError("No hay suficiente stock para esta salida.")
        
        # 3. Modificar el stock del Producto ATÓMICAMENTE
        if tipo == Movimiento.ENTRADA:
            Producto.objects.filter(pk=movimiento.producto_id).update(stock=F('stock') + cantidad)
        elif tipo == Movimiento.SALIDA:
            Producto.objects.filter(pk=movimiento.producto_id).update(stock=F('stock') - cantidad)

        return movimiento