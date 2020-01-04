import unittest
from BSTestRunner import BSTestRunner
from time import strftime

test_dir=r'E:\python\envname\Scripts\imooc\test_api\test_run'
report_dir=r'E:\python\envname\Scripts\imooc\test_api\test_report'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_run.py')

now=strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+'report.html'

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title='aaaaaaa',description='bbbbbb')
    runner.run(discover)

