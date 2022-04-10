from rest_framework.serializers import ModelSerializer
from .models import Banner

class BannerSerializer(ModelSerializer):

    class Meta:
        model = Banner
        fields = ["img_url", "link_url"]