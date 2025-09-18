from apps.empleado.models import Empleado
from apps.persona.serializer import PersonaSerializer


class EmpleadoSerializer(PersonaSerializer):
    class Meta(PersonaSerializer.Meta):
        model = Empleado
        fields = PersonaSerializer.Meta.fields + (
            'hora_trabajo',
            'estado',
            'cargo',
        )