from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.locators import *
import time


class HomePage(BasePage):

    def __init__(self, driver):
        self.locator = DHomePageLocators
        super().__init__(driver)  # Python3 version

    def search_item(self, item):
        self.clear_search()
        self.find_element(*self.locator.SEARCH).send_keys(item)
        self.find_element(*self.locator.SEARCH).send_keys(Keys.ENTER)

    def clear_search(self):
        # self.find_element(*self.locator.SEARCH).clear()
        self.find_element(*self.locator.SEARCH).send_keys(Keys.CONTROL + "a")
        self.find_element(*self.locator.SEARCH).send_keys(Keys.DELETE)

    def click_login_link(self):
        self.wait_element(*self.locator.LOGINLINK)
        self.find_element(*self.locator.LOGINLINK).click()
        return LoginPage(self.driver)


    def click_brand_checkbox(self):
        self.wait_element(*self.locator.BRANDCHECKBOX)
        self.find_element(*self.locator.BRANDCHECKBOX).click()


    def click_service_checkbox(self):
        self.wait_element(*self.locator.SERVICECHECKBOX)
        self.find_element(*self.locator.SERVICECHECKBOX).click()

    def click_brandandservice(self):
        self.click_brand_checkbox()
        self.click_service_checkbox()
        

    def click_product(self):
        self.wait_element(*self.locator.PRODUCTLINK)
        self.find_element(*self.locator.PRODUCTLINK).click()

    def click_addtocart(self):
        self.wait_element(*self.locator.ADDTOCARTBTN)
        self.find_element(*self.locator.ADDTOCARTBTN).click()

    def click_gotocart(self):
        self.wait_element(*self.locator.GOTOCARTBTN)
        self.find_element(*self.locator.GOTOCARTBTN).click()

    def get_product_name(self):
        self.wait_element(*self.locator.PRODUCTNAME)
        return self.find_element(*self.locator.PRODUCTNAME).text

    def get_product_brand(self):
        self.wait_element(*self.locator.PRODUCTBRAND)
        return self.find_element(*self.locator.PRODUCTBRAND).text

    def get_cartproduct_name(self):
        self.wait_element(*self.locator.CARTPRODUCTNAME)
        return self.find_element(*self.locator.CARTPRODUCTNAME).text

    def get_cartproduct_brand(self):
        self.wait_element(*self.locator.CARTPRODUCTBRAND)
        return self.find_element(*self.locator.CARTPRODUCTBRAND).text

    def add_prduct_to_cart(self):
        self.click_product()
        pn = self.get_product_name()
        pb = self.get_product_brand()
        self.click_addtocart()
        return pn, pb

    def get_cart_product_detail(self):
        self.click_gotocart()
        cpn = self.get_cartproduct_name()
        cpb = self.get_product_brand
        return cpn, cpb


    def get_productlist(self):
        self.wait_element(*self.locator.PRODUCTLIST)
        products = self.find_elements(*self.locator.PRODUCTLIST)
        productlist = []
        for product in products:
            productlist.append(product.text)
        productlist.append("Number of products: "+ str(len(productlist)))
        return productlist