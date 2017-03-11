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
    while len(urls_to_visit) < 500:
        try:
            # print(urls_to_visit[0])
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


def crawl_articles():
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
            urls_to_visit.append(website)
            # Reset website
            website = ''
    while(urls_to_visit):
        # Make a soup of the website domain
        try:
            print(urls_to_visit[0])
            og_html = urllib.request.urlopen('https://' + urls_to_visit[0]).read()
        except:
            print("URL can not be opened")
        current_site = urls_to_visit.pop(0)
        # Make BeautifulSoup Object from webpage
        try:
            soup = BeautifulSoup(og_html, "html.parser")
        except:
            continue
        desc = soup.findAll(attrs={"name": "aplicationName"})
        try:
            desc = desc[0]['content'].lower()
            if 'article' in desc:
                print(desc)
                articles.writerow(current_site)
        except:
            pass
        # Put all hrefs in urls_to_visit
        for tag in soup.findAll('a', href=True):
            found_url = tag['href']
            urls_to_visit.append(found_url)


def main():
    """Call the other methods"""
    # crawl_for_sites()
    crawl_articles()
    return


if __name__ == "__main__":
    main()
