import unittest
from driver.driver import browser
from Website.test_case.pageObject.login_page import *

class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.maximize_window()
        self.a=BasePage(self.driver)
        self.a.open()
        self.b=LoginPage(self.a)

    def tearDown(self):
        self.driver.quit()
