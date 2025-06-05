from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Collection, CollectionCategory
from user_auth.models import User


class CollectionCategoryListSerializer(ModelSerializer):
    # articles = CollectionSerializer(many=True, read_only=True)
    total = serializers.IntegerField(
        source='articles_count',  # 对应注解字段
        read_only=True,
        help_text='该分类下的文章数量'
    )

    class Meta:
        model = CollectionCategory
        fields = '__all__'
        # read_only_fields = ['create_time', 'update_time']

class CollectionCategoryDetailSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()
    # total = serializers.IntegerField(
    #     source='articles_count',
    #     read_only=True,
    #     help_text='分类下的文章数量'
    # )

    class Meta:
        model = CollectionCategory
        fields = ['id', 'name', 'create_time', 'articles']

    def get_articles(self, obj):
        return CollectionSerializer(
            obj.articles.all().order_by('-create_time'),
            many=True,
            context=self.context
        ).data

class CollectionCategorySerializer(ModelSerializer):
    class Meta:
        model = CollectionCategory
        # fields = '__all__'
        fields = ['id', 'name']
        read_only_fields = ['id']  # 确保ID只读

# 获取文章列表
class CollectionSerializer(ModelSerializer):
    categories = CollectionCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Collection
        # fields = '__all__'
        fields = ['id', 'auth', 'categories', 'title', 'type', 'create_time', 'update_time', 'is_show']
        read_only_fields = ['create_time', 'update_time']


    def create(self, validated_data):
        print("=====CollectionListSerializer create:", validated_data)
        obj = Collection(**validated_data)
        obj.auth = User()
        obj.save()
        return obj

# 获取文章，创建文章
class CollectionDetailSerializer(serializers.ModelSerializer):
    auth = serializers.SerializerMethodField()
    # 写入字段（处理ID数组）
    categories = serializers.PrimaryKeyRelatedField(
        queryset=CollectionCategory.objects.all(),
        many=True,
        write_only=True  # 只在写入时生效
    )
    
    # 读取字段（自动生成详细信息）
    categories_info = CollectionCategorySerializer(
        source='categories',
        many=True,
        read_only=True
    )


    class Meta:
        model = Collection
        fields = '__all__'
        read_only_fields = ('auth',)


    def validate(self, data):
        """
        Check that start is before finish.
        """
        print("validate", data)
        return data
    
    def get_auth(self, obj):
        return obj.auth.username
    
    def to_representation(self, instance):
        """ 重写输出格式 """
        data = super().to_representation(instance)
        # 将 categories_info 重命名为 categories
        data['categories'] = data.pop('categories_info')
        return data 

    def update(self, instance, validated_data):
        """处理分类关系更新"""
        categories = validated_data.pop('categories', None)
        if categories is not None:
            instance.categories.set(categories)
        return super().update(instance, validated_data)

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

        article = Collection.objects.create(auth=user, **validated_data)

        return article



