from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.

from .models import Page
from .serializers import PageListSerializer, PageDetailSerializer

class PageModelViewSet(ModelViewSet):
    queryset = Page.objects.filter(valid=True)
    #authentication_classes = [JSONWebTokenAuthentication, SessionAuthentication]
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [AllowAny]
    
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    #ordering_fields = [ 'field1', 'field2' ]  # 可以根据这里的字段进行排序
    search_fields = ['url']  # 可以根据这里的字段进行搜索

    def get_queryset(self):
        print("page =====user:", self.request.user, self.request.user.is_superuser)
        user = self.request.user
        valid = self.request.query_params.get('valid')
        print("valid:", valid)
        
        if valid is None:
            return self.queryset

        # admin backend
        if user.is_superuser and valid is not None and valid.lower() == 'all':
            return Page.objects.all()
        
        return self.queryset

    def get_serializer_class(self):
        # if 'title' in self.kwargs:  # URL中包含了文章ID，使用ArticleDetailSerializer
        print("=======", self.request.query_params)
        if self.request.query_params.get('search'):
            return PageDetailSerializer

        print("kwargs:", self.kwargs, "action:", self.action)
        if self.action == 'list':
            return PageListSerializer
        elif self.action == 'retrieve':
            return PageDetailSerializer
        elif self.action == 'create':
            return PageDetailSerializer
        # return serializers.Serializer
        return PageDetailSerializer