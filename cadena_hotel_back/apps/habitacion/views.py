from rest_framework import viewsets
from .models import Habitacion
from .serializers import HabitacionSerializer

# Create your views here.

class HabitacionViewSet(viewsets.ModelViewSet):
    queryset = Habitacion.objects.all()
    serializer_class = HabitacionSerializer