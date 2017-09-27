from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=1000)
    authors = models.CharField(max_length=5000)
    content = models.CharField(max_length=50000)
    url = models.CharField(max_length=800)
    date = models.DateTimeField('date')
    event_id = models.ManyToManyField('summarize.Event',
                                      related_name='article')

    class Meta():
        app_label = 'scraper'
