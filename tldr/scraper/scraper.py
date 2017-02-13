from bs4 import BeautifulSoup
import urllib2
import scrapy

class NewsSpider(scrapy.Spider):
    name = 'newsspider'
    start_urls = ['https://www.nytimes.com']

    def parse(self, response):
        for title in response.css('h2 a'):
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('h2 a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
