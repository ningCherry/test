from Website.test_case.modle.function import *
from Website.test_case.modle.myunit import StartEnd
from Website.test_case.pageObject.login_page import *
import unittest
from ddt import ddt,data,unpack

logger=get_logger()

@ddt
class Login_test(StartEnd):
    csv_file=r'E:\python练习库\jd_practices全流程\Website\test_data\smelp.csv'

    @unittest.skip('normal')
    def test_login_normal(self):
        logger.info('start test_login1_normal')
        a=BasePage(self.driver)
        a.open()
        b=LoginPage(a)
        data=get_csv_date(self.csv_file,0)
        b.login_action(self.driver,data[0],data[1])
        # b.check_login_status(self.driver,data[0],data[1])
        get_screen_shot(self.driver,'test_login1_normal.png')

    @unittest.skip('error')
    def test_login_error(self):
        logger.info('start test_login_error')
        a=BasePage(self.driver)
        a.open()
        b=LoginPage(a)
        data=get_csv_date(self.csv_file,1)
        b.login_action(self.driver,data[0],data[1])
        get_screen_shot(self.driver, 'test_login_error.png')

    @unittest.skip('empty')
    def test_login_empty(self):
        logger.info('start test_login_empty')
        a=BasePage(self.driver)
        a.open()
        b=LoginPage(a)
        data=get_csv_date(self.csv_file,2)
        b.login_action(self.driver,'','')
        get_screen_shot(self.driver, 'test_login_empty.png')

    # @data(('','afsada0'),('',''))
    @data(('','afsada0'),)
    @unpack
    def test_login_ddt(self,username,password):
        '''test_login_ddt'''
        logger.info('start test_login_ddt')
        # a=BasePage(self.driver)
        # a.open()
        # b=LoginPage(a)
        self.b.login_action(self.driver,username,password)
        get_screen_shot(self.driver, 'test_login_ddt.png')

if __name__ == '__main__':
    unittest.main()