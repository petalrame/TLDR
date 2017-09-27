from __future__ import unicode_literals
from django.db import models
from summarize.models import Event


class Article(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    url = models.CharField(max_length=300)
    date = models.DateTimeField('date')
    event_id = models.ManyToManyField(Event)

    class Meta():
        app_label = 'scraper'
