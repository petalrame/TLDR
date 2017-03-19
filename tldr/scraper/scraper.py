"""This module data mines articles daily"""
import urllib.request
import csv
from bs4 import BeautifulSoup
import urllib.parse
# Package that "Extracts the top level domain (TLD) from the URL given"
from tld import get_tld
from tld.utils import update_tld_names


def crawl_for_sites():
    """Crawl the internet for websites"""
    update_tld_names()
    news_sites = csv.writer(open('newsSites.csv', 'w', newline=''))
    # Stack of urls to that may contain
    urls_to_visit = ['https://www.yahoo.com/news/', 'https://news.google.com/', 'http://www.foxnews.com/', 'https://www.washingtonpost.com/',
                     'www.bbc.co.uk/news', 'https://www.nytimes.com/']
    # TODO
    # Still getting some duplicates
    # BBC tld raises an exception
    while(urls_to_visit):
        try:
            og_html = urllib.request.urlopen(urls_to_visit[0]).read()
        except:
            print("URL can not be opened")

        current_site = urls_to_visit.pop(0)
        # Make BeautifulSoup Object from webpage
        soup = BeautifulSoup(og_html, "html.parser")

        # Checks for news in meta description tags and will not fall for social
        # media
        desc = soup.findAll(attrs={"name": "description"})
        try:
            desc = desc[0]['content']
            if 'news' in desc.lower() and 'twitter' not in desc.lower() and 'facebook' not in desc.lower() and 'instagram' not in desc.lower():
                try:
                    domain = get_tld(current_site)
                    news_sites.writerow(domain)
                    print(domain)
                except:
                    print("Exception at: " + current_site)
        except:
            pass

        for tag in soup.findAll('a', href=True):
            found_url = tag['href']
            try:
                domain = get_tld(found_url)
                # Variable to count occurances of current website in
                count = 0
                for website in urls_to_visit:
                    if domain in website:
                        count = count + 1
                        break
                if count == 0:
                    urls_to_visit.append(found_url)

            except:
                pass


def crawl_for_articles():
    """Crawls through different articles in a domain"""
    urls_to_visit = []
    update_tld_names()
    articles = csv.writer(open('articles.csv', 'w', newline=''))

    with open('newsSites.csv') as csvfile:
        reader = csv.reader(csvfile)
        website = ''
        for row in reader:
            for i in row:
                website = website + i
            # Add website to queue
            urls_to_visit.append("https://" + website.lower())
            # Reset website
            website = ''

    while(urls_to_visit):
        current_site = urls_to_visit.pop(0)
        # Make a soup of the website domain
        try:
            og_html = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor).open(current_site)
        except:
            continue
        # Make BeautifulSoup Object from webpage
        try:
            soup = BeautifulSoup(og_html, "html.parser")
        except:
            continue
        # Looking for article in application name
        try:
            for name in soup.findAll(attrs={"name": "aplicationName"}):
                if 'article' in name['content'].lower():
                    articles.writerow(current_site)
                    continue
        except:
            pass
        # Looking for article in og:type meta tag
        try:
            for name in soup.findAll(attrs={"property": "og:type"}):
                if 'article' in name['content'].lower():
                    articles.writerow(current_site)
                    continue
        except:
            pass

        # Put all hrefs in urls_to_visit
        for tag in soup.findAll('a', href=True):
            found_url = tag['href']
            if found_url.lower() not in urls_to_visit:
                urls_to_visit.append(found_url.lower())


def scrape_articles():
    """Scrapes individual articles for information"""
    urls_to_visit = []
    article_stats = csv.writer(open('articleInfo.csv', 'w', newline=''))

    with open('articles.csv') as csvfile:
        reader = csv.reader(csvfile)
        website = ''
        for row in reader:
            for i in row:
                website = website + i
            # Add website to queue
            if website not in urls_to_visit:
                urls_to_visit.append(website)
            # Reset website
            website = ''

    while(urls_to_visit):
        article_info = ['article', 'title']
        # Scraping set up
        current_site = urls_to_visit.pop(0).lower()
        try:
            og_html = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor).open(current_site)
        except:
            continue
        # Make BeautifulSoup Object from webpage
        try:
            soup = BeautifulSoup(og_html, "html.parser")
        except:
            continue
        # End of setting up
        article_content = ""
        for tag in soup.findAll('p'):
            article_content = article_content + "" + tag.getText().lower()
        article_info[0] = article_content
        try:
            title = soup.find('h1', attrs={'itemprop': 'headline'}).getText()
        except:
            pass
        article_info[1] = title
        print(article_info[1])
        for stat in article_info:
            article_stats.writerow(stat)


def main():
    """Call the other methods"""
    crawl_for_sites()
    crawl_for_articles()
    scrape_articles()
    return


if __name__ == "__main__":
    main()
