"""Newspaper is a library for extracting & curating articles."""
import newspaper
import datetime
from newspaper import news_pool
# List of article dictionaries.
# Dicts must contain Author, Url, Body text and datetime added
article_list = []


def get_source_list():
    """Build newspaper objects for scraping. Returns a list."""
    # Build Papers Objects to be downloaded and parsed for data extraction.
    tech_crunch = newspaper.build(
        'https://www.techcrunch.com/', memoize_articles=False)
    fox = newspaper.build('https://www.foxnews.com/', memoize_articles=False)
    nytimes = newspaper.build('http://nytimes.com', memoize_articles=False)
    wsj = newspaper.build('http://wsj.com', memoize_articles=False)
    bbc = newspaper.build('http://bbcnews.com', memoize_articles=False)
    cnn = newspaper.build('http://cnn.com', memoize_articles=False)
    breit = newspaper.build('http://breitbart.com', memoize_articles=False)

    papers = [tech_crunch, fox, nytimes, wsj, bbc, cnn, breit]
    return papers


def scrape(sources):
    """Scrape the source article."""
    for article in sources.articles:
        article.download()
        article.parse()
        article_obj = dict()
        print(article.title)
        print(article.text)
        print(article.authors)
        article_obj.update({'title': article.title,
                            'body': article.text,
                            'author': article.authors,
                            'datetime': datetime.datetime.now()})
    article_list.append(article_obj)


def display_data():
    """Output the scraper results to console."""
    for article in article_list:
        for key in article:
            print(article[key])


if __name__ == "__main__":
    sources = get_source_list()
    scrape(sources)
    display_data()
