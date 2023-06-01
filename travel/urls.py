from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TravelViewSet, OrderViewSet

router = SimpleRouter()
router.register(r'travel', TravelViewSet, basename='travel')

print("-------------router.urls:", router.urls)
urlpatterns = router.urls

router = SimpleRouter()
router.register(r'order', OrderViewSet, basename='order')
urlpatterns += router.urls