from django.db import models


class News(models.Model):
    """Новость с сайта - набор материалов по конкретной новости"""
    title = models.CharField('Заголовок новости', max_length=255)
    url = models.URLField('Ссылка на новость', max_length=255)
    created = models.DateTimeField('Дата и время сохранения новости в БД')

    class Meta:
        db_table = 'news'
