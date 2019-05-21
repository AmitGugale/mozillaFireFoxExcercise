from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from PageObjects.Locators import Locators
from selenium.common.exceptions import StaleElementReferenceException

# Google Search Page Object


class googleSearchPage():
    # Initialises Google Search Page and identifies required elements
    def __init__(self, driver):
        self.driver = driver

        self.search_textbox = Locators.search_textbox

    # Method to retrieve title of page the driver has opened
    def get_page_title(self):
        return self.driver.title

    # Method which enters a text on the search input, selects a desired text
    # from the auto-populated suggestions and clicks it

    def google_search_results_access(self, search_input_text, search_select_text):
        result_found = False
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.NAME, Locators.search_textbox))
            )
        except TimeoutException:
            print("Google Search Box Failed to load.")
        try:
            self.driver.find_element_by_name(self.search_textbox).clear()
            self.driver.find_element_by_name(self.search_textbox).send_keys(search_input_text)
        except StaleElementReferenceException as se:
            print('StaleElementReferenceException encountered while entering search string. Trying functionality again')
            self.driver.find_element_by_name(self.search_textbox).clear()
            self.driver.find_element_by_name(self.search_textbox).send_keys(search_input_text)
        except TimeoutException as te:
            print('TimeoutException encountered while entering search string. Trying functionality again')
            self.driver.find_element_by_name(self.search_textbox).clear()
            self.driver.find_element_by_name(self.search_textbox).send_keys(search_input_text)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, Locators.search_result_set))
            )
        except TimeoutException:
            print("Search Result Set Failed to Load")
        try:
            auto_options = self.driver.find_elements_by_xpath(Locators.search_result_set)
        except StaleElementReferenceException as StaleException:
            print('StaleElementReferenceException encountered while retrieving auto results. Trying functionality again')
            auto_options = self.driver.find_elements_by_xpath(Locators.search_result_set)
        except TimeoutException as TOException:
            print('TimeoutException encountered while retrieving auto results. Trying functionality again')
            auto_options = self.driver.find_elements_by_xpath(Locators.search_result_set)
        for link in auto_options:
            try:
                text = link.text
            except StaleElementReferenceException as StaleException:
                print('StaleElementReferenceException  while retrieving text. Trying functionality again')
                text = link.text
            except TimeoutException as TOException:
                print('TimeoutException  while retrieving text. Trying functionality again')
                text = link.text
            if text == search_select_text:
                time.sleep(2)
                try:
                    link.click()
                except StaleElementReferenceException as StaleException:
                    print('StaleElementReferenceException encountered while clicking link. Trying functionality again')
                    link.click()
                except TimeoutException as TOExceptionException:
                    print('TimeoutException encountered while clicking link. Trying functionality again')
                    link.click()
                print(f'{text} result is clicked')
                result_found = True
                break

        return result_found
