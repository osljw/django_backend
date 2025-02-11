from django.shortcuts import render

# from django.contrib.auth.models import User

from rest_framework.authtoken.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework.generics import CreateAPIView
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer

# Create your views here.
# 用户注册
# class Register(APIView):
#     def post(self,request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         if User.objects.filter(username=username).exists():
#             resp = {
#                 'status':False,
#                 'data':'用户名已被注册'
#             }
#         else:
#             user = User.objects.create_user(username=username,password=password)
#             token, created = Token.objects.get_or_create(user=user)
#             resp = {
#                 'status':True,
#                 'token': token.key,
#                 'user_id': user.pk,
#                 'user_name': user.username,
#             }
#         return Response(resp)
    
'''
{
    "username": "123",
    "password": "123"
}
'''
class Register(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = []

    def post(self,request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            resp = {
                'status_code': -1,
                'msg': '用户名【{}】已注册'.format(username)
            }
        else:
            user = User.objects.create_user(username=username,password=password)
            # # token, created = Token.objects.get_or_create(user=user)
            # payload = jwt_payload_handler(user)
            # token = jwt_encode_handler(payload)
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            resp = {
                'status_code': 0,
                'user_id': user.pk,
                'user_name': user.username,
                'access_token': access_token,
            }

        return Response(resp)

# 用户登录
# class Login(APIView):

#     def post(self, request, *args, **kwargs):
#         print("Login request:", request.data)
#         serializer = AuthTokenSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=False)
#         if 'user' not in serializer.validated_data:
#             return Response({
#                 'status': False,
#             })
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'status':True,
#             'token': token.key,
#             'user_id': user.pk,
#             'user_name':user.username,
#         })

# class UserList(APIView):
#     authentication_classes = [JSONWebTokenAuthentication,]
#     # 权限控制
#     permission_classes = [IsAuthenticated,]
#     def get(self, request, *args, **kwargs):
#         print("UserList request:", request, request.query_params.dict())
#         params = request.query_params.dict()

#         print("UserList:", User.objects.all())

#         # pagesize = int(params['pagesize'])
#         pagesize = 2
#         if pagesize == 0:
#             pagesize = 2

#         # pagenum = int(params['pagenum']) - 1
#         pagenum = 2

#         # if User.objects.all():
#         #     resp = {
#         #         'status':False,
#         #         'data':'用户名已被注册'
#         #     }
#         # else:
#         user_list = {
#             'status': True,
#             'data': {
#                 'user_list': [],
#                 'meta': {
#                     'total': 0,
#                     'pagenum': pagenum,
#                     'pagesize': pagesize,
#                     'pagesizes': [1, 2, 4, 8]
#                 }
#             }
#         }

#         data = User.objects.all()
#         for id, user in enumerate(data[pagenum*pagesize:(pagenum+1)*pagesize]):
#             user_list['data']['user_list'].append({
#                 'id': id,
#                 'name': user.username
#             })

#         user_list['data']['meta']['total'] = len(data)

#         print("user_list return:", user_list)
#         return Response(user_list)