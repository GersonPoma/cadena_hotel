from django.shortcuts import render
from rest_framework import viewsets

from apps.empleado.models import Empleado
from apps.empleado.serializers import EmpleadoSerializer


# Create your views here.
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer