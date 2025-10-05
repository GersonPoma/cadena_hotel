from rest_framework import serializers
from .models import Habitacion

class HabitacionSerializer(serializers.ModelSerializer):
    hotel_nombre = serializers.SerializerMethodField()

    class Meta:
        model = Habitacion
        fields = '__all__'

    def get_hotel_nombre(self, obj):
        return obj.hotel.nombre if obj.hotel else None
