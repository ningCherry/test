import sys
import unittest

path=r'E:\python\envname\Scripts\imooc'
sys.path.append(path)

from test_api.test_case.test_modle import RunTest


class test_run(unittest.TestCase):
    def setUp(self):
        print('start....')

    def tearDown(self):
        print('end')

    def test(self):
        RunTest().go_on_run()

if __name__ == '__main__':
    unittest.main()