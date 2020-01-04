import unittest
from appium_practices.bussniessView.loginPage import Login_page
from appium_practices.bussniessView.record_parctice import RecordPage
from appium_practices.common.desired_caps import *
from appium_practices.basicView.basicView import BaseView
from appium_practices.common.common_func import *
from time import sleep

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info('==========setUp==========')
        self.driver=appium_desired()
        self.l = BaseView(self.driver)
        self.login=Login_page(self.l)
        self.record=RecordPage(self.l)

    def tearDown(self):
        logging.info('==========tearDown==========')
        sleep(5)
        self.driver.close_app()