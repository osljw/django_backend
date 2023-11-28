from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PageModelViewSet


router = SimpleRouter(trailing_slash=False)
router.register('page', PageModelViewSet)
urlpatterns = router.urls