from rest_framework import serializers
from django.db import transaction
from .models import Producto
from apps.movimientos.models import Movimiento

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
    @transaction.atomic
    def create(self, validated_data):
        stockt_inicial = validated_data.get('stock', 0)
        producto = super().create(validated_data)
        
        # Si el producto se crea con stock inicial mayor a 0, crear un movimiento de entrada
        if stockt_inicial > 0:
            Movimiento.objects.create(
                producto=producto,
                tipo=Movimiento.ENTRADA,
                cantidad=stockt_inicial,
                origen=Movimiento.AUTOMATICO,
                observaciones="Registro inicial del producto."
            )
       
        return producto