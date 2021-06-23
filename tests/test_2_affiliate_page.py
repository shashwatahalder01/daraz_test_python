import unittest
from tests.base_test import BaseTest
from pages.affiliate_page import *
from utils.test_cases import test_cases



class TestAffiliatePage(BaseTest):
    

    def test_link_item(self):
        
        print("\n" + str(test_cases(6)) + "\n")
        print("\n" + str(test_cases(7)) + "\n")
        page = AffiliatePage(self.driver)
        page.click_affiliate_link()
        search_result = page.search_item()
        print("\n ["+ search_result+"]")
        self.assertEqual('www.daraz.com.bd', search_result, "url is not matching")

        print("\n" + str(test_cases(8)) + "\n")
        page.click_helpcenter_link()
        search_result = page.get_title()
        print("\n ["+ search_result+"]")
        self.assertIn("Help Center",search_result, "link is not valid")

        print("\n" + str(test_cases(9)) + "\n")
        page.go_back()
        page.click_howtobuy_link()
        search_result = page.get_title()
        print("\n ["+ search_result+"]")
        self.assertIn("Help Center",search_result, "link is not valid")

        print("\n" + str(test_cases(10)) + "\n")
        page.go_back()
        page.click_returnrefund_link()
        search_result = page.get_title()
        print("\n ["+ search_result+"]")
        self.assertIn("Return Goods",search_result, "link is not valid")

        print("\n" + str(test_cases(11)) + "\n")
        page.go_back()
        page.click_contactus_link()
        search_result = page.get_title()
        print("\n ["+ search_result+"]")
        self.assertIn("Contact Us",search_result, "link is not valid")
        

# python -m unittest tests.test_affiliate_page.TestAffiliatePage