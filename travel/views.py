from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.crypto import get_random_string
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Travel, Order, City
from .serializers import TravelSerializer, OrderSerializer

class FilterView(APIView):
    def get(self, request, *args, **kwargs):
        # 获取参数：request.GET.get('param_name')

        # 获取所有唯一的城市名称
        unique_cities = City.objects.values_list('name', flat=True).distinct()  

        return Response({'unique_cities': unique_cities})

class TravelViewSet(viewsets.ViewSet):
    
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        queryset = Travel.objects.all()
        is_popular = self.request.query_params.get('is_popular', '').lower() in ['true', '1']  # 获取请求参数中的 is_popular 字段，并将其转换为布尔类型
        print("is_popular", is_popular)
        if is_popular:  # 如果请求参数中包含的 is_popular 字段为真，则只返回热门订单
            queryset = Travel.objects.filter(is_popular__exact=True)

        destination = self.request.query_params.get('destination', None)
        print("destination", destination)
        if destination is not None:
            destinations_list = destination.split(',')
            queryset = Travel.objects.filter(cities__name__in=destinations_list)

        start_time_gt = self.request.query_params.get('start_time_gt', None)
        if start_time_gt is not None:
            queryset = queryset.filter(start_time__gte=start_time_gt)

        start_time_lt = self.request.query_params.get('start_time_lt', None)
        if start_time_lt is not None:
            queryset = queryset.filter(start_time__lte=start_time_lt)

        price = self.request.query_params.get('price', None)
        if price is not None:
            price_min, price_max = price.split('-')
            print("====price:", price_min, "max:", price_max)
            price_min = float(price_min)
            queryset = queryset.filter(price__gte=price_min)

            price_max = float(price_max)
            queryset = queryset.filter(price__lte=price_max)

        return queryset

    def get_permissions(self):
        """
        根据当前请求返回所需的权限列表。
        """
        if self.action in ('create', 'update', 'destroy'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


    def list(self, request):
        queryset = self.get_queryset()
        try:
            queryset = self.get_queryset()
        except:
            return Response({"error": "查询参数错误"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
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