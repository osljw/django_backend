from django.urls import path
from .views import notice_view

urlpatterns = [
    path('notice', notice_view, name='notice'),
]