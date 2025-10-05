from rest_framework import viewsets
from .models import Habitacion
from .serializers import HabitacionSerializer

# Create your views here.

class HabitacionViewSet(viewsets.ModelViewSet):
    serializer_class = HabitacionSerializer
    pagination_class = None     # Desactiva la paginación para esta vista

    def get_queryset(self):
        """
        Opcionalmente filtra las habitaciones por hotel
        usando el parámetro ?hotel=id
        """
        queryset = Habitacion.objects.all()
        hotel_id = self.request.query_params.get('hotel')

        if hotel_id:
            queryset = queryset.filter(hotel_id=hotel_id)

        return queryset
