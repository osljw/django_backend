
from markdown.extensions.toc import TocExtension


from rest_framework.authtoken.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status, filters, pagination
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer

class ArticlePagination(pagination.PageNumberPagination):
    page_size = 10  # 每页显示的记录数量
    page_size_query_param = 'page_size'  # URL 参数中控制每页记录数量的参数
    max_page_size = 100  # 每页最大记录数量

    page_query_param = 'page'  # 控制页码的查询参数名
    ordering_param = 'ordering'  # 控制排序的查询参数名

    def paginate_queryset(self, queryset, request, view=None):
        ordering = request.query_params.get(self.ordering_param)
        if ordering:
            queryset = queryset.order_by(ordering)

        page = request.query_params.get(self.page_query_param)
        if page is None:
            return None
        return super().paginate_queryset(queryset, request, view)
    

class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.filter(is_show=True)
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [AllowAny]
    pagination_class = ArticlePagination    # 分页功能
    ordering_fields = ('id', 'create_time', 'update_time')  # 定义允许排序的字段
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        print("=====user:", self.request.user, self.request.user.is_superuser)
        user = self.request.user
        
        all_param = self.request.query_params.get('all')
        print("all_param:", all_param)
        if all_param is None:
            return self.queryset

        # admin backend
        if user.is_superuser and all_param is not None:
            return Article.objects.all()
        
        return self.queryset
        
    def get_serializer_class(self):
        # if 'title' in self.kwargs:  # URL中包含了文章ID，使用ArticleDetailSerializer
        print("kwargs:", self.kwargs, "action:", self.action)
        if self.action == 'list':
            return ArticleListSerializer
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

    # def partial_update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()  # 执行保存操作
    #     print("===pathch data:", serializer.data)
    #     return Response(serializer.data)
    
    # def create(self, request):
        
    #     # leaderboard_id = get_random_string(length=8)
    #     # # Get the request data as a dictionary, handling both form data and JSON data
    #     # if request.content_type == 'multipart/form-data':
    #     #     print("post multipart/form-data:", request.POST.dict())
    #     #     data = {'id': leaderboard_id, **request.POST.dict()}
    #     # else:
    #     #     print("post:", request.data)
    #     #     data = {'id': leaderboard_id, **request.data}
    #     data = request.data
    #     print("post create:", request.data)
    #     print("serializer_class:", self.get_serializer)

    #     serializer = self.get_serializer(data=data, context={'request': request})
    #     # serializer.is_valid(raise_exception=True)
    #     serializer.is_valid(raise_exception=False)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    
# class ArticleListView(ListAPIView):
#     queryset = Article.objects.filter(is_show=True)
#     serializer_class = ArticleSerializer


# class ArticleDetailView(APIView):

#     def get(self, request, pk):
#         article = Article.objects.get(pk=pk)

#         md = markdown.Markdown(
#             extensions=[
#                 'markdown.extensions.extra',
#                 'markdown.extensions.codehilite',
#                 'mdx_math',
#                 # 'markdown.extensions.toc',
#                 TocExtension(slugify=slugify),
#             ],
#             extension_configs = { 
#                     'mdx_math': {'enable_dollar_delimiter': True} 
#             }
#         )
#         md.convert(article.body)
#         # article.body = md.convert(article.body)
        
#         serializer = ArticleSerializer(article)
#         d = serializer.data
#         d['toc'] = md.toc
#         print(d)
#         # 返回 Json 数据
#         # return Response(serializer.data)
#         return Response(d)
