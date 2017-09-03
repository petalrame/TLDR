"""Scrape data (urls, authors, content, titles) from articles."""
import newspaper
from models import article
from django.utils import timezone
# List of article dictionaries.
# Dicts must contain Author, Url, Body text and datetime added
article_list = []


def get_source_list():
    """Build newspaper objects for scraping. Returns a list."""
    # Build Papers Objects to be downloaded and parsed for data extraction.
    tech_crunch = newspaper.build(
        'https://www.techcrunch.com/', memoize_articles=False)
    fox = newspaper.build('https://www.foxnews.com/', memoize_articles=True)
    nytimes = newspaper.build('http://nytimes.com', memoize_articles=True)
    wsj = newspaper.build('http://wsj.com', memoize_articles=True)
    bbc = newspaper.build('http://bbcnews.com', memoize_articles=True)
    cnn = newspaper.build('http://cnn.com', memoize_articles=True)
    breit = newspaper.build('http://breitbart.com', memoize_articles=True)
    papers = [tech_crunch, fox, nytimes, wsj, bbc, cnn, breit]
    return papers


def scrape(sources):
    """Scrape the source article."""
    for source in sources:
        for article in source.articles:
            article.download()
            article.parse()
            a = article(title = ''.join(article.title), authors = ''.join(article.authors), content = ''.join(article.text),date = timezone.now())
            a.save()


def display_data():
    """Output the scraper results to console."""
    for article in article_list:
        for key in article:
            print(article[key])


def run_scraper():
    """Call all necessary scraper functions."""
    print("Running...")
    sources = get_source_list()
    scrape(sources)
    print("Scraper has completed.")


if __name__ == "__main__":
    run_scraper()