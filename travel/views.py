from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Travel, Order
from .serializers import TravelSerializer, OrderSerializer
from django.utils.crypto import get_random_string

class TravelViewSet(viewsets.ViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def get_queryset(self):
        queryset = Travel.objects.all()
        is_popular = self.request.query_params.get('is_popular', '').lower() in ['true', '1']  # 获取请求参数中的 is_popular 字段，并将其转换为布尔类型
        print("is_popular", is_popular)
        if is_popular:  # 如果请求参数中包含的 is_popular 字段为真，则只返回热门订单
            queryset = Travel.objects.filter(is_popular__exact=True)

        destination = self.request.query_params.get('destination', None)
        if destination is not None:
            queryset = queryset.filter(destination__icontains=destination)

        start_time_gt = self.request.query_params.get('start_time_gt', None)
        if start_time_gt is not None:
            queryset = queryset.filter(start_time__gte=start_time_gt)

        start_time_lt = self.request.query_params.get('start_time_lt', None)
        if start_time_lt is not None:
            queryset = queryset.filter(start_time__lte=start_time_lt)

        price_min = self.request.query_params.get('price_min', None)
        if price_min is not None:
            queryset = queryset.filter(price__gte=price_min)

        price_max = self.request.query_params.get('price_max', None)
        if price_max is not None:
            queryset = queryset.filter(price__lte=price_max)


        return queryset

    def list(self, request):
        queryset = self.get_queryset()

        # descending = request.query_params.get('descending', 'true').lower() == 'true'
        # order_by = '-score' if descending else 'score'
        # queryset = queryset.order_by(order_by)
        
        # limit = int(request.query_params.get('limit', -1))
        # queryset = queryset[:limit]

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
        print("travel retrieve")
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

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer