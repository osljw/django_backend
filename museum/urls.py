from django.urls import path
from .views import MuseumListView

urlpatterns = [
    path("list", MuseumListView.as_view()),
]