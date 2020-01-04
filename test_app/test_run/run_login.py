import unittest
from BSTestRunner import BSTestRunner
from time import strftime
import sys,logging
from appium_practices.common.common_func import *

path=r'E:\\python\\envname\\Scripts\\imooc\\'
sys.path.append(path)

test_dir=r'E:\\python\\envname\\Scripts\\imooc\\appium_practices\\test_case'
report_dir=r'E:\\python\\envname\\Scripts\\imooc\\appium_practices\\test_report'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_record.py')
now=strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' report.html'

with open(report_name,'wb') as file:
    runner=BSTestRunner(stream=file,title='appium test',description='report')
    logging.info('start test report')
    runner.run(discover)
