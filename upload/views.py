from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

import os
# Create your views here.

def handle_uploaded_file(f, save_path):
    with open(save_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

class UploadView(APIView):
    def post(self, request, format=None):
        print("upload view:", request.FILES['file'])

        filename = request.FILES['file'].name
        save_path = os.path.join('media/upload', filename)
        handle_uploaded_file(request.FILES['file'], save_path)

        data = {
            "name": filename,
            "status": "done",
            "url": "http://localhost:8000/" + save_path,
        }
        return Response(data=data, status=status.HTTP_200_OK)