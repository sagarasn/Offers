from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd

offer_url = [
    'https://www.freecharge.in/offers'
]

print('offer URL', offer_url[0])

dropdownOptions = {
    'Recharges': 1,
    'DTH/Bills': 4,
    'Postpaid': 10
}


class RechargeSpider():

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)

    def parse(self):

        # Get the Web Page Content (URL)
        self.driver.get(offer_url[0])
                		
        try:
            select_dropdown = Select(self.driver.find_element_by_css_selector('._2bzfR > select'))
            select_dropdown.select_by_index(dropdownOptions['Recharges'])
            offersList = self.driver.find_elements_by_css_selector('._37F1f')
            parentTab = self.driver.current_window_handle
            offerPromoCodeList = []
            offerTitleList = []

            for offerelement in offersList:
                # To fetch the offer title from 
                offerPromocode = offerelement.find_element_by_css_selector('._2fwR5 > h3').text
                print 'Offer Promo Code,', offerPromocode
                offerPromoCodeList.append(offerPromocode)

                offerTitle = offerelement.find_element_by_css_selector('._3UnxB').text
                print "Offer Title,", offerTitle
                offerTitleList.append(offerTitle)

                offerLink = offerelement.find_element_by_css_selector('a').get_attribute('href')
                openLink = "window.open('{0}', 'offerDetailPage');".format(offerLink)
                self.driver.execute_script(openLink)
                newTab = self.driver.window_handles[1]
                self.driver.switch_to_window(newTab)
                iterateElement = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.terms-list')))
                for descEle in self.driver.find_elements_by_css_selector('.terms-list'):
                    desc = descEle.get_attribute('innerText')
                    print 'Desc,', desc

                self.driver.close()
                self.driver.switch_to_window(parentTab)

	except Exception as e:
            print('exception caught', e)
            pass

        self.driver.close()
        data = {'PROMOCODE': offerPromoCodeList, 'TITLE': offerTitleList}
        df = pd.DataFrame(data)
        print df
        df.to_csv('FreeChargeOffers.csv')
        
		
if __name__ == "__main__":
    RS = RechargeSpider()
    RS.parse()
