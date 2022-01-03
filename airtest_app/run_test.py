from common.common_func import *
import pytest,os,time

ti=time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

#执行案例
test_dir= r'fuli_ui/test_case/test_case_my.py'
#生成报告文件
test_report=REPORT_DIR+'/xml-'+ti
#美化报告
html_dir= r'./test_report/html'

#获取最新报告
latest_report=latest_report()
print(latest_report)
# print(html_dir)


'''
## 生成配置信息 "-s 代表可以将执行成功的案例日志打印出来 ; -q+文件执行路径 代表只需要执行的文件"
# pytest.main(['-s', '-q', test_dir, '--alluredir', test_report])

# 运行类中的指定用例
# pytest.main(['-s', '-q', './test_case/test_case_my.py::Test_my::test_my_info','./test_case/test_case_my.py::Test_my::test_system_setting', '--alluredir', test_report])
# pytest.main(['-s', '-q', './test_case/test_case_my.py::Test_my::test_my_info', '--alluredir', test_report])

#  # 匹配test_case.py模块下包含test_my_info的用例
# pytest.main(['-s', '-q', '-k','test_my_info','./test_case/test_case_my.py', '--alluredir', test_report])


#os模块运行allure命令，来生成html格式的报告（根据刚刚生成的配置信息）
# os.system('/Users/ninghaidan/Downloads/allure-2.15.0/bin/allure ' 'generate ' './test_case/report/xml-2021-09-17-15:19:27 ' '-o ' './test_case/report/html ' '--clean')

'''
# pytest.main(['-s', '-q', './test_case/test_case_my.py::Test_my::test_my_message', '--alluredir', test_report])

# pytest.main(['-s', '-q', test_dir, '--alluredir', test_report])

os.system("/Users/ninghaidan/Downloads/allure-2.15.0/bin/allure generate %s -o %s --clean"%(latest_report,html_dir))

# #失败的用例重新执行
# os.system("pytest -s --reruns 1")


