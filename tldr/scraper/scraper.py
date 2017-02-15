import urllib.request
from bs4 import BeautifulSoup

def crawlForSites():
    url = "https://en.wikipedia.org/wiki/Wikipedia:News_sources/Americas"
    urlsToVisit = [url] #Stack of urls to that may contain
    visited = [url] #list of sites already visited
    print ("hello")
    while (urlsToVisit):
        try:
            ogHtml = urllib.request.urlopen(url).read()
        except:
            print("shit")
        soup = BeautifulSoup(ogHtml)
        urls.pop(0)

        for tag in soup.findAll('a', href = True):
            foundUrl = tag['href']
            foundUrl = urlparse.urljoin(url , foundUrl) #If it finds an href with a link that will give problems, this makes it a working link
            print(foundUrl)
            if url in foundUrl and foundUrl not in visited:
                urls.append(foundUrl) #Adding new site to queue
                visited.append(foundUrl) #Adding new site to visited

    def main():
        print("hello")
        crawlForSites();
        return

    if __name__ == "__main__":
        main()
