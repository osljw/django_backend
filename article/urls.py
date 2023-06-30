from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ArticleModelViewSet


router = SimpleRouter(trailing_slash=False)
router.register('article', ArticleModelViewSet)
urlpatterns = router.urls