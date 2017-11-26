import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from selenium import webdriver

offer_url = [
    'https://paytm.com/dth-recharge',
    'https://paytm.com/recharge/'
]

print('offer URL', offer_url[1])

class RechargeSpider(CrawlSpider):
    name = "rechargeOffers"
    allowed_domains = ["paytm.com"]
    # start_urls is default scrapy variable 
    # It reads URL content and pass the content to parse function by default

    start_urls = [ offer_url[1] ]

    def __init__(self, *a, **kw):
        super(CrawlSpider, self).__init__(*a, **kw)
        self.driver = webdriver.Firefox()

	# rules = (Rule(LinkExtractor(allow=(), restrict_css=('.ofr_img',)), callback="parse_item", follow=True),)

    def parse(self, response):

        # Get the Web Page Content (URL)
        self.driver.get(offer_url[1])
		
        try:
            # _33La is a Class Name of the offer items 
            offersList = self.driver.find_elements_by_css_selector('._33La')
#            print('detail offer', offersList)

            for offerelement in offersList:
                # To fetch the offer title from 
                offerTitle = offerelement.get_attribute('innerText')
                print('Offer Title', offerTitle)
                offerelement.click()
                # _36_0 
                offerPromoCodeEle = self.driver.find_element_by_css_selector('._36_0 > input')
                offerPromoCode = offerPromoCodeEle.get_attribute('value')
                print('Offer Promocode', offerPromoCode)
                offerDescElement = self.driver.find_element_by_css_selector('.CLNZ > p')
                offerDescText = offerDescElement.get_attribute('innerHTML')
                print('Offer Description', offerDescText)
                print "\n"

                offerDescClose = self.driver.find_element_by_css_selector('.icon-delete')
                offerDescClose.click()

                # yield scrapy.Request('https://paytm.com/recharge/', callback=self.parse_item)
	except Exception as e:
            print('exception caught', e)

        self.driver.close()
		
    def parse_item(self, response):
        print('extracted T&C', response.css('.CLNZ > p::text').extract())

if __name__ == "__main__":
    RechargeSpider()
