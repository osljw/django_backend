from django.urls import path
from .views import ArticleDetailView, ArticleListView

urlpatterns = [
    path(r"article/list", ArticleListView.as_view()),
    path(r"article/<int:pk>", ArticleDetailView.as_view())
]