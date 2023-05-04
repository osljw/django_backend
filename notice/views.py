from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Notice

# Create your views here.

@api_view(['GET'])
def notice_view(request):
    notice = Notice.objects.filter(is_active=True).order_by('-updated_at').first()
    if notice:
        data = {
            'content': notice.content,
            'updated_at': notice.updated_at
        }
        return Response(data)
    else:
        return Response({'content': '暂无公告'})