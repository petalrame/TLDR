"""Scrape data (urls, authors, content, titles) from articles."""
import newspaper
from scraper.models import article
from django.utils import timezone
# List of article dictionaries.
# Dicts must contain Author, Url, Body text and datetime added
article_list = []


def get_source_list():
    """Build newspaper objects for scraping. Returns a list."""
    # Build Papers Objects to be downloaded and parsed for data extraction.
    tech_crunch = newspaper.build(
        'https://www.techcrunch.com/', memoize_articles=False, language='en')
    fox = newspaper.build('https://www.foxnews.com/', memoize_articles=True, language='en')
    nytimes = newspaper.build('http://nytimes.com', memoize_articles=True, language='en')
    wsj = newspaper.build('http://wsj.com', memoize_articles=True, language='en')
    bbc = newspaper.build('http://bbcnews.com', memoize_articles=True, language='en')
    cnn = newspaper.build('http://cnn.com', memoize_articles=True, language='en')
    breit = newspaper.build('http://breitbart.com', memoize_articles=True, language='en')
    papers = [tech_crunch, fox, nytimes, wsj, bbc, cnn, breit]
    return papers


def scrape(sources):
    """Scrape the source article."""
    for source in sources:
        for news_article in source.articles:
            try:
                news_article.download()
                news_article.parse()
            except:
                break
            title = ''.join(news_article.title)
            content = ''.join(news_article.text)
            date = timezone.now()
            authors = ''
            url = ''.join(source.url)
            try:
                for author in news_article.authors:
                    authors = author + ', ' + authors
            except:
                print("")
            print(content)
            a = article(title = title,authors = authors ,content = content,url = url,date = date)
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