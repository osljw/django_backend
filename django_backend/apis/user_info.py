from django.http import HttpResponse

import json

def user_info(request):
    d = {}
    d['data'] = [
        {
            'id': 0,
            'name': "用户管理",
            'date': "2021",
            'status': True
        },
        {
            "id": 1,
            'name': "权限管理",
            'date': "2020",
            'status': False
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