from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Article, ArticleCategory
from user_auth.models import User

class ArticleCategorySerializer(ModelSerializer):
    class Meta:
        model = ArticleCategory
        # fields = '__all__'
        fields = ['id', 'name']

class ArticleSerializer(ModelSerializer):
    categories = ArticleCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['id', 'auth', 'categories', 'title', 'type', 'create_time', 'update_time', 'is_show']
        read_only_fields = ['create_time', 'update_time']

    def get_auth(self, obj):
        return obj.auth.username
    
    # def get_tags(self, obj):
    #     return list(obj.tags.names())

    def create(self, validated_data):
        print("=====ArticleListSerializer create:", validated_data)
        obj = Article(**validated_data)
        obj.auth = User()
        obj.save()
        return obj
    
class ArticleDetailSerializer(serializers.ModelSerializer):
    auth = serializers.SerializerMethodField()
    # tags = serializers.SerializerMethodField()

    # tags = serializers.ListField(child=serializers.CharField(), required=False)
    # auth = serializers.IntegerField(required=False)
    # tags = TagListSerializerField()

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ['id', 'title', 'body', 'type', 'auth', 'is_show']


    def validate(self, data):
        """
        Check that start is before finish.
        """
        # if data['start'] > data['finish']:
        #     raise serializers.ValidationError("finish must occur after start")
        print("validate", data)
        return data
    
    def get_auth(self, obj):
        return obj.auth.username
    
    # def get_tags(self, obj):
    #     return list(obj.tags.names())
    

    def create(self, validated_data):
        print("initial_data:", self.initial_data)
        print("validated_data:", validated_data)
        # tags_data = validated_data.pop('tags', [])  # Get the tags data
        auth_data = self.initial_data.get('auth', None)  # Get the auth data

        # Check if auth_data is provided
        if auth_data and isinstance(auth_data, dict) and 'username' in auth_data:
            auth_username = auth_data['username']
            try:
                user = User.objects.get(username=auth_username)
            except User.DoesNotExist:
                raise serializers.ValidationError('Invalid auth username')
        else:
            # Create a new user with a default username if auth_data is not provided
            user = User.objects.get_or_create(username='default_username')

        article = Article.objects.create(auth=user, **validated_data)

        # Update the tags for the article
        # if tags_data:
        #     article.tags.set(tags_data)

        return article


class ArticleCategoryListSerializer(ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)
    # article_titles = serializers.SerializerMethodField()
    # def get_article_titles(self, obj):
    #     return [article.title for article in obj.articles.all()]

    class Meta:
        model = ArticleCategory
        fields = '__all__'
        # read_only_fields = ['create_time', 'update_time']
