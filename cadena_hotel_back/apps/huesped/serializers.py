from apps.huesped.models import Huesped
from apps.persona.serializer import PersonaSerializer


class HuespedSerializer(PersonaSerializer):
    class Meta(PersonaSerializer.Meta):
        model = Huesped
        fields = PersonaSerializer.Meta.fields + ['fecha_registro', 'vip']