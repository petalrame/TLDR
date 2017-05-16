import newspaper

def scrape():
    """Uses the Newspaper library to parse news websites for content"""
    #Master list
    articles = []
    #USA Today
    usa = newspaper.build('https://www.usatoday.com/',memoize_articles=False)
    for article in usa.articles:
        article.download()
        article.parse()
        #Article object init
        article_obj = dict()
        #Fill the object
        article_obj.update({'title':article.title})
        article_obj.update({'body':article.text})
        article_obj.update({'author':article.authors})
        articles.append(article_obj)
    #NY Times
    nytimes = newspaper.build('http://nytimes.com',memoize_articles=False)
    for article in nytimes.articles:
        article.download()
        article.parse()
        #Article object init
        article_obj = dict()
        #Fill the object
        article_obj.update({'title':article.title})
        article_obj.update({'body':article.text})
        article_obj.update({'author':article.authors})
        articles.append(article_obj)
    #Washington Street Journal
    wsj = newspaper.build('http://wsj.com',memoize_articles=False)
    for article in wsj.articles:
        article.download()
        article.parse()
        #Article object init
        article_obj = dict()
        #Fill the object
        article_obj.update({'title':article.title})
        article_obj.update({'body':article.text})
        article_obj.update({'author':article.authors})
        articles.append(article_obj)


def main():
    scrape()

if __name__ == "__main__":
    main()
