from rest_framework.routers import DefaultRouter

from apps.servicio.views import ServicioView

router = DefaultRouter()
router.register(r'', ServicioView, basename='servicios')

urlpatterns = router.urls