from selenium import webdriver
from PageObjects.Pages.googleSearchPage import googleSearchPage
from TestVariables.test_Variables import test_variables
import unittest


class test_Google_SearchPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(test_variables.chromedriver_location)
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_Google_SearchPage(self):
        driver = self.driver
        driver.get(test_variables.google_search_link)
        driver.set_page_load_timeout(30)
        search_page_expected_title = test_variables.google_search_page_title
        retrieve_result = ''
        search_page = googleSearchPage(driver)
        page_title = search_page.get_page_title()
        if page_title == search_page_expected_title:
            print("Google Page Successfully Opened")
            retrieve_result = search_page.google_search_results_access(test_variables.search_string_to_be_entered,
                                                                       test_variables.search_result_to_be_chosen)
        else:
            print("Google Page Not Loaded. Exiting the test")
            driver.quit()
            driver.close()

        if retrieve_result:
            print(f'Mozilla Firefox searched and results are displayed')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
