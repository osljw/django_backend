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
from django.urls import path, re_path, include
import xadmin
from xadmin.plugins import xversion
from django.views.static import serve
from . import settings

from . import api
from .apis.user_info import user_info
from user_auth.views import (
    Register,
    Login,
    UserList
)
from user_menu.views import UserMenu

xversion.register_models()
xadmin.autodiscover()

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('xadmin', xadmin.site.urls),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    path('user', user_info),
    

    path('api/register', Register.as_view()),
    path('api/login', Login.as_view()),

    path('api/menus', UserMenu.as_view()),
    path('api/users', UserList.as_view()),

    path('', include('home.urls')),
]

from user_chat.views import ChatConsumer

websocket_urlpatterns = [
    # 前端请求websocket连接
    path('ws/chat', ChatConsumer.as_asgi()),
]