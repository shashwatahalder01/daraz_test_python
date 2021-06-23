from selenium.webdriver.common.by import By



class DLoginPageLocators(object):
    
    USERNAME =  (By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div[1]/div[1]/input')
    USERPASSWORD =  (By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div[1]/div[2]/input')
    LOGINBTN =  (By.XPATH, '//*[@id="container"]/div/div[2]/form/div/div[2]/div[1]/button')

    
class DHomePageLocators(object):
    
    LOGINLINK =  (By.XPATH, '//*[@id="anonLogin"]/a')

    SEARCH =  (By.NAME, 'q')

    BRANDCHECKBOX =  (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[1]/label[4]/span[1]/input')
    SERVICECHECKBOX =  (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div/div[3]/div[2]/div/div/label[2]/span[1]/input')
    
    PRODUCTLIST =  (By.CLASS_NAME, 'c16H9d')
    
    PRODUCTLINK =  (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div/div[1]/div/a')
    
    PRODUCTNAME =  (By.XPATH, '//*[@id="module_product_title_1"]/div/div/span')
    PRODUCTBRAND =  (By.XPATH, '//*[@id="module_product_brand_1"]/div/a[1]')
    
    ADDTOCARTBTN=  (By.XPATH, '//*[@id="module_add_to_cart"]/div/button[2]')
    GOTOCARTBTN =  (By.XPATH, '//*[@id="dialog-body-1"]/div/div[1]/div/div[2]/div/div[2]/div/div[2]/button[2]')
    
    CARTPRODUCTNAME=  (By.XPATH, '//div//div//div//div//div//div//div//div//div//div//div[2]//a[1]')
    CARTPRODUCTBRAND =  (By.XPATH, '//body/div/div/div/div/div/div/div/div/div/div/div/div/div/a[2]')


class AffilitePageLocators(object):

    AFFILIATELINK =  (By.XPATH, '//*[@id="anonSignup"]/a')
    AFFILIATEURL =  (By.XPATH, '//*[@id="J_6558113530"]/div/div/p[5]/a[1]')
    HELPCENTERLINK =  (By.XPATH, '//*[@id="J_1362278930"]/section/div[1]/div/div[1]/ul[1]/li[1]/a')
    HOWTOBUYLINK =  (By.XPATH, '//*[@id="J_1362278930"]/section/div[1]/div/div[1]/ul[1]/li[2]/a')
    RETURNREFUNDLINK =  (By.XPATH, '//*[@id="J_1362278930"]/section/div[1]/div/div[1]/ul[1]/li[4]/a')
    CONTACTUSLINK =  (By.XPATH, '//*[@id="J_1362278930"]/section/div[1]/div/div[1]/ul[1]/li[5]/a')

