from rest_framework import viewsets
from apps.huesped.models import Huesped
from apps.huesped.serializers import HuespedSerializer

# Create your views here.

class HuespedViewSet(viewsets.ModelViewSet):
    queryset = Huesped.objects.all()
    serializer_class = HuespedSerializer
