from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import Register

urlpatterns = [
    # path('login', obtain_jwt_token),
    path('login', TokenObtainPairView.as_view()),
    # path('api-token-refresh/', refresh_jwt_token),
    path('register', Register.as_view()),

    path('token/refresh', refresh_jwt_token),
]