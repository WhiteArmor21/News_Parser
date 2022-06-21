from .models import News
from .serializers import NewsSerializer
from .parser import collect_data_from_news_site
import json
from celery import shared_task


def get_request_params(request):
    """Получает дополнительные параметры из запроса"""
    order = request.GET.get("order", "created")
    if order not in ['title', 'url', 'created', '-title', '-url', '-created']:
        order = 'created'
    offset = int(request.GET.get("offset", 0))
    if offset < 0:
        offset = 0
    limit = int(request.GET.get("limit", 5))
    if limit > 30 or limit < 0:
        limit = 30
    return order, offset, limit


@shared_task
def update_or_create_posts() -> None:
    """Обновляет все записи в БД, если записей нет, создает новые"""
    data = json.loads(collect_data_from_news_site())
    pk = 1
    for item in data.values():
        if News.objects.filter(pk=pk):
            _update_post(item, pk)
        else:
            _create_post(item)
        pk += 1


def _update_post(item, pk) -> None:
    """Обновляет запиcь c идентификатором pk"""
    News.objects.filter(pk=pk).update(url=item['url'], title=item['title'], created=item['created'])


def _create_post(item) -> None:
    """Создает новую запись в БД"""
    news_object = NewsSerializer(data=item)
    news_object.is_valid(raise_exception=True)
    news_object.save()


