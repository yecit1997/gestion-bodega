from django.db import models
from simple_history.models import HistoricalRecords

from apps.producto.models import Producto

import uuid

class Movimiento(models.Model):
    # Aqui manejamos las opciones de tipo de movimiento
    ENTRADA = 'E'
    SALIDA = 'S'
    TIPO_CHOICES = [
        (ENTRADA, 'Entrada'),
        (SALIDA, 'Salida'),
    ]
    
    # 
    MANUAL = 'M'
    AUTOMATICO = 'A'
    ORIGEN_CHOICES = [
        (MANUAL, 'Manual'),
        (AUTOMATICO, 'Automático'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    cantidad = models.PositiveIntegerField()
    origen = models.CharField(max_length=20, choices=ORIGEN_CHOICES, default=MANUAL)
    fecha = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)
    history = HistoricalRecords()

    def __str__(self):
        '''
        Esta funcion get_tipo_display() es proporcionada por Django para obtener la representación legible del campo 'tipo' 
        basado en las opciones definidas en TIPO_CHOICES.
        '''
        return f"{self.get_tipo_display()} - {self.producto.nombre} ({self.cantidad})" # type: ignore[attr-defined]
    
    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimientos"
        ordering = ['-fecha']