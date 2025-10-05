from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CrearHuespedConUsuarioAPIView, CrearEmpleadoConUsuarioAPIView

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('usuarios/crear-huesped/', CrearHuespedConUsuarioAPIView.as_view(), name='crear-huesped-con-usuario'),
    path('usuarios/crear-empleado/', CrearEmpleadoConUsuarioAPIView.as_view(), name='crear-empleado-con-usuario'),
]

urlpatterns += router.urls
