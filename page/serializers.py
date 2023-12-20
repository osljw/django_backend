from rest_framework import serializers

from .models import Page
from user_auth.models import User

class PageListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Page
        fields = ['id', 'title', 'url', 'type', 'valid']


class PageDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Page
        fields = ['id', 'title', 'url', 'type', 'body', 'valid']


