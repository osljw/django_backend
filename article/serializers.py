from rest_framework.serializers import ModelSerializer
from .models import Article

class ArticleSerializer(ModelSerializer):

    class Meta:
        model = Article
        fields = [
            "id",
            "auth",
            # "tags",
            "title",
            "body",
            "create_time",
            "update_time",
        ]

# class ArticleCategorySerializer(ModelSerializer):
    
#     class Meta:
#         model = ArticleCategory
#         fields = "__all__"