from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import NewsSerializer
from .models import News
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .services import update_or_create_posts, get_request_params


@api_view(('GET',))
@permission_classes((AllowAny,))
def update_posts_view(request):
    """Веб-сервис обновляющий список новостей с сайта"""
    update_or_create_posts()
    return JsonResponse({'success': True})


@api_view(('GET',))
@permission_classes((AllowAny,))
def get_posts_view(request):
    """Веб сервис, который выдает список новостей из БД"""
    order, offset, limit = get_request_params(request)
    queryset = News.objects.order_by(order)[offset:limit + offset]
    seializer = NewsSerializer(
        instance=queryset,
        many=True
    )
    return Response(seializer.data)