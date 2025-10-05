from drf_spectacular.utils import extend_schema
from rest_framework_simplejwt.views import TokenObtainPairView

from security.serializers import CustomTokenObtainPairSerializer


@extend_schema(
    responses=CustomTokenObtainPairSerializer,
    request=CustomTokenObtainPairSerializer,
)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer