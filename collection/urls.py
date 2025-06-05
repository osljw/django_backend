from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CulturalRelicViewSet

router = DefaultRouter()
router.register(r'collection', CulturalRelicViewSet)

urlpatterns = [
    path('', include(router.urls)),
]