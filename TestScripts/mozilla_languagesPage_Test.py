from selenium import webdriver
from TestVariables.test_Variables import test_variables
from PageObjects.Pages.mozillaFirefoxLanguagesPage import mozilla_Firefox_Languages_Page

import unittest


class mozilla_langPage_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(test_variables.chromedriver_location)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_mozilla_mainPage(self):
        driver = self.driver
        driver.get(test_variables.mozilla_languages_page_link)
        mozilla_lang = mozilla_Firefox_Languages_Page(driver)
        lang_output = ''
        if mozilla_lang.get_mozilla_language_page_logo().is_displayed():
            lang_output = mozilla_lang.get_mozilla_language_list()
            print("List of Languages From The Mozilla Download Page")
            print("************************************************")
            for lang in lang_output:
                print(f'{lang}\n')

        if len(lang_output) > 0:
            print("List of Languages From The Mozilla Download Page Successfully Made Available")
        else:
            print("Unable to Retrieve List. Exiting Test")
            driver.quit()
            driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Ended")


if __name__ == '__main__':
    unittest.main()
