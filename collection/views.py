
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.db.models import Count


from rest_framework.authtoken.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, filters, pagination

from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import action



from .models import Article, ArticleCategory
from .serializers import ArticleSerializer, ArticleDetailSerializer
from .serializers import ArticleCategoryListSerializer, ArticleCategoryDetailSerializer

class ArticlePagination(pagination.PageNumberPagination):
    page_size = 10  # 每页显示的记录数量
    page_size_query_param = 'page_size'  # URL 参数中控制每页记录数量的参数
    max_page_size = 100  # 每页最大记录数量

    page_query_param = 'page'  # 控制页码的查询参数名
    ordering_param = 'ordering'  # 控制排序的查询参数名

    # @method_decorator(never_cache)
    def paginate_queryset(self, queryset, request, view=None):
        ordering = request.query_params.get(self.ordering_param)
        if ordering:
            queryset = queryset.order_by(ordering)

        # 没有page参数时，不分页
        # page = request.query_params.get(self.page_query_param)
        # if page is None:
        #     return None

        return super().paginate_queryset(queryset, request, view)
    

class ArticleCategoryViewSet(ModelViewSet):
    # queryset = ArticleCategory.objects.all()
    queryset = ArticleCategory.objects.annotate(articles_count=Count('articles'))
    serializer_class = ArticleCategoryListSerializer
    # pagination_class = ArticlePagination    # 分页功能

    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ArticleCategoryListSerializer
    #     return ArticleCategoryDetailSerializer
    
    # /category/{id}/articles
    @action(detail=True, methods=['get'])
    def articles(self, request, pk=None):
        category = self.get_object()
        articles = category.articles.all().order_by('-create_time')
        paginator = ArticlePagination()
        page = paginator.paginate_queryset(articles, request, view=self)
        serializer = ArticleSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.filter(is_show=True)
    authentication_classes = [JWTAuthentication]
    # permission_classes = [AllowAny]
    pagination_class = ArticlePagination    # 分页功能
    ordering_fields = ('id', 'create_time', 'update_time')  # 定义允许排序的字段
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']

    def get_permissions(self):
        if self.action in ['retrieve', 'list']:
            permission_classes = [AllowAny]
        else:
            # permission_classes = self.permission_classes
            permission_classes = [IsAuthenticated]
        print("全部请求头:", self.request.META)  # 检查所有元数据
        print(f"Auth User: {self.request.user}")  # 查看认证用户
        print(f"Auth Header: {self.request.META.get('HTTP_AUTHORIZATION')}")  # 查看请求头
        print("article view permission:", permission_classes)
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        print("article =====user:", self.request.user, self.request.user.is_superuser)
        user = self.request.user
        
        all_param = self.request.query_params.get('all')
        print("all_param:", all_param)

        # admin backend
        if user.is_superuser:
            if all_param is not None or self.action in ["create", "update", "partial_update", "destroy"]:
                return Article.objects.all()

        queryset = Article.objects.filter(is_show=True)

        return queryset
        
    def get_serializer_class(self):
        # if 'title' in self.kwargs:  # URL中包含了文章ID，使用ArticleDetailSerializer
        print("kwargs:", self.kwargs, "action:", self.action)
        if self.action == 'list':
            # return ArticleListSerializer
            return ArticleSerializer
        elif self.action == 'retrieve':
            return ArticleDetailSerializer
        elif self.action == 'create':
            return ArticleDetailSerializer
        # return serializers.Serializer
        return ArticleDetailSerializer

    def get_ordering(self):
        """
        获取排序字段和顺序
        """
        ordering = self.request.query_params.get('ordering')
        if ordering in self.ordering_fields:
            return ordering
        return None

    def perform_update(self, serializer):
        serializer.save(auth=self.request.user)
    



