from django.shortcuts import render

from rest_framework.authtoken.views import APIView
from rest_framework.response import Response

class UserMenu(APIView):
    def get(self, request, *args, **kwargs):
        d = {}
        d['data'] = [
            {
                'id': 0,
                'name': "用户管理",
                "children": [
                    {
                        "id": 0,
                        "name": "用户列表",
                        "path": "user"
                    }
                ]
            },
            {
                "id": 1,
                'name': "权限管理",
                "children": [
                    {
                        "id": 0,
                        "name": "权限列别",
                        "path": "user"
                    }
                ]
            },
            {
                "id": 2,
                'name': "商品管理"
            },
            {
                "id": 3,
                "name": "订单管理"
            },
            {
                "id": 4,
                "name": "数据统计"
            }
        ]
        d['status'] = True
        print("UserMenu:", d)
        return Response(d)