import unittest
from .desired_caps import *
from common.common_func import *

# class StartEnd(unittest.TestCase):
#     def setUp(self):
#         logging.info('==========setUp==========')
#         start_app("com.mt.trader.app")  # 启动程序
#
#
#     def tearDown(self):
#         logging.info('==========tearDown==========')
#         sleep(2)
#         stop_app("com.mt.trader.app")  # 停止程序

#我的页面前置条件
class Test_my():
    def setup_method(self):
        logging.info('==========setUp==========')
        start_app("com.mt.trader.app")  # 启动程序
        ele_exists('my_data.xls', 'my', 'banner图') #判断首页banner图是否存在
        handle_poco_click('my_data.xls', 'my/', '我的') #点击我的TAB

    def teardown_method(self):
        logging.info('==========tearDown==========')
        sleep(2)
        stop_app("com.mt.trader.app")  # 停止程序


#发现页的前置条件
class Test_find():
    def setup_method(self):
        logging.info('==========setUp==========')
        start_app("com.mt.trader.app")  # 启动程序
        ele_exists('my_data.xls', 'my', 'banner图') #判断首页banner图是否存在
        handle_poco_click('find_data.xls', 'find/立即开户', '发现页') #点击发现TAB

    def teardown_method(self):
        logging.info('==========tearDown==========')
        sleep(2)
        stop_app("com.mt.trader.app")  # 停止程序





