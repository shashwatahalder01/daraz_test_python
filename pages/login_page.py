from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import *
from utils.users import user


class LoginPage(BasePage):
    
    def __init__(self, driver):
        self.locator = DLoginPageLocators
        super().__init__(driver)  


    def enter_username(self, email):
        self.find_element(*self.locator.USERNAME).send_keys(email)

    def enter_password(self, password):
        self.find_element(*self.locator.USERPASSWORD).send_keys(password)

    def click_login_button(self):
        self.find_element(*self.locator.LOGINBTN).click()

    def login(self):
        self.enter_username(user.get('email'))
        self.enter_password(user.get('password'))
        self.click_login_button()






    

