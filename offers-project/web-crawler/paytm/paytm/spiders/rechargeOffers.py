from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

offer_url = [
    'https://paytm.com/dth-recharge/',
    'https://paytm.com/recharge/'
]

print('offer URL', offer_url[0])

class RechargeSpider():
    name = "rechargeOffers"
    # allowed_domains = ["paytm.com"]
    # start_urls is default scrapy variable 
    # It reads URL content and pass the content to parse function by default

    # start_urls = [ offer_url[0] ]

    def __init__(self):
        self.driver = webdriver.Firefox()

	# rules = (Rule(LinkExtractor(allow=(), restrict_css=('.ofr_img',)), callback="parse_item", follow=True),)

    def parse(self):

        # Get the Web Page Content (URL)
        self.driver.get(offer_url[0])
        #self.driver.maximize_window()
        actions = ActionChains(self.driver)
		
        try:
            # _33La is a Class Name of the offer items 
            offersList = self.driver.find_elements_by_css_selector('.YGVM')
            print('detail offer', offersList)

            for offerelement in offersList:
                # To fetch the offer title from 
                # actions.move_to_element(offerelement).perform()
                # self.driver.execute_script("arguments[0].scrollIntoView();", offerelement)
                #offerelement.location_once_scrolled_into_view.click()
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                offerelement.click()
                print("element Clicked")
                print ("self driver", self.driver)
                offerTitleEle = self.driver.find_element_by_css_selector('._36No > h1')
                offerTitle = offerTitleEle.get_attribute('innerText')
                print('Offer Title', offerTitle)
                # _36_0 
                offerPromoCodeEle = self.driver.find_element_by_css_selector('._36_0 > input')
                print "offerPromocode", offerPromoCodeEle
                offerPromoCode = offerPromoCodeEle.get_attribute('value')
                print('Offer Promocode', offerPromoCode)
                offerDescElement = self.driver.find_element_by_css_selector('.CLNZ > p')
                offerDescText = offerDescElement.get_attribute('innerHTML')
                print('Offer Description', offerDescText)
                print "\n"

                offerDescClose = self.driver.find_element_by_css_selector('.icon-delete')
                offerDescClose.click()

                # yield scrapy.Request('https://paytm.com/recharge/', callback=self.parse_item)
	except:
            # print('exception caught', e)
            pass

        self.driver.close()
		
if __name__ == "__main__":
    RS = RechargeSpider()
    RS.parse()

