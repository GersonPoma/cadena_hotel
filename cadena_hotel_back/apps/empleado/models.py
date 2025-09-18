from django.conf import settings
from django.db import models

from apps.cargo.models import Cargo
from apps.persona.models import Persona


# Create your models here.

class Empleado(Persona):
    hora_trabajo = models.TimeField()
    estado = models.CharField(max_length=50)
    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.PROTECT,
        related_name='empleados'
    )
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='empleado'
    )