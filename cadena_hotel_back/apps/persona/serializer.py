from rest_framework import serializers

from apps.persona.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    edad = serializers.SerializerMethodField()

    class Meta:
        model = Persona
        fields = [
            'id',
            'nombre',
            'apellido',
            'fecha_nacimiento',
            'edad',
            'documento_identidad',
            'email',
            'telefono',
            'direccion',
            'ciudad',
            'pais',
        ]

    def get_edad(self, obj):
        return obj.get_edad()