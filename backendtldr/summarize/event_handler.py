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
        # Create an event object with attributes from the article
        e = Event(event_title = article.title, summaries = None,  articles = article, no_tags = None,
                  tags = None, last_updated = timezone.now(), needs_summary = True)
        # Save the data to the database
        e.save()
        # Set the event_id of the article to the event it was just created from
        article.event_id = e.id
