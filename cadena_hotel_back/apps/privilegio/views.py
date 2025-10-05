from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from apps.privilegio.models import Privilegio
from apps.privilegio.serializers import PrivilegioSerializer


# Create your views here.
class PrivilegioViewSet(ModelViewSet):
    queryset = Privilegio.objects.all()
    serializer_class = PrivilegioSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["nombre"]
    ordering = ["id"]
    #permission_classes = [IsAuthenticated]
