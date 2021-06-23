from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import *


class AffiliatePage(BasePage):
    
    def __init__(self, driver):
        self.locator = AffilitePageLocators
        super().__init__(driver)  

    def search_item(self):
        self.wait_element(*self.locator.AFFILIATEURL)
        return self.find_element(*self.locator.AFFILIATEURL).text
    
    def go_back(self):
        return self.driver.back()

    def click_affiliate_link(self):
        self.wait_element(*self.locator.AFFILIATELINK)
        self.find_element(*self.locator.AFFILIATELINK).click()

    def click_helpcenter_link(self):
        self.wait_element(*self.locator.HELPCENTERLINK)
        self.find_element(*self.locator.HELPCENTERLINK).click()

    def click_howtobuy_link(self):
        self.wait_element(*self.locator.HOWTOBUYLINK)
        self.find_element(*self.locator.HOWTOBUYLINK).click()

    def click_returnrefund_link(self):
        self.wait_element(*self.locator.RETURNREFUNDLINK)
        self.find_element(*self.locator.RETURNREFUNDLINK).click()

    def click_contactus_link(self):
        self.wait_element(*self.locator.CONTACTUSLINK)
        self.find_element(*self.locator.CONTACTUSLINK).click()

    

