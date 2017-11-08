"""
Handles the creation/updating of events.
Pairs articles from the Article table to an Event.
Finds Events needing summarization and passes it to the Summary Handler
"""
from django.utils import timezone
from summarize.models import Event
from scraper.models import Article
from datetime import datetime

def generate_events_from_articles():
    """Creates an empty event object with fields taken from article objects."""
    # Loop through all the articles in the article table.
    articles = Article.objects.all()
    for article in articles:
        # Check if an event already exists for a given article
        if Event.objects.all().filter(articles=article) != None:
            continue
        # Create an event object with attributes from the article
        e = Event(title = article.title, ranking=0, summary=article.content, lastedited=datetime.now(), dateadded=datetime.now(),
		clicktraffic=0, needs_summary=True, num_tags=1, tags=article.tags)

        # Save the data to the database
        e.save()
        e.articles.add(article)
    Article.objects.all().delete()
