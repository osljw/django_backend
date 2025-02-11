from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Article, ArticleCategory

class ArticleCategorySerializer(ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = '__all__'

class ArticleSerializer(ModelSerializer):
    categories = ArticleCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['create_time', 'update_time']


class ArticleCategoryListSerializer(ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    # article_titles = serializers.SerializerMethodField()
    # def get_article_titles(self, obj):
    #     return [article.title for article in obj.articles.all()]

    class Meta:
        model = ArticleCategory
        fields = '__all__'
        # read_only_fields = ['create_time', 'update_time']