from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import LeaderboardSerializer
from .models import Leaderboard
from django.utils.crypto import get_random_string

class LeaderboardViewSet(viewsets.ViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

    def list(self, request):
        limit = int(request.query_params.get('limit', 100))
        descending = request.query_params.get('descending', 'true').lower() == 'true'

        order_by = '-score' if descending else 'score'
        queryset = Leaderboard.objects.order_by(order_by)[:limit]

        serializer = LeaderboardSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        
        leaderboard_id = get_random_string(length=8)
        # Get the request data as a dictionary, handling both form data and JSON data
        if request.content_type == 'multipart/form-data':
            print("post multipart/form-data:", request.POST.dict())
            data = {'id': leaderboard_id, **request.POST.dict()}
        else:
            print("post:", request.data)
            data = {'id': leaderboard_id, **request.data}
        serializer = self.serializer_class(data=data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        leaderboard = get_object_or_404(self.queryset, id=pk)
        # serializer = self.serializer_class(leaderboard)
        serializer = self.serializer_class(leaderboard)
        return Response(serializer.data)

    def update(self, request, pk=None):
        leaderboard = get_object_or_404(self.queryset, id=pk)
        serializer = self.serializer_class(leaderboard, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        leaderboard = get_object_or_404(self.queryset, id=pk)
        leaderboard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
