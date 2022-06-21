from django.urls import path
from news.views import get_posts_view, update_posts_view


urlpatterns = [
    path('update', update_posts_view),
    path('posts', get_posts_view),
]

