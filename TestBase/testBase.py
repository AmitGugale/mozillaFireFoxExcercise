import unittest
from selenium import webdriver
from TestVariables.test_Variables import test_variables

# The base class which all test cases can use. This class performs driver management


class testBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(test_variables.chromedriver_location)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed. Please check results")
