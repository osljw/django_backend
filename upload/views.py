from rest_framework import generics, status
from rest_framework.views import APIView
from django.http import JsonResponse

import os
import hashlib
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
            "location": "http://localhost:8000/" + save_path,
        }
        return JsonResponse(data=data, status=status.HTTP_200_OK)