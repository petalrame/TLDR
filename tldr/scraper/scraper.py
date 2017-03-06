"""This module data mines articles daily"""
import urllib.request
import csv
from bs4 import BeautifulSoup
import urllib.parse
# Package that "Extracts the top level domain (TLD) from the URL given"
from tld import get_tld
from tld.utils import update_tld_names


def crawl_for_sites():
    update_tld_names()
    """Crawl the internet for websites"""
    news_sites = csv.writer(open('newsSites.csv', 'w', newline=''))
    # Stack of urls to that may contain
    urls_to_visit = ['https://www.yahoo.com/news/','https://news.google.com/','http://www.foxnews.com/','https://www.washingtonpost.com/',
                    'www.bbc.co.uk/news','https://www.nytimes.com/']
    while urls_to_visit:
        try:
            # print(urls_to_visit[0])
            og_html = urllib.request.urlopen(urls_to_visit[0]).read()
        except:
            print("URL can not be opened")

        current_site = urls_to_visit.pop(0)
        # Make BeautifulSoup Object from webpage
        soup = BeautifulSoup(og_html, "html.parser")

        # We want only sites with news in the title
        titles = soup.findAll('title')
        for title in titles:
            content = ("".join(title.contents)).lower()
            if "news" in content:
                news_sites.writerow(current_site)
                # Add new sites found on page to urls_to_visit
        for tag in soup.findAll('a', href=True):
            found_url = tag['href']
            try:
                domain = get_tld(found_url)
                # Variable to count occurances of current website in
                count = 0
                for website in urls_to_visit:
                    if domain in website:
                        # Stop repeating domains
                        count = count + 1

                if count == 0:
                    urls_to_visit.append(domain)

            except:
                print("")


def crawl_articles():
    """Crawls through different articles in a domain"""
    with open('newsSites.csv') as csvfile:
        reader = csv.reader(csvfile)
        website = ''
        for row in reader:
            for i in row:
                website = website + i
            print(website + "\n")
            website = ''
            # Scrape some shiz


def main():
    """Call the other methods"""
    crawl_for_sites()
    crawl_articles()
    return


if __name__ == "__main__":
    main()
