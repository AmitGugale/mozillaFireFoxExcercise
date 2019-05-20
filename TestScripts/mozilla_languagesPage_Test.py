from TestVariables.test_Variables import test_variables
from PageObjects.Pages.mozillaFirefoxLanguagesPage import mozilla_Firefox_Languages_Page
from TestBase.testBase import testBase
import unittest

# This Test Accesses the Mozilla Download in Other Languages Page,confirms the presence of the mozilla logo
# and displays the entire set of available languages as result.


class mozilla_langPage_Test(testBase):

    def test_mozilla_mainPage(self):
        driver = self.driver
        driver.get(test_variables.mozilla_languages_page_link)
        mozilla_lang = mozilla_Firefox_Languages_Page(driver)
        lang_output = ''

        # Functionality is performed only if the logo is confirmed to be displayed

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


if __name__ == '__main__':
    unittest.main()
