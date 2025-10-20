from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.movimientos.models import Movimiento
from apps.inventario.models import Kardex
from apps.producto.models import Producto

@receiver(post_save, sender=Movimiento)
def actualizar_kardex(sender, instance, created, **kwargs):
    if not created:
        return
    
    producto = instance.producto
    stock_actual = producto.stock  # stock ya actualizado por tu lógica en el serializer

    Kardex.objects.create(
        producto=producto,
        fecha=instance.fecha,
        tipo=instance.get_tipo_display(),
        cantidad=instance.cantidad,
        saldo=stock_actual,
        referencia=f"Movimiento {instance.id}"
    )
