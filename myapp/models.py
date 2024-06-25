from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fechaCreada = models.DateTimeField(auto_now_add=True)
    fechaCompletada = models.DateTimeField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
