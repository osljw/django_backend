"""django_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import api
from .apis.user_info import user_info
from user_auth.views import (
    Register,
    Login,
)
from user_menu.views import UserMenu

urlpatterns = [
    #path('login', api.login, name='login'),
    
    path('user', user_info),
    path('admin/', admin.site.urls),

    path('api/register', Register.as_view()),
    path('api/login', Login.as_view()),

    #path('api/menus', api.menus, name='menus'),
    path('api/menus', UserMenu.as_view()),
]
