from PageObjects.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

# Google Search Result Page Object

class googleSearchResultPage():

    # Initialises Google Search Results Page and identifies required elements
    def __init__(self, driver):
        self.driver = driver
        self.search_results_link_set = Locators.search_result_result_links

    # Method to retrieve title of page the driver has opened
    def get_search_result_page_title(self):
        return self.driver.title

    # Method to click the desired link among the various links returned in the result.
    # The criteria for selecting link is the text displayed

    def google_select_desired_link(self, link_search_text):
        link_result_found = True
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Locators.search_result_result_links))
            )
        except TimeoutException:
            print("Search Result Links Failed to Load")
        try:
            search_results = self.driver.find_elements_by_xpath(Locators.search_result_result_links)
        except StaleElementReferenceException as StaleException:
            print('StaleElementReferenceException while retrieving result of search string. Trying functionality again')
            search_results = self.driver.find_elements_by_xpath(Locators.search_result_result_links)
        except TimeoutException as TOException:
            print('TimeoutException while retrieving result of search string. Trying functionality again')
            search_results = self.driver.find_elements_by_xpath(Locators.search_result_result_links)

        for result in search_results:
            try:
                result_link = result.text
            except StaleElementReferenceException as StaleException:
                print('StaleElementReferenceException  while processing result. Trying functionality again')
                result_link = result.text
            except TimeoutException as TOException:
                print('TimeoutException while processing result. Trying functionality again')
                result_link = result.text
            if link_search_text in result_link:
                try:
                    result.click()
                except StaleElementReferenceException as StaleException:
                    print('StaleElementReferenceException while clicking result link. Trying functionality again')
                    result.click()
                except TimeoutException as TOException:
                    print('TimeoutException encountered while clicking result link. Trying functionality again')
                    result.click()
                break
        return link_result_found
