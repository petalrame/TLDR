from django.db import models


# Tag table
class Tag(models.Model):
    name = models.CharField(max_length=50)


# Event Model
class Event(models.Model):
    event_title = models.CharField(max_length=500)
    summaries = models.CharField(max_length=40000)
    articles = models.ManyToManyField("scraper.article"
                                      , verbose_name="articles"
                                      , related_name="events")
    no_tags = models.IntegerField(default=100)
    tags = models.ManyToManyField(Tag)
    last_updated = models.DateTimeField('date')
    needs_summary = models.BooleanField(default=True)
