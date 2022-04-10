from django.urls import path
from .views import BannerView

urlpatterns = [
    path(r"banner", BannerView.as_view()),
]