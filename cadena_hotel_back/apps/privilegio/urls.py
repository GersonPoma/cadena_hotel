from rest_framework.routers import DefaultRouter

from apps.privilegio.views import PrivilegioViewSet

router = DefaultRouter()
router.register(r'', PrivilegioViewSet, basename='privilegios')

urlpatterns = router.urls