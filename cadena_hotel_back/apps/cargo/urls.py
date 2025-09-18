from rest_framework.routers import DefaultRouter

from apps.cargo.views import CargoViewSet

router = DefaultRouter()
router.register(r'', CargoViewSet, basename='cargos')

urlpatterns = router.urls