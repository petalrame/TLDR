"""This module data mines articles daily"""
import urllib.request
import csv
from bs4 import BeautifulSoup


def crawl_for_sites():
    """Crawl the internet for websites"""
    news_sites = csv.writer(open('newsSites.csv', 'w', newline=''))
    url = "https://en.wikipedia.org/wiki/Wikipedia:News_sources/Americas"
    urls_to_visit = [url] #Stack of urls to that may contain
    visited = [url] #list of sites already visited
    while urls_to_visit:
        try:
            og_html = urllib.request.urlopen(url).read()
        except:
            print("shit")
        soup = BeautifulSoup(og_html)
        urls_to_visit.pop(0)

        for tag in soup.findAll('a', href=True):
            found_url = tag['href']
            #print(foundUrl)
            news_sites.writerow(found_url)
            if url in found_url and found_url not in visited:
                urls_to_visit.append(found_url) #Adding new site to queue
                visited.append(found_url) #Adding new site to visited


def crawl_articles():
    """Crawls through different articles in a domain"""
    with open('newsSites.csv') as csvfile:
        reader = csv.reader(csvfile)
        website = ''
        for row in reader:
            for i in row:
                website = website + i
            print(website+"\n")
            website = ''
            #Scrape some shiz



def main():
    """Call the other methods"""
    crawl_for_sites()
    crawl_articles()
    return

if __name__ == "__main__":
    main()
