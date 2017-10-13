from __future__ import unicode_literals
from django.db import models
from tagulous.models import TagField


class Article(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)
    url = models.CharField(max_length=300)
    date = models.DateTimeField('date')
    event_id = models.ManyToManyField('summarize.Event',
                                      related_name='article')
    tags = TagField()


    class Meta():
        app_label = 'scraper'
