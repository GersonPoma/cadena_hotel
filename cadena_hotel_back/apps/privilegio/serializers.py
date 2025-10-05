import re

from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from apps.privilegio.models import Privilegio


class PrivilegioSerializer(ModelSerializer):
    class Meta:
        model = Privilegio
        fields = '__all__'

    def validate_nombre(self, value):
        """Valida el formato del nombre del privilegio"""

        # Eliminar espacios en blanco al inicio y final
        value = value.strip()

        # Validar longitud mínima
        if len(value) < 3:
            raise ValidationError(
                "El nombre debe tener al menos 3 caracteres"
            )

        # Validar longitud máxima
        if len(value) > 100:
            raise ValidationError(
                "El nombre no puede exceder 100 caracteres"
            )

        # Validar que solo contenga letras, números, guiones y guiones bajos
        if not re.match(r'^[A-Za-z0-9_-]+$', value):
            raise ValidationError(
                "El nombre solo puede contener letras, números, guiones (-) y guiones bajos (_)"
            )

        # Validar que empiece con una letra
        if not re.match(r'^[A-Za-z]', value):
            raise ValidationError(
                "El nombre debe comenzar con una letra"
            )

        return value