from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.servicio.models import Servicio
from apps.servicio.serializers import ServicioSerializer


# Create your views here.
class ServicioView(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer
    pagination_class = None  # Desactiva la paginación para esta vista
    #permission_classes = [IsAuthenticated]