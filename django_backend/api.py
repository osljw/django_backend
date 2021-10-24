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
