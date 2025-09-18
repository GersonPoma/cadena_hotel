from django.conf import settings
from django.db import models

from apps.persona.models import Persona


# Create your models here.

class Huesped(Persona):
    fecha_registro = models.DateField(auto_now_add=True)
    vip = models.BooleanField(default=False)
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='huesped'
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"