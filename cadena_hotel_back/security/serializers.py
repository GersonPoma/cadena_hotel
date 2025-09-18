from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # perfiles opcionales
        if hasattr(user, "empleado"):
            token["empleado_id"] = user.empleado.id
        elif hasattr(user, "huesped"):
            token["huesped_id"] = user.huesped.id
        else:
            token["usuario_id"] = user.id  # si no tiene perfil

        # un solo rol (string)
        role = user.groups.values_list("name", flat=True).first()
        token["role"] = role or "usuario"  # fallback si no tiene grupo

        return token