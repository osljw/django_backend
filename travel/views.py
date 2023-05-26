from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import TravelSerializer
from .models import Travel
from django.utils.crypto import get_random_string

class TravelViewSet(viewsets.ViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def list(self, request):
        queryset = Travel.objects

        # descending = request.query_params.get('descending', 'true').lower() == 'true'
        # order_by = '-score' if descending else 'score'
        # queryset = queryset.order_by(order_by)
        
        limit = int(request.query_params.get('limit', -1))
        queryset = queryset[:limit]

        serializer = TravelSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        
        Travel_id = get_random_string(length=8)
        # Get the request data as a dictionary, handling both form data and JSON data
        if request.content_type == 'multipart/form-data':
            print("post multipart/form-data:", request.POST.dict())
            data = {'id': Travel_id, **request.POST.dict()}
        else:
            print("post:", request.data)
            data = {'id': Travel_id, **request.data}
        serializer = self.serializer_class(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        Travel = get_object_or_404(self.queryset, id=pk)
        # serializer = self.serializer_class(Travel)
        serializer = self.serializer_class(Travel)
        return Response(serializer.data)

    def update(self, request, pk=None):
        Travel = get_object_or_404(self.queryset, id=pk)
        serializer = self.serializer_class(Travel, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        Travel = get_object_or_404(self.queryset, id=pk)
        Travel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
