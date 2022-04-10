from django.shortcuts import render

# Create your views here.

from rest_framework.generics import ListAPIView
from .models import Banner
from .serializers import BannerSerializer

class BannerView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True).order_by("orders")
    serializer_class = BannerSerializer