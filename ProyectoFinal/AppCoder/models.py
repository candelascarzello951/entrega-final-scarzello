from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    imagen = models.FileField(upload_to="media/blogs", null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"{self.titulo} por {self.autor.username}"
    
class Producto (models.Model):
    nombre_producto = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre_producto}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    
class stock (models.Model):
    stock = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.stock}"

from django.contrib.auth.models import User

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to="media/avatares", null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
    

