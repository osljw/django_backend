from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .models import Museum
from .serializers import MuseumSerializer
# Create your views here.


class MuseumListView(ListAPIView):
    queryset = Museum.objects.all()
    serializer_class = MuseumSerializer