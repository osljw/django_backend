from rest_framework import generics, status
from rest_framework.views import APIView
from django.http import JsonResponse
from django.http import HttpResponse
from django.views import View

import os
import hashlib
import requests
from urllib.parse import unquote
# Create your views here.

def handle_uploaded_file(f, save_path):
    with open(save_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class UploadView(APIView):
    def post(self, request, format=None):
        print("upload view:", request.FILES['file'])
        uploaded_file = request.FILES['file']
        file_data = uploaded_file.read()
        md5 = hashlib.md5(file_data).hexdigest()

        # filename = request.FILES['file'].name
        filename = f"{md5}.{uploaded_file.name.split('.')[-1]}"
        save_path = os.path.join('media/uploads', filename)
        handle_uploaded_file(request.FILES['file'], save_path)

        data = {
            "name": filename,
            "status": "done",
            "location": save_path,
        }
        return JsonResponse(data=data, status=status.HTTP_200_OK)
    
class ProxyView(View):
    def get(self, request, *args, **kwargs):
        # 从请求路径中获取目标 URL
        path = kwargs.get('path', '')
        # path = unquote(path)  # 处理 URL 编码

        # # 目标 URL（可以从 path 拼接或者在实际场景中进行更灵活的处理）
        # target_url = f"https://{path}"

        # 发起请求到目标 URL
        try:
            response = requests.get(path)
            content_type = response.headers.get('Content-Type', 'application/octet-stream')

            # 返回目标服务器的内容
            return HttpResponse(response.content, content_type=content_type)
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Error: {str(e)}", status=500)