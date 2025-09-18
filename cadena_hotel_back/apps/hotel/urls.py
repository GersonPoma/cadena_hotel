from rest_framework.routers import DefaultRouter
from .views import HotelViewSet

router = DefaultRouter()
router.register(r'', HotelViewSet, basename='hoteles')

urlpatterns = router.urls

