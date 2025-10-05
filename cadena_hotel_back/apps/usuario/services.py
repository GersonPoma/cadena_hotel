from rest_framework import serializers
from django.db import transaction
from .serializers import UsuarioSerializer
from apps.huesped.serializers import HuespedSerializer
from apps.empleado.serializers import EmpleadoSerializer


def generar_username(nombre, documento_identidad):
    """
    Genera username: primer_nombre + documento_identidad
    """
    primer_nombre = nombre.strip().split()[0]  # Obtiene el primer nombre
    return f"{primer_nombre}{documento_identidad}"


def generar_password(nombre, apellido, documento_identidad):
    """
    Genera password basado en apellidos y nombres:
    - Si tiene 2 apellidos: Primera_letra_apellido1(mayúscula) + "." + primera_letra_apellido2(minúscula) + "." + documento_identidad
    - Si tiene 1 apellido: Primera_letra_apellido(mayúscula) + "." + primera_letra_primer_nombre(minúscula) + "." + documento_identidad
    """
    apellidos = apellido.strip().split()
    primer_nombre = nombre.strip().split()[0]

    if len(apellidos) >= 2:
        # Tiene 2 o más apellidos
        primera_letra_apellido1 = apellidos[0][0].upper()
        primera_letra_apellido2 = apellidos[1][0].lower()
        return f"{primera_letra_apellido1}.{primera_letra_apellido2}.{documento_identidad}"
    else:
        # Solo tiene 1 apellido
        primera_letra_apellido = apellidos[0][0].upper()
        primera_letra_nombre = primer_nombre[0].lower()
        return f"{primera_letra_apellido}.{primera_letra_nombre}.{documento_identidad}"


def crear_usuario(nombre, apellido, documento_identidad):
    """
    Función utilitaria para crear un usuario con username y password generados automáticamente
    """
    username = generar_username(nombre, documento_identidad)
    password = generar_password(nombre, apellido, documento_identidad)

    usuario_data = {
        'username': username,
        'password': password,
        'password_confirm': password,
        'is_active': True
    }

    serializer = UsuarioSerializer(data=usuario_data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise serializers.ValidationError(serializer.errors)


@transaction.atomic
def crear_huesped_con_usuario(huesped_data, usuario_data=None):
    """
    Función para crear un huesped con su usuario asociado
    Args:
        huesped_data: diccionario con los datos del huesped
        usuario_data: (opcional) diccionario con datos de usuario. Si no se proporciona, se genera automáticamente
    Returns:
        tuple: (huesped_instance, usuario_instance)
    """

    # Crear usuario con datos generados automáticamente
    usuario = crear_usuario(
        huesped_data['nombre'],
        huesped_data['apellido'],
        huesped_data['documento_identidad']
    )

    # Agregar el usuario al huesped_data
    huesped_data['usuario'] = usuario.id

    # Crear huesped usando su serializer
    huesped_serializer = HuespedSerializer(data=huesped_data)
    if huesped_serializer.is_valid():
        huesped = huesped_serializer.save()
        return huesped, usuario
    else:
        # Si falla, eliminar el usuario creado
        usuario.delete()
        raise serializers.ValidationError(huesped_serializer.errors)


@transaction.atomic
def crear_empleado_con_usuario(empleado_data, usuario_data=None):
    """
    Función para crear un empleado con su usuario asociado
    Args:
        empleado_data: diccionario con los datos del empleado
        usuario_data: (opcional) diccionario con datos de usuario. Si no se proporciona, se genera automáticamente
    Returns:
        tuple: (empleado_instance, usuario_instance)
    """

    # Crear usuario con datos generados automáticamente
    usuario = crear_usuario(
        empleado_data['nombre'],
        empleado_data['apellido'],
        empleado_data['documento_identidad']
    )

    # Agregar el usuario al empleado_data
    empleado_data['usuario'] = usuario.id

    # Crear empleado usando su serializer
    empleado_serializer = EmpleadoSerializer(data=empleado_data)
    if empleado_serializer.is_valid():
        empleado = empleado_serializer.save()
        return empleado, usuario
    else:
        # Si falla, eliminar el usuario creado
        usuario.delete()
        raise serializers.ValidationError(empleado_serializer.errors)
