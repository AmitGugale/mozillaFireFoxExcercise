import unittest
from selenium import webdriver
from TestVariables.test_Variables import test_variables
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# The base class which all test cases can use. This class performs driver management


class testBase(unittest.TestCase):

    def setUp(self):
        if test_variables.browser == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            self.driver = webdriver.Chrome(GeckoDriverManager().install())
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed. Please check results")
