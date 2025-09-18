from rest_framework import viewsets

from apps.cargo.models import Cargo
from apps.cargo.serializers import CargoSerializer

# Create your views here.

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer