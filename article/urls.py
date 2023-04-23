from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ArticleDetailView, ArticleListView, ArticleModelViewSet

urlpatterns = [
    # path(r"article/list", ArticleListView.as_view()),
    # path(r"article/<int:pk>", ArticleDetailView.as_view())
]

router = DefaultRouter()
router.register('article', ArticleModelViewSet)
urlpatterns += router.urls