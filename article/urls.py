from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ArticleModelViewSet, ArticleCategoryViewSet


router = SimpleRouter(trailing_slash=False)
router.register('article/category', ArticleCategoryViewSet)
router.register('article', ArticleModelViewSet)
urlpatterns = router.urls