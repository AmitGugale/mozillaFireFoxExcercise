from selenium import webdriver
from TestVariables.test_Variables import test_variables
from PageObjects.Pages.mozillaFirefoxMainPage import mozilla_Firefox_Main_Page

import unittest


class mozilla_mainPage_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(test_variables.chromedriver_location)
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_mozilla_mainPage(self):
        driver = self.driver
        driver.get(test_variables.mozilla_main_page_link)
        mozilla_main = mozilla_Firefox_Main_Page(driver)
        if mozilla_main.get_mozilla_main_page_logo().is_displayed():
            mozilla_main.access_mozilla_all_lang_link()
            print("Mozilla - Download in Other Languages Link is Clicked")
        else:
            print("Mozilla - Download in Other Languages Link Unavailable. Exiting the test")
            driver.quit()
            driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
