from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    titulo          = models.CharField(max_length=50)
    descripcion     = models.TextField(blank=True)
    fechaCreada     = models.DateTimeField(auto_now_add=True)
    important       = models.BooleanField(default=False)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    precio          = models.IntegerField(default=0)
    imagen          = models.ImageField(upload_to='media/productos/', null=True, blank=True)

    def __str__ (self):
        return self.titulo +' |- Hecho por: ' + self.user.username
    def precio_formateado(self):
        return f"${self.precio:,}".replace(",", ".")
 
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

