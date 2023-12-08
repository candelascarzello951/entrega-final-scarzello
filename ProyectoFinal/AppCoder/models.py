from django.db import models

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

