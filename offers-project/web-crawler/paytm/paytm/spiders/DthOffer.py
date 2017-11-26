import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver

class RechargeSpider(CrawlSpider):
    name = "dthOffers"
    allowed_domains = ["paytm.com"]
    start_urls = [
        'https://paytm.com/dth-recharge'
    ]

    def __init__(self, *a, **kw):
        super(CrawlSpider, self).__init__(*a, **kw)
        self.driver = webdriver.Firefox()

		# rules = (Rule(LinkExtractor(allow=(), restrict_css=('.ofr_img',)), callback="parse_item", follow=True),)

    def parse(self, response):
        self.driver.get('https://paytm.com/dth-recharge')
		
        try:
            detail_offer = self.driver.find_element_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "_33La", " " ))]')
            print('detail offer', detail_offer)
            detail_offer.click()
            offer = self.driver.find_element_by_css_selector('.CLNZ')
            print(offer.get_attribute('innerHTML'))
            #yield scrapy.Request('https://paytm.com/dth-recharge', callback=self.parse_item)
	except Exception as e:
            print('exception caught', e)

        self.driver.close()
		
    def parse_item(self, response):
        print('extracted T&C', response.css('.CLNZ > p::text').extract())

if __name__ == "__main__":
    RechargeSpider()
