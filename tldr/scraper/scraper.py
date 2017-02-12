from bs4 import BeautifulSoup
import urllib2

def scrapeNYtimes:
    url = "https://www.nytimes.com/"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content)
    
