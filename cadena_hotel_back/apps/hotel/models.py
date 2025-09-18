from django.db import models

# Create your models here.

class Hotel(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    categoria = models.IntegerField()  # 1 a 5 estrellas
    fecha_inauguracion = models.DateField()