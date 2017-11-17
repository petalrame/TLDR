"""Scrape data (urls, authors, content, titles) from articles."""
import sys
sys.path.append("newspaper-0.1.0.7")
import newspaper
from scraper.models import Article
from django.utils import timezone
# import event creation function from summarize app
from summarize import event_handler
# List of article dictionaries.
# Dicts must contain Author, Url, Body text and datetime added
article_list = []


def get_source_list():
    """Build newspaper objects for scraping. Returns a list."""
    # Build Papers Objects to be downloaded and parsed for data extraction.
    tech_crunch = newspaper.build(
        'https://www.techcrunch.com/', memoize_articles=False, language='en')
    fox = newspaper.build(
        'https://www.foxnews.com/', memoize_articles=False, language='en')
    nytimes = newspaper.build(
        'http://nytimes.com', memoize_articles=True, language='en')
    wsj = newspaper.build(
        'http://wsj.com', memoize_articles=True, language='en')
    bbc = newspaper.build(
        'http://bbcnews.com', memoize_articles=True, language='en')
    cnn = newspaper.build(
        'http://cnn.com', memoize_articles=True, language='en')
    ap = newspaper.build(
        'https://www.ap.org/en-us/', memoize_articles=True, language='en')
    papers = [fox, nytimes, wsj, bbc, cnn, ap]
    return papers


def scrape(sources):
    """Scrape the source article."""
    for source in sources:
        for news_article in source.articles:
            try:
                #print("Downloading")
                news_article.download()
                #print("Parsing")
                news_article.parse()
                #print("NLP")
                news_article.nlp()
            except:
                print("Failed article for:", news_article)
                continue
            if news_article.title is not None:
                title = ''.join(news_article.title)
            else:
                continue
            content = ''.join(news_article.text)
            date = timezone.now()
            authors = ""
            url = ''.join(news_article.url)
            try:
                for author in news_article.authors:
                    authors = format_author(author) + ', ' + authors
            except:
                continue
            # Call newspaper NLP...This call is very expensive,
            # and will be replaced by a better tagging implementation
            # fetch "tags"
            tags = ','.join(news_article.keywords)
            a = Article(title=title, authors=authors,
                        content=content, url=url, date=date, tags=tags)

            # save the article to the database
            try:
                #print("Paring and Summarizing")
                a.save()
                event_handler.generate_events_from_articles()
            except:
                print("There was a problem saving", a, "to db")


def format_author(author):
    formatted_author = author
    if "Hour Ago" in author:
        formatted_author = formatted_author.replace("Hour Ago", "")
    if "Hours Ago" in author:
        formatted_author = formatted_author.replace("Hours Ago", "")
    if "Minutes Ago" in author:
        formatted_author = formatted_author.replace("Minutes Ago", "")
    if "Seconds Ago" in author:
        formatted_author = formatted_author.replace("Seconds Ago", "")
    return formatted_author


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
    #print("Summarizaing")
    #summary_handler.run_summary()
    print("Scraper/Summ has completed.")


if __name__ == "__main__":
    run_scraper()
