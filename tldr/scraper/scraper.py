import urllib.request
from bs4 import BeautifulSoup
import csv
def crawlForSites():
    newsSites = csv.writer(open('newsSites.csv', 'w', newline=''))
    url = "https://en.wikipedia.org/wiki/Wikipedia:News_sources/Americas"
    urlsToVisit = [url] #Stack of urls to that may contain
    visited = [url] #list of sites already visited
    while (urlsToVisit):
        try:
            ogHtml = urllib.request.urlopen(url).read()
        except:
            print("shit")
        soup = BeautifulSoup(ogHtml)
        urlsToVisit.pop(0)

        for tag in soup.findAll('a', href = True):
            foundUrl = tag['href']
            #print(foundUrl)
            newsSites.writerow( foundUrl)
            if url in foundUrl and foundUrl not in visited:
                urls.append(foundUrl) #Adding new site to queue
                visited.append(foundUrl) #Adding new site to visited

def crawlArticles():
    with open('newsSites.csv') as csvfile:
        reader = csv.reader(csvfile)
        website = ''
        for row in reader:
            for x in row:
                website = website + x
            print(website+"\n")
            website = ''
            #Scrape some shiz



def main():
        crawlForSites();
        crawlArticles();
        return

if __name__ == "__main__":
        main()
