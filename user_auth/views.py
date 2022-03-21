from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework.authtoken.views import APIView,AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
# 用户注册
class Register(APIView):
    def post(self,request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        if User.objects.filter(username=username).exists():
            resp = {
                'status':False,
                'data':'用户名已被注册'
            }
        else:
            user = User.objects.create_user(username=username,password=password)
            token, created = Token.objects.get_or_create(user=user)
            resp = {
                'status':True,
                'token': token.key,
                'user_id': user.pk,
                'user_name': user.username,
            }
        return Response(resp)

# 用户登录
class Login(APIView):

    def post(self, request, *args, **kwargs):
        print("Login request:", request.data)
        serializer = AuthTokenSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=False)
        if 'user' not in serializer.validated_data:
            return Response({
                'status': False,
            })
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'status':True,
            'token': token.key,
            'user_id': user.pk,
            'user_name':user.username,
        })

class UserList(APIView):
    def get(self, request, *args, **kwargs):
        print("UserList request:", request, request.query_params.dict())
        params = request.query_params.dict()

        print("UserList:", User.objects.all())

        pagesize = int(params['pagesize'])
        if pagesize == 0:
            pagesize = 2

        pagenum = int(params['pagenum']) - 1

        # if User.objects.all():
        #     resp = {
        #         'status':False,
        #         'data':'用户名已被注册'
        #     }
        # else:
        user_list = {
            'status': True,
            'data': {
                'user_list': [],
                'meta': {
                    'total': 0,
                    'pagenum': pagenum,
                    'pagesize': pagesize,
                    'pagesizes': [1, 2, 4, 8]
                }
            }
        }

        data = User.objects.all()
        for id, user in enumerate(data[pagenum*pagesize:(pagenum+1)*pagesize]):
            user_list['data']['user_list'].append({
                'id': id,
                'name': user.username
            })

        user_list['data']['meta']['total'] = len(data)

        print("user_list return:", user_list)
        return Response(user_list)