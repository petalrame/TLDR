"""Newspaper is a library for extracting & curating articles."""
import newspaper
from newspaper import news_pool
# List of article dictionaries.
# Dicts must contain Author, Url, Body text and datetime added
article_list = []


def initialize_scraper():
    """Build newspaper objects and parse and download them."""
    # Build Papers Objects to be downloaded and parsed for data extraction.
    fox = newspaper.build('https://www.foxnews.com/', memoize_articles=False)
    nytimes = newspaper.build('http://nytimes.com', memoize_articles=False)
    wsj = newspaper.build('http://wsj.com', memoize_articles=False)
    bbc = newspaper.build('http://bbcnews.com', memoize_articles=False)
    cnn = newspaper.build('http://cnn.com', memoize_articles=False)
    breit = newspaper.build('http://breitbart.com', memoize_articles=False)

    papers = [fox, nytimes, wsj, bbc, cnn, breit]
    # news_pool.set(papers, threads_per_source=2)  # (3*2) = 6 threads total
    # news_pool.join()
    for source in papers:
        for article in source.articles:
            scrape(article)


def scrape(article):
    """Scrape the source article."""
    article.download()
    article.parse()
    article_obj = dict()
    article_obj.update({'title': article.title,
                        'body': article.text,
                        'author': article.authors,
                        'datetime': ""})

    article_list.append(article_obj)


def display_data():
    """Output the scraper results to console."""
    for article in article_list:
        for key in article:
            print(article[key])


if __name__ == "__main__":
    initialize_scraper()
    display_data()
