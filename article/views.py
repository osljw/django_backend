
import markdown
from markdown.extensions.toc import TocExtension

from django.utils.text import slugify
from rest_framework.authtoken.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.filter(is_show=True)
    # serializer_class = ArticleListSerializer

    def get_serializer_class(self):
        if 'pk' in self.kwargs:  # URL中包含了文章ID，使用ArticleDetailSerializer
            return ArticleDetailSerializer
        return ArticleListSerializer

    def create(self, request):
        
        # leaderboard_id = get_random_string(length=8)
        # # Get the request data as a dictionary, handling both form data and JSON data
        # if request.content_type == 'multipart/form-data':
        #     print("post multipart/form-data:", request.POST.dict())
        #     data = {'id': leaderboard_id, **request.POST.dict()}
        # else:
        #     print("post:", request.data)
        #     data = {'id': leaderboard_id, **request.data}
        data = request.data
        print("post create:", request.data)

        serializer = self.serializer_class(data=data, context={'request': request})
        # serializer.is_valid(raise_exception=True)
        serializer.is_valid(raise_exception=False)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
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
