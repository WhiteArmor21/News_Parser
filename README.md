# Django News Parser
## Launch instructions:
- in main/.env type your MYSQL passwords
- in core catalog (contains files : Dockerfile, docker-compose.yml, manage.py,...)
- use command "docker-compose up -d --build"
- since that moment, the service will be available by url "http://localhost:8000/"
## Service methods:
### Show posts method:
(http://localhost:8000/posts)
Show saved posts from database in json format:
### Example
    {
        "id": 1,
        "title": "Webcams aren't good enough",
        "url": "https://reincubate.com/support/how-to/why-are-webcams-bad/",
        "created": "2022-06-20T00:00:01.047776+03:00"
    },
    {
        "id": 2,
        "title": "The brain has a ‘low-power mode’ that blunts our senses",
    ...
Can be sorted and filtered by extra params:
- order (sort posts by order field, default: "created"),
- offset (skip the specified number of posts, default: 0),
- limit (the number of posts displayed on the page, default: 5)
### Forced update method:
(http://localhost:8000/update)
Parse posts from website, updates them in database and then returns json response ({'success': True})
### The service is also able to update posts automatically using Celery
- By default, the update occurs every 10 minutes, but you can change this setting in the file settings.py
- On the last lines of the file, you can replace the value passed to the crontab() function
### Example
    crontab() - to update every minute.
    crontab(minute=0, hour=0) - to update daily at midnight.
    crontab(minute='*/15') - to update every 15 minutes.
    ...
more Examples at https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#:~:text=Meaning-,crontab(),-Execute%20every%20minute
