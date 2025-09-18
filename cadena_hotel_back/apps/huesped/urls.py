from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HuespedViewSet

router = DefaultRouter()
router.register(r'', HuespedViewSet, basename='huespedes')

urlpatterns = [
    path('', include(router.urls)),
]

