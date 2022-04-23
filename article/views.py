
import markdown
from markdown.extensions.toc import TocExtension

from django.utils.text import slugify
from rest_framework.authtoken.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .models import Article
from .serializers import ArticleSerializer

class ArticleListView(ListAPIView):
    queryset = Article.objects.filter(is_show=True)
    serializer_class = ArticleSerializer

class ArticleDetailView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            # 'markdown.extensions.toc',
            TocExtension(slugify=slugify),
        ])
        article.body = md.convert(article.body)
        serializer = ArticleSerializer(article)
        d = serializer.data
        d['toc'] = md.toc
        print(d)
        # 返回 Json 数据
        # return Response(serializer.data)
        return Response(d)
