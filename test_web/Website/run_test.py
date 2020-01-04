import unittest,time
from BSTestRunner import BSTestRunner
from Website.test_case.modle.function import *

logger=get_logger()

test_dir='./test_case'
repor_dir='./test_report'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_login.py')

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_file=repor_dir+'/'+now+'report.html'

logger.info('start test case')
with open(report_file,'wb') as f:
    runner=BSTestRunner(stream=f,title='ning test report',description='ning')
    runner.run(discover)
    f.close()

# logger.info('send mial...')
# send_mail(latest_report())
# logger.info('end')
