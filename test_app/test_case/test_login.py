from appium_practices.common.myunit import StartEnd
from appium_practices.common.common_func import *
import ddt
import unittest

@ddt.ddt
class test_login(StartEnd):

    @ddt.data(('宁樱樱', '**'),)
    @ddt.unpack
    def test_login1(self,username,password):
        get_logger().info('test_login1')
        self.login.login_actin(self.driver,username,password)
        self.assertTrue(self.login.check_loginStatus())


if __name__ == '__main__':
    unittest.main()

