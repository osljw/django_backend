from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TravelViewSet

router = SimpleRouter(trailing_slash=False)
router.register('travel', TravelViewSet)

urlpatterns = router.urls