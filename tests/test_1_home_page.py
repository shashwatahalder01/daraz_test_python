import unittest
import time
from tests.base_test import BaseTest
from pages.home_page import *
from utils.test_cases import test_cases
from utils.searchitems import searchitems
from utils.writetxt import writetxt



class TestHomePage(BaseTest):
    

    def test_page_item(self):

        items = searchitems()

        page = HomePage(self.driver)
        
        print("\n" + str(test_cases(0)) + "\n")
        loginpage = page.click_login_link()
        
        print("\n" + str(test_cases(1)) + "\n")
        loginpage.login()

        print("\n" + str(test_cases(2)) + "\n")
        for item in items:
            time.sleep(5)
            page.search_item(item)
            # page.click_brandandservice()
            # time.sleep(5)
            productlist= page.get_productlist()
            filename = "D:\\TestAutomation\\daraz_test_python\\data\\Item_" + str(item)+".txt"
            writetxt(filename, productlist)
 
        # time.sleep(5)
        # page.search_item('keyboard')
        print("\n" + str(test_cases(3)) + "\n")
        print("\n" + str(test_cases(4)) + "\n")
        [pn,pb]= page.add_prduct_to_cart()
        print(pn,pb, sep='\n')
        
        print("\n" + str(test_cases(5)) + "\n")
        [cpn,cpb] = page.get_cart_product_detail()
        print(cpn,cpb, sep='\n')
        
        self.assertEqual(pn, cpn, "cart product dont match")







       
        
        
# python -m unittest tests.test_dhome_page.TestDHomePage