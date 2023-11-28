from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.

from .models import Page
from .serializers import PageListSerializer, PageDetailSerializer

class PageModelViewSet(ModelViewSet):
    queryset = Page.objects.filter(valid=True)
    # lookup_field = 'title'

    def get_serializer_class(self):
        # if 'title' in self.kwargs:  # URL中包含了文章ID，使用ArticleDetailSerializer
        print("kwargs:", self.kwargs, "action:", self.action)
        if self.action == 'list':
            return PageListSerializer
        elif self.action == 'retrieve':
            return PageDetailSerializer
        elif self.action == 'create':
            return PageDetailSerializer
        # return serializers.Serializer
        return PageDetailSerializer