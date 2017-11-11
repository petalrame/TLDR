from __future__ import unicode_literals

from django.db import models
from tagulous.models import TagField


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    ranking = models.IntegerField()
    summary = models.TextField()
    # TODO: Foreign Key relationship with articles
    lastedited = models.DateTimeField(auto_now=False, auto_now_add=False)
    dateadded = models.DateTimeField(auto_now=False, auto_now_add=False)
    clicktraffic = models.PositiveIntegerField()
    articles = models.ManyToManyField("scraper.Article", related_name="events")
    needs_summary = models.BooleanField(default=True)
    num_tags = models.IntegerField(default=0)
    tags = TagField()

    class Meta():
        app_label = 'summarize'
