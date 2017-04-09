from scrapy.spiders import CrawlSpider, Rule
from scrapy.http.request import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy.selector import Selector
import urllib2
from bs4 import BeautifulSoup
import csv


class site_finder(CrawlSpider):
    name = 'sites'

    start_urls = ['http://www.kadaza.com/news']
    # Allow any url pattern
    # Deny social media sites from the crawl_for_site
    # Each website that is hit calls the parse_item method
    rules = (
        Rule(LinkExtractor(allow=('.*',), deny=('tumblr', 'twitter', 'youtube',
                                                'facebook', 'instagram',)), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        """Compiles a dictionary of news websites to be put in a csv"""
        current_site = response.url
        url = urllib2.urlopen(current_site).read()
        soup = BeautifulSoup(url, 'html.parser')
        desc = soup.findAll(attrs={"name": "description"})
        try:
            desc = desc[0]['content']
            if 'news' in desc.lower():
                print(response.url)
                yield{'List of Websites': response.url}
        except:
            pass


# Start urls dynamically identified globally
urls = []
with open('news_sites.csv') as csv:
    for row in csv:
        urls.append(row)
urls.pop(0)


class article_finder(CrawlSpider):
    name = 'articles'
    start_urls = urls
    # Alllow all domains
    # Deny social media
    # Calls parse_article for each URL
    rules = (
        Rule(LinkExtractor(allow=('.*',), deny=('tumblr', 'twitter', 'youtube',
                                                'facebook', 'instagram',)), callback='parse_article', follow=False),
    )

    def parse_article(self, response):
        """Identifies articles and calls helper method to scrape data"""
        # CSS selector grabs article titles
        for title in response.css('h3 a::attr(href)'):
            print(response.url)
            #print('calling function with ' + title.extract())
            self.scrape_article('' + title)

        # Some sites have h3 some have h1 some have neither
        for title in response.css('h1 a::attr(href)'):
            # urljoin puts together broken links
            try:
                self.scrape_article(response.urljoin(title.extract()))
            except:
                pass

    def scrape_article(url):
        """scrapes data and yields results to csv"""
        print("scraping")
        article_info = ['title', 'article_content']
        current_site = response.url
        url = urllib2.urlopen(current_site).read()
        # Make soup object
        soup = BeautifulSoup(url, 'html.parser')
        article_content = ""
        try:
            title = soup.find('h1', attrs={'itemprop': 'headline'}).getText()
        except:
            title = "N/A"
        for tag in soup.findAll('p'):
            article_content = article_content + "" + tag.getText().lower()
        article_info[0] = title
        article_info[1] = article_content
        # print(article_info[0])
        yield article_info
