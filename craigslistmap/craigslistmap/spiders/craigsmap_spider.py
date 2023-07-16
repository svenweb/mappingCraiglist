import scrapy
from scrapy.crawler import CrawlerProcess

class CraigslistSpider(scrapy.Spider):
    name = "craigslist"
    start_urls = ['https://vancouver.craigslist.org/search/bia?search=1&gallery=0&query=']
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'bicycle_listings.csv'
    }

    def parse(self, response):
        links = response.css('a.cl-app-anchor.text-only.posting-title::attr(href)').getall()
        for href in links:
            if '/bik/' in href:
                yield response.follow(href, self.parse_bicycle)


    def parse_bicycle(self, response):
        map_div = response.css('div#map')
        latitude = map_div.attrib['data-latitude']
        longitude = map_div.attrib['data-longitude']
        yield {
            'href': response.url,
            'latitude': latitude,
            'longitude': longitude
        }