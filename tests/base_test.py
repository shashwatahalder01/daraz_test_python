import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        options.add_argument('--no-sandbox')  # # Bypass OS security model
        # options.add_argument('disable-infobars')
        # options.add_argument("--disable-extensions")
        # options.add_argument("--start-fullscreen")
        # options.add_argument('--disable-gpu')
        chrome_path="D:\\TestAutomation\\test1\\driver\\chromedriver.exe"
        self.driver = webdriver.Chrome(chrome_path, options=options)
        self.driver.get("https://www.daraz.com.bd/")

    def tearDown(self):
        self.driver.close()
        # self.driver.quit()


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    # unittest.TextTestRunner(verbosity=1).run(suite)
    unittest.main()
