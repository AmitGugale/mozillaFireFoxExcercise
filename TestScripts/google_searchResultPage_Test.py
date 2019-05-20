from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from PageObjects.Pages.googleSearchResultPage import googleSearchResultPage
from TestVariables.test_Variables import test_variables
from PageObjects.Locators import Locators

import unittest


class google_Search_Result_Page_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(test_variables.chromedriver_location)
        cls.driver.implicitly_wait(20)
        cls.driver.maximize_window()

    def test_google_search_page(self):
        driver = self.driver
        driver.get(test_variables.google_search_link)
        driver.set_page_load_timeout(30)
        driver.find_element_by_name(Locators.search_textbox).send_keys(test_variables.search_result_to_be_chosen)
        driver.find_element_by_name(Locators.search_textbox).send_keys((Keys.ENTER))
        search_result = googleSearchResultPage(driver)
        retrieve_link = ''
        search_result_expected_title = test_variables.search_result_to_be_chosen
        search_result_page_title = search_result.get_search_result_page_title()
        if search_result_expected_title in search_result_page_title:
            print("Results for mozilla firefox successfully displayed on the page")
            retrieve_link = search_result.google_select_desired_link(test_variables.google_search_results_link_text)
        else:
            print("Results for given text not retrieved on the page. Exiting the test")
            driver.quit()
            driver.close()
        if retrieve_link:
            print(f'The Required Link Has Been Clicked')
        else:
            print("Required Link Not Available to be Clicked. Exiting the test")
            driver.quit()
            driver.close()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()


