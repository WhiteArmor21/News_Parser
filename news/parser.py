import requests
import json
from bs4 import BeautifulSoup
from django.utils import timezone

url = 'https://news.ycombinator.com/'


def collect_data_from_news_site():
    """Собирает информацию с сайта новостей
    и возвращает ее в виде json"""
    posts = _get_news_set_from_news_website(url)
    data = _get_json_data_from_posts(posts)
    return data


def main():
    try:
        collect_data_from_news_site()
    except Exception as ex:
        print(ex)


def _get_news_set_from_news_website(url):
    """Возвращает множество новостей с вебсайта с адресом url"""
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    posts = soup.find_all(class_='titlelink')
    return posts


def _get_json_data_from_posts(posts):
    """Возвращает данные из новостей posts в формате json"""
    posts_dict = {}
    id = 0
    for post in posts:
        post_url = _validate_url(post.get('href'))
        post_title = post.text
        created = timezone.now().isoformat()
        posts_dict[id] = dict([('url', post_url), ('title', post_title), ('created', created)])
        id += 1
    return json.dumps(posts_dict)


def _validate_url(post_url):
    """Возвращает дополненный url,
     если изначальный url был ссылкой на другой объект на сайте,
     иначе, возвращет url неизменным"""
    if post_url[:4] == 'item':
        post_url = url + post_url
    return post_url


if __name__ == '__main__':
    main()