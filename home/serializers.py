from rest_framework.serializers import ModelSerializer
from .models import (
    Banner,
    NarBar,
)

class BannerSerializer(ModelSerializer):

    class Meta:
        model = Banner
        fields = ["img_url", "link_url"]


class NarBarSerializer(ModelSerializer):

    class Meta:
        model = NarBar
        fields = ["title", "link_url", "is_insite"]