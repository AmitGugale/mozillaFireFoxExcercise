from PageObjects.Locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

# Mozilla Firefox Main Page Object


class mozilla_Firefox_Main_Page():

    # Initialises Mozilla main Page and identifies required elements
    def __init__(self, driver):
        self.driver = driver
        self.main_page_mozilla_logo = Locators.mozilla_main_logo
        self.main_page_mozilla_language_link = Locators.all_languages_link

    # Method which returns the logo element of Mozilla main page.

    def get_mozilla_main_page_logo(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, Locators.mozilla_main_logo))
            )
        except TimeoutException:
            print("Mozilla Main Page Logo Has Not Loaded")
        return self.driver.find_element_by_xpath(Locators.mozilla_main_logo)

    # Method to access and click the "Download in other languages" link.

    def access_mozilla_all_lang_link(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH, Locators.all_languages_link))
            )
        except TimeoutException:
            print("Mozilla Main Page Languages Link Has Not Loaded")
        try:
            self.driver.find_element_by_xpath(Locators.all_languages_link).click()
        except StaleElementReferenceException as STException:
            print('StaleElementReferenceException while clicking language link. Trying functionality again')
            self.driver.find_element_by_xpath(Locators.all_languages_link).click()
        except TimeoutException as TOException:
            print('TimeoutException while clicking language link. Trying functionality again')
            self.driver.find_element_by_xpath(Locators.all_languages_link).click()

