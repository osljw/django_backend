from django.urls import path

from .views import UploadView, ProxyView

urlpatterns = [
    path('upload', UploadView.as_view()),
    path('proxy/<path:path>', ProxyView.as_view(), name='proxy')
]