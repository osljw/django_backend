from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters

# Create your views here.

from .models import Page
from .serializers import PageListSerializer, PageDetailSerializer

class PageModelViewSet(ModelViewSet):
    queryset = Page.objects.filter(valid=True)

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    #ordering_fields = [ 'field1', 'field2' ]  # 可以根据这里的字段进行排序
    search_fields = ['url']  # 可以根据这里的字段进行搜索

    def get_queryset(self):
        # print("=====user:", self.request.user)
        user = self.request.user
        query = self.request.query_params.get('query')
        
        
        return Page.objects.all()
    
        if user.is_superuser:
            return Page.objects.all()
        else:
            return Page.objects.filter(valid=True)
        

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