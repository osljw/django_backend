from rest_framework.serializers import ModelSerializer
from .models import Museum

class MuseumSerializer(ModelSerializer):

    class Meta:
        model = Museum
        fields = [
            "id",
            "name",
            "website",
            "areaid",
        ]