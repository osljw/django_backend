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
from django.conf.urls.static import static
from django.views.generic import TemplateView
# import xadmin
# from xadmin.plugins import xversion

import re
from . import settings
from . import api

# xversion.register_models()
# xadmin.autodiscover()

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('wangeditor/', include('wangeditor.urls')),
    # path('xadmin', xadmin.site.urls),
    path('markdownx/', include('markdownx.urls')), # grappelli URLS

    # re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

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

    path('api/', include('notice.urls')),
    # path('api/', include('chatgpt.urls')),
    path('api/', include('travel.urls')),
    # path('api/', include('pay_ali.urls')),

    path('api/', include('book_management.urls')),

    # 将静态文件路由排在前面
    re_path(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve, {'document_root': settings.STATIC_ROOT}),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns +=[
#     # Catch-all route to redirect to the frontend
#     re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
# ]

# for url in urlpatterns:
#     print(url)

from user_chat.views import ChatConsumer, GameConsumer

websocket_urlpatterns = [
    # 前端请求websocket连接
    path('ws/chat', ChatConsumer.as_asgi()),
    path('ws/game', GameConsumer.as_asgi()),
]