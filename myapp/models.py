from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    titulo          = models.CharField(max_length=50)
    descripcion     = models.TextField(blank=True)
    fechaCreada     = models.DateTimeField(auto_now_add=True)
    fechaCompletada = models.DateTimeField(null=True, blank=True)
    important       = models.BooleanField(default=False)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    precio          = models.DecimalField(max_digits=12, decimal_places=0, default=0.00)

    def __str__ (self):
        return self.titulo +' |- Hecho por: ' + self.user.username
    

class Carrito(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fecha_carrito = models.DateTimeField(auto_now_add=True)

class producto_item(models.Model):
    carr = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad_item = models.IntegerField(default=1)

    @property
    def total(self):
        return self.product.precio * self.cantidad_item

