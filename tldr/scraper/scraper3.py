import newspaper
#news_pool async library
from newspaper import news_pool

def scrape():
    """Uses the Newspaper library to parse news websites for content"""
    #Master list
    articles = []
    #Build Papers
    usa = newspaper.build('https://www.usatoday.com/',memoize_articles=False)
    nytimes = newspaper.build('http://nytimes.com',memoize_articles=False)
    wsj = newspaper.build('http://wsj.com',memoize_articles=False)

    papers = [usa, nytimes, wsj]
    news_pool.set(papers, threads_per_source=2) # (3*2) = 6 threads total
    news_pool.join()

    #USA Today
    for article in usa.articles:
        article.parse()
        #Article object init
        article_obj = dict()
        #Fill the object
        article_obj.update({'title':article.title})
        article_obj.update({'body':article.text})
        article_obj.update({'author':article.authors})
        articles.append(article_obj)
    #NY Times
    for article in nytimes.articles:
        article.parse()
        #Article object init
        article_obj = dict()
        #Fill the object
        article_obj.update({'title':article.title})
        article_obj.update({'body':article.text})
        article_obj.update({'author':article.authors})
        articles.append(article_obj)
    #Washington Street Journal
    for article in wsj.articles:
        article.parse()
        #Article object init
        article_obj = dict()
        #Fill the object
        article_obj.update({'title':article.title})
        article_obj.update({'body':article.text})
        article_obj.update({'author':article.authors})
        articles.append(article_obj)
        print(article.title)


def main():
    scrape()

if __name__ == "__main__":
    main()
