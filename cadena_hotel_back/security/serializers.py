from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Un solo user_id que puede ser empleado, huesped o usuario base
        if hasattr(user, "empleado") and user.empleado:
            token["user_id"] = user.empleado.id
        elif hasattr(user, "huesped") and user.huesped:
            token["user_id"] = user.huesped.id
        else:
            token["user_id"] = user.id  # si no tiene perfil

        # un solo rol (string)
        role = user.groups.values_list("name", flat=True).first()
        token["role"] = role or "usuario"  # fallback si no tiene grupo

        return token