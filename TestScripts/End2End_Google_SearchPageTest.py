from selenium import webdriver
from PageObjects.Pages.googleSearchPage import googleSearchPage
from PageObjects.Pages.googleSearchResultPage import googleSearchResultPage
from PageObjects.Pages.mozillaFirefoxLanguagesPage import mozilla_Firefox_Languages_Page
from PageObjects.Pages.mozillaFirefoxMainPage import mozilla_Firefox_Main_Page
from TestVariables.test_Variables import test_variables
import unittest


class google_SearchPageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(test_variables.chromedriver_location)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_google_search_page(self):
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

        mozilla_main = mozilla_Firefox_Main_Page(driver)
        if mozilla_main.get_mozilla_main_page_logo().is_displayed():
            mozilla_main.access_mozilla_all_lang_link()
            print("Mozilla - Download in Other Languages Link is Clicked")
        else:
            print("Mozilla - Download in Other Languages Link Unavailable. Exiting the test")
            driver.quit()
            driver.close()

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
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()


