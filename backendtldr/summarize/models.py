from django.db import models
from tagulous.models import TagField


# Event Model
class Event(models.Model):
    event_title = models.CharField(max_length=500)
    summaries = models.CharField(max_length=40000)
    articles = models.ManyToManyField("scraper.Article",
                                      related_name="events")
    no_tags = models.IntegerField(default=100)
    tags = TagField()
    last_updated = models.DateTimeField('date')
    needs_summary = models.BooleanField(default=True)

    class Meta():
        app_label = 'summarize'
