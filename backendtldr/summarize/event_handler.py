"""
Handles the creation/updating of events.
Pairs articles from the Article table to an Event.
Finds Events needing summarization and passes it to the Summary Handler
"""
from django.utils import timezone
from summarize.models import Event
from scraper.models import Article

def generate_events_from_articles():
    """Creates an empty event object with fields taken from article objects."""
    # Loop through all the articles in the article table.
    for article in Article.objects.all():
        # article = e is questionable
        e = Event(event_title = e.title, summaries = None,  articles = e, no_tags = None,
                  tags = None, last_updated = timezone.now(), needs_summary = True)
        e.save()
