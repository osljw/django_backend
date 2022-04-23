from django.urls import path
from .views import BannerView, TopNavView, BottomNavView

urlpatterns = [
    path(r"banner", BannerView.as_view()),
    path(r"nav/top", TopNavView.as_view()),
    path(r"nav/bottom", BottomNavView.as_view()),
]