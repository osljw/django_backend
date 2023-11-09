from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Article

class ArticleListSerializer(ModelSerializer):
    auth = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        fields = ['id', 'auth', 'title', 'create_time', 'update_time', 'is_show']
        read_only_fields = ['create_time', 'update_time']

    def get_auth(self, obj):
        return obj.auth.username
    
class ArticleDetailSerializer(serializers.ModelSerializer):
    auth = serializers.SerializerMethodField()
    
    class Meta:
        model = Article
        fields = '__all__'

    def get_auth(self, obj):
        return obj.auth.username
    
# class ArticleCategorySerializer(ModelSerializer):
    
#     class Meta:
#         model = ArticleCategory
#         fields = "__all__"