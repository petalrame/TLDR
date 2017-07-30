"""Newspaper is a library for extracting & curating articles."""
import newspaper
# news_pool async library
from newspaper import news_pool
# Master list
articles = []


def initialize_scraper():
    """Use the Newspaper library to parse news websites for data."""
    # Build Papers
    fox = newspaper.build('https://www.foxnews.com/', memoize_articles=False)
    nytimes = newspaper.build('http://nytimes.com', memoize_articles=False)
    wsj = newspaper.build('http://wsj.com', memoize_articles=False)

    papers = [fox, nytimes, wsj]
    news_pool.set(papers, threads_per_source=2)  # (3*2) = 6 threads total
    news_pool.join()
    scrape(fox)


def scrape(source):
    """Collect article information. Takes a source object as a parameter."""
    for article in source.articles:
        article.parse()
        # Dictionary that contains article information
        article_obj = dict()
        # Populate the dict with fields from articles
        article_obj.update({'title': article.title, 'body': article.text,
                            'author': article.authors})
        articles.append(article_obj)
        print(article.title)


def main():
    """Run scrapy.py this is called."""
    initialize_scraper()


if __name__ == "__main__":
    main()
