# # -*- coding: utf-8 -*-
# import scrapy

# class RechargeoffersSpider(scrapy.Spider):
    # name = 'rechargeOffers'
    # allowed_domains = ['paytm.com']
    # start_urls = ['http://paytm.com/']

    # def parse(self, response):
        # pass

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
class RechargeSpider(CrawlSpider):
    name = "rechargeOffers"
    allowed_domains = ["paytm.com"]
    start_urls = [
        'https://paytm.com/offer/recharge/'
    ]

    rules = (Rule(LinkExtractor(allow=(), restrict_css=('.ofr_txt',)), callback="parse_item", follow=True),)

    def parse_item(self, response):
		print('Entering parse_item')
		print('Processing URL..', response.url)
		print('type of response', type(response))
		print(response.css('.list > li::text').extract())