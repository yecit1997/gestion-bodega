from django.db import models
from django.contrib.auth.models import User
from apps.producto.models import Producto

import uuid

class Inventario(models.Model):
    """
    Representa una toma física de inventario (conteo en bodega).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Inventario {self.fecha.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"
        ordering = ['-fecha']


class DetalleInventario(models.Model):
    """
    Detalle de productos dentro de una toma física de inventario.
    Permite comparar el stock real con el del sistema.
    """
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    stock_sistema = models.PositiveIntegerField()
    stock_fisico = models.PositiveIntegerField()
    diferencia = models.IntegerField()

    def save(self, *args, **kwargs):
        # Calcula la diferencia automáticamente antes de guardar
        self.diferencia = self.stock_fisico - self.stock_sistema
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.producto.nombre} (Dif: {self.diferencia})"

    class Meta:
        verbose_name = "Detalle de Inventario"
        verbose_name_plural = "Detalles de Inventario"


class Kardex(models.Model):
    """
    Registro histórico de entradas y salidas de un producto (movimientos consolidados).
    Este modelo se puede llenar automáticamente a partir de los Movimientos.
    """
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    tipo = models.CharField(max_length=10, choices=[('Entrada', 'Entrada'), ('Salida', 'Salida')])
    cantidad = models.PositiveIntegerField()
    saldo = models.IntegerField()  # stock resultante tras ese movimiento
    referencia = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "Kardex"
        verbose_name_plural = "Kardex"
        ordering = ['producto', 'fecha']

    def __str__(self):
        return f"{self.producto.nombre} - {self.tipo} ({self.cantidad})"

