from appium_practices.common.myunit import StartEnd
from appium_practices.common.common_func import *
from ddt import ddt,data,unpack
import unittest
import logging

@ddt
class test_login(StartEnd):
    @data(('记录一下',),)
    @unpack
    def test_record(self,content):
        logging.info('记录流水')
        logging.info('test_login1')
        self.record.record_all(self.driver,content)
        self.assertTrue(self.record.check_recordStatus(self.driver))

if __name__ == '__main__':
    unittest.main()
