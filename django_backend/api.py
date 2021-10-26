from django.http import HttpResponse

import json

def login(request):
    print("request method:", request.method)
    data = request.body.decode('utf-8')
    data = json.loads(data)
    print("data:", data)

    username = data.get('username')
    password = data.get('password')
    print("username:", username, "password:", password)

    d = {}
    if username == "admin" and password == "123456":  
        d = {
            'data': {
                'username': 'admin',
                'token': '123456',
            },
            'meta': {
                'status': 0,
                'msg': '登录成功'
            }
        }
    else: 
        d['meta'] = {
            'status': 1,
            'msg': '登录失败'
        }
    print("rsp:", d)
    return HttpResponse(json.dumps(d))


def menus(request):
    data = request.body.decode('utf-8')
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
    d['meta'] = {
        'status': 200,
        'msg': '更新成功'
    }
    return HttpResponse(json.dumps(d))
