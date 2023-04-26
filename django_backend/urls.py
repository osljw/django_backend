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
from django.views.static import serve
# import xadmin
# from xadmin.plugins import xversion

from . import settings
from . import api
from user_menu.views import UserMenu

from upload.views import UploadView

# xversion.register_models()
# xadmin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('xadmin', xadmin.site.urls),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # 登录认证
    # path('api/login', obtain_jwt_token),
    # path('api-token-refresh/', refresh_jwt_token),
    path('api/', include('user_auth.urls')),

    # path('api/menus', UserMenu.as_view()),
    # path('api/users', UserList.as_view()),

    path('api/', include('home.urls')),
    path('api/', include('article.urls')),



    path('api/room/', include('music_room.urls')),

    path('api/museum/', include('museum.urls')),

    path('api/upload/', include('upload.urls')),
    # path('api/upload', UploadView.as_view())

    path('api/', include('question.urls')),
    path('api/', include('leaderboard.urls')),
]

from user_chat.views import ChatConsumer, GameConsumer

websocket_urlpatterns = [
    # 前端请求websocket连接
    path('ws/chat', ChatConsumer.as_asgi()),
    path('ws/game', GameConsumer.as_asgi()),
]