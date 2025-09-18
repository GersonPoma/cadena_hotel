from django.db import models

from apps.hotel.models import Hotel


# Create your models here.

class Habitacion(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)  # Ejemplo: Sencilla, Doble, Suite
    capacidad = models.IntegerField()  # Número de personas que puede alojar
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20)  # Ejemplo: Disponible, Ocupada, Mantenimiento
    hotel = models.ForeignKey(Hotel, on_delete=models.PROTECT, related_name='habitaciones')

    def __str__(self):
        return f'Habitación {self.numero} - {self.tipo} - {self.hotel.nombre}'