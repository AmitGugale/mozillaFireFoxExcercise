from PageObjects.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class mozilla_Firefox_Languages_Page():
    def __init__(self, driver):
        self.driver = driver
        self.mozilla_languages_logo = Locators.all_languages_logo
        self.mozilla_language_table = Locators.language_table

    def get_mozilla_language_page_logo(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Locators.all_languages_logo))
            )
        except TimeoutException:
            print("Mozilla Languages Page Logo Has Not Loaded")
        return self.driver.find_element_by_xpath(Locators.all_languages_logo)

    def get_mozilla_language_list(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Locators.language_table))
            )
        except TimeoutException:
            print("Mozilla Language Table Has Not Loaded")
        try:
            rows = self.driver.find_elements_by_xpath(Locators.language_table)
        except StaleElementReferenceException as StaleException:
            print('StaleElementReferenceException while retrieving Mozilla Language Table. Trying functionality again')
            rows = self.driver.find_elements_by_xpath(Locators.language_table)
        except TimeoutException as TOException:
            print('TimeoutException while retrieving Mozilla Language Table. Trying functionality again')
            rows = self.driver.find_elements_by_xpath(Locators.language_table)
        results = []
        for row in rows:
            try:
                col_text = row.text
            except StaleElementReferenceException as StaleException:
                print('StaleElementReferenceException  while processing result. Trying functionality again')
                col_text = row.text
            except TimeoutException as TOException:
                print('TimeoutException  while processing result. Trying functionality again')
                col_text = row.text
            results.append(col_text)
        return results

