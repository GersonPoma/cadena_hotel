from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .models import Usuario
from .serializers import UsuarioSerializer, UsuarioSimpleSerializer
from .services import crear_huesped_con_usuario, crear_empleado_con_usuario
from ..empleado.serializers import EmpleadoSerializer
from ..huesped.serializers import HuespedSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return UsuarioSimpleSerializer
        return UsuarioSerializer


class CrearHuespedConUsuarioAPIView(APIView):
    """
    APIView para crear un huésped con su usuario asociado automáticamente
    """

    @extend_schema(
        request=HuespedSerializer,
        responses={
            201: HuespedSerializer,
            400: OpenApiResponse(
                description="Error en validación de datos"
            )
        },
        description="Crea un huésped y genera automáticamente su usuario con credenciales basadas en nombre, apellido y documento de identidad",
        summary="Crear huésped con usuario"
    )
    def post(self, request):
        """
        Crea un huésped con usuario generado automáticamente

        Username generado: primer_nombre + documento_identidad
        Password generado:
        - Con 2 apellidos: Primera_letra_apellido1(mayúscula) + "." + primera_letra_apellido2(minúscula) + "." + documento
        - Con 1 apellido: Primera_letra_apellido(mayúscula) + "." + primera_letra_nombre(minúscula) + "." + documento
        """
        huesped_data = request.data

        # Validar que se proporcionen los campos requeridos para generar usuario
        required_fields = ['nombre', 'apellido', 'documento_identidad']
        missing_fields = [field for field in required_fields if not huesped_data.get(field)]

        if missing_fields:
            return Response(
                {"error": f"Faltan campos requeridos: {', '.join(missing_fields)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            huesped, usuario = crear_huesped_con_usuario(huesped_data)

            # Serializar la respuesta
            huesped_serializer = HuespedSerializer(huesped)

            return Response({
                "message": "Huésped y usuario creados exitosamente",
                "huesped": huesped_serializer.data,
                "usuario": {
                    "id": usuario.id,
                    "username": usuario.username,
                    "is_active": usuario.is_active,
                    "date_joined": usuario.date_joined
                },
                "credenciales": {
                    "username": usuario.username,
                    "password_info": "Password generado automáticamente basado en apellidos y documento"
                }
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )


class CrearEmpleadoConUsuarioAPIView(APIView):
    """
    APIView para crear un empleado con su usuario asociado automáticamente
    """

    @extend_schema(
        request=EmpleadoSerializer,
        responses={
            201: EmpleadoSerializer,
            400: OpenApiResponse(
                description="Error en validación de datos"
            )
        },
        description="Crea un empleado y genera automáticamente su usuario con credenciales basadas en nombre, apellido y documento de identidad",
        summary="Crear empleado con usuario"
    )
    def post(self, request):
        """
        Crea un empleado con usuario generado automáticamente

        Username generado: primer_nombre + documento_identidad
        Password generado:
        - Con 2 apellidos: Primera_letra_apellido1(mayúscula) + "." + primera_letra_apellido2(minúscula) + "." + documento
        - Con 1 apellido: Primera_letra_apellido(mayúscula) + "." + primera_letra_nombre(minúscula) + "." + documento
        """
        empleado_data = request.data

        # Validar que se proporcionen los campos requeridos para generar usuario
        required_fields = ['nombre', 'apellido', 'documento_identidad']
        missing_fields = [field for field in required_fields if not empleado_data.get(field)]

        if missing_fields:
            return Response(
                {"error": f"Faltan campos requeridos: {', '.join(missing_fields)}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            empleado, usuario = crear_empleado_con_usuario(empleado_data)

            # Serializar la respuesta
            empleado_serializer = EmpleadoSerializer(empleado)

            return Response({
                "message": "Empleado y usuario creados exitosamente",
                "empleado": empleado_serializer.data,
                "usuario": {
                    "id": usuario.id,
                    "username": usuario.username,
                    "is_active": usuario.is_active,
                    "date_joined": usuario.date_joined
                },
                "credenciales": {
                    "username": usuario.username,
                    "password_info": "Password generado automáticamente basado en apellidos y documento"
                }
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
