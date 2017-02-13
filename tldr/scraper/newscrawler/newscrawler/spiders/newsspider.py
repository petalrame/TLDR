from scrapy.selector import Selector
from scrapy.spiders import BaseSpider
from newscrawler.items import NewscrawlerItem
data = {"Title":"", "Content":""}
#Base spider crawls over a single page and not the subsequent links present on the first page
class NewsSpider (BaseSpider) :
  name = "newsspider"
  allowed_domains = ["nytimes.com"]
  start_urls = ['http://nytimes.com/']

  #This will be called automatically
  def parse(self, response):
        for title in response.css('h2 a'):
            data["Title"] = {'title': title.css('a ::text').extract_first()}
            print(data["Title"])
            yield {'title': title.css('a ::text').extract_first()}

        next_page = response.css('h2 a ::attr(href)').extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
