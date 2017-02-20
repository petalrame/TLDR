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
            #print(urls_to_visit[0])
            og_html = urllib.request.urlopen(urls_to_visit[0]).read()
        except:
            print("shit")
        current_site = urls_to_visit.pop(0)
        soup = BeautifulSoup(og_html,"html.parser")
        titles = soup.findAll('title')
        should_we_search = 0 #Added this in an attempt to decrease # of websites we crawl. Progress kinda stops when executing

        for title in titles:
            content = ("".join(title.contents)).lower()
            if "news" in content:
                print(content)
                news_sites.writerow(current_site)
                should_we_search = 1
        if should_we_search == 1:
            for tag in soup.findAll('a', href=True):
                found_url = tag['href']
                #print(found_url)
                if found_url not in visited:
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
    #crawl_articles()
    return

if __name__ == "__main__":
    main()
