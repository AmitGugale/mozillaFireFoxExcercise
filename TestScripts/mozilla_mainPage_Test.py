from TestVariables.test_Variables import test_variables
from PageObjects.Pages.mozillaFirefoxMainPage import mozilla_Firefox_Main_Page
from TestBase.testBase import testBase
import unittest
# This Test Accesses the Mozilla Firefox Link, confirms the presence of the mozilla logo
# and clicks the Download in Other Languages button


class mozilla_mainPage_Test(testBase):

    def test_mozilla_mainPage(self):
        driver = self.driver
        driver.get(test_variables.mozilla_main_page_link)
        mozilla_main = mozilla_Firefox_Main_Page(driver)

        # Functionality is performed only if the logo is confirmed to be displayed

        if mozilla_main.get_mozilla_main_page_logo().is_displayed():
            mozilla_main.access_mozilla_all_lang_link()
            print("Mozilla - Download in Other Languages Link is Clicked")
        else:
            print("Mozilla - Download in Other Languages Link Unavailable. Exiting the test")
            driver.quit()
            driver.close()


if __name__ == '__main__':
    unittest.main()
