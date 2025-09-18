from rest_framework import serializers

from apps.empleado.models import Empleado
from apps.persona.serializer import PersonaSerializer


class EmpleadoSerializer(PersonaSerializer):
    cargo_nombre = serializers.CharField(source='cargo.nombre', read_only=True)

    class Meta(PersonaSerializer.Meta):
        model = Empleado
        fields = PersonaSerializer.Meta.fields + [
            'hora_trabajo',
            'estado',
            'cargo',
            'cargo_nombre',
            'usuario',
        ]
        read_only_fields = ['usuario']