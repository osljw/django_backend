# Create your views here.

from rest_framework.generics import ListAPIView
from .models import (
    Banner,
    NarBar,
)
from .serializers import (
    BannerSerializer,
    NarBarSerializer,
)


class BannerView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True).order_by("orders")
    serializer_class = BannerSerializer


class TopNavView(ListAPIView):
    queryset = NarBar.objects.filter(is_show=True, position=1).order_by("orders")
    serializer_class = NarBarSerializer

class BottomNavView(ListAPIView):
    queryset = NarBar.objects.filter(is_show=True, position=2).order_by("orders")
    serializer_class = NarBarSerializer