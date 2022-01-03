import sys,os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)

from common.common_func import *
from common.myunit import *
import pytest,allure

'''
#打包生成
airtest report ./fuli_ui/test_case --log_root ./fuli_ui/log --static_root ./fuli_ui/report  --plugin airtest_selenium.report poco.utils.airtest.report --lang zh --export ./fuli_ui/report_all/
#自己生成
airtest report ./fuli_ui/test_case --log_root ./fuli_ui/log --outfile ./fuli_ui/log.html --static_root ./fuli_ui/static  --plugin airtest_selenium.report poco.utils.airtest.report --lang zh
airtest report ./fuli_ui/test_case --log_root ./fuli_ui/my_report/log --outfile ./fuli_ui/log.html --static_root ./fuli_ui/my_report/static  --plugin airtest_selenium.report poco.utils.airtest.report --lang zh


airtest report ./fuli_ui/test_case --log_root ./fuli_ui/log1/log --outfile ./fuli_ui/log1.html --static_root ./fuli_ui/my_report/static  --plugin airtest_selenium.report poco.utils.airtest.report --lang zh
airtest report ./fuli_ui/test_case --log_root ./fuli_ui/log/log-2021-09-16-17:21:37/log --outfile ./fuli_ui/log.html --static_root ./fuli_ui/my_report/static  --plugin airtest_selenium.report poco.utils.airtest.report --lang zh

批量运行脚本
https://www.cnblogs.com/xuanjian-91/p/10375853.html
https://www.cnblogs.com/zhangxue521/p/12349789.html
https://blog.csdn.net/zhichuan0307/article/details/116461607

Pytest（完结篇）Pytest+Airtest+Allure实战！！！
https://blog.csdn.net/qq_42831466/article/details/115747820
https://www.likecs.com/show-179401.html
Airtest+Poco+Pytest框架搭建1
https://blog.csdn.net/George513/article/details/103544608
'''


@allure.severity("normal")  #用例等级-blocker、critical、normal、minor、trivial
@allure.epic("项目名称：我的页面") #epic描述
# @allure.issue("http://rhjs.techgp.cn/zentao/bug-browse-124-0-openedbyme.html")  #缺陷地址
# @allure.testcase("https://www.cnblogs.com/Zhan-W/p/13141219.html") #测试用例的连接地址
@allure.feature('test-my')  #模块名称
# class Test_my():
class Test_my(Test_my):
# class test_my(StartEnd):
    # 基本信息
    filename='my_data.xls'
    pic_file='my'
    datas=get_yaml()['my'] #获取yaml测试数据

    # @pytest.mark.skip
    @allure.story('基本信息')  #用例名称
    @allure.title('基本信息')
    @pytest.mark.parametrize("name",datas["name"])  #测试数据驱动
    def test_basic_info(self,name):
        allure.step(">>>>>>>>>>>>>>开始基本信息模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始基本信息模块测试>>>>>>>>>>>>>>')
        handle_poco_click(self.filename,self.pic_file,'基本信息')
        #上传头像
        # waitloading(self.filename,self.pic_file,'头像')
        # handle_poco_click(self.filename,self.pic_file,'头像-取消')
        # handle_air(self.pic_file,'从手机相册选择')
        # upload_snap()
        #修改昵称
        handle_poco_click(self.filename,self.pic_file,'昵称')
        handle_poco(self.filename,'修改昵称').set_text(name)
        handle_poco_click(self.filename, self.pic_file, '保存昵称')

        handle_poco_click(self.filename,self.pic_file,'手机号')
        handle_poco_click(self.filename,self.pic_file,'取消更换手机号')
        handle_poco_click(self.filename,self.pic_file,'微信号')
        waitloading(self.filename,self.pic_file,'再想一想','BACK')


    # @pytest.mark.skip
    @allure.story('我的页面')
    @allure.title('我的页面')
    def test_my_info(self):
        allure.step('>>>>>>>>>>>>>>开始我的页面测试>>>>>>>>>>>>>>')
        logging.info('>>>>>>>>>>>>>>开始我的页面测试>>>>>>>>>>>>>>')
        #专属客服
        handle_poco_click(self.filename,self.pic_file, '专属客服','BACK')
        #开户指南
        handle_air(self.pic_file,'开户指南')
        handle_air(self.pic_file,'开户指南-文章','BACK')
        keyevent("BACK")
        #股价提醒
        handle_poco_click(self.filename,self.pic_file, '股价提醒','BACK')
        #帮助中心
        handle_poco_click(self.filename,self.pic_file, '帮助中心')
        handle_air(self.pic_file,'帮助中心-标准收费表','BACK')
        sleep(0.5)
        handle_air(self.pic_file,'帮助中心-如何开户')
        sleep(0.5)
        handle_air(self.pic_file,'帮助中心-期货交易协议','BACK')
        keyevent("BACK")
        sleep(0.5)
        keyevent("BACK")
        # 联系客服
        handle_poco_click(self.filename,self.pic_file, '联系客服','BACK')
        #意见反馈
        handle_poco_click(self.filename,self.pic_file, '意见反馈')
        handle_air(self.pic_file, '意见反馈-我要反馈','BACK')
        handle_air(self.pic_file,'意见反馈-福利证券新股认购声明','BACK')
        handle_air(self.pic_file,'意见反馈-历史反馈','BACK')
        sleep(0.5)
        keyevent("BACK")
        # 投诉热线
        handle_poco_click(self.filename,self.pic_file, '投诉热线','BACK')


    # @pytest.mark.skip
    @allure.story('设置')
    @allure.title('设置')
    def test_system_setting(self):
        allure.step('>>>>>>>>>>>>>>开始设置模块测试>>>>>>>>>>>>>>')
        logging.info('>>>>>>>>>>>>>>开始设置模块测试>>>>>>>>>>>>>>')
        handle_poco_click(self.filename,self.pic_file, '设置')
        handle_poco_click(self.filename,self.pic_file, '账号管理','BACK')
        handle_poco_click(self.filename,self.pic_file, '检测版本')
        handle_poco_click(self.filename,self.pic_file, '关于我们','BACK')
        handle_poco_click(self.filename,self.pic_file, '免责声明','BACK')
        handle_poco_click(self.filename,self.pic_file, '个人隐私保护指引','BACK')
        handle_poco_click(self.filename,self.pic_file, '用户服务协议','BACK')
        handle_poco_click(self.filename,self.pic_file, '系统权限设置','BACK')
        keyevent("BACK")


    # @pytest.mark.skip
    @allure.story('我的banner')
    @allure.title('我的banner')
    def test_banner(self):
        swip_left(self.filename,'我的banner')
        swip_left(self.filename,'我的banner')


    # @pytest.mark.skip
    @allure.story('我的消息')
    @allure.title('我的消息')
    def test_my_message(self):
        handle_poco_click(self.filename, self.pic_file, '我的消息')
        handle_poco_click(self.filename, self.pic_file, '交易通知', 'BACK')
        handle_poco_click(self.filename, self.pic_file, '股价提醒', 'BACK')
        handle_poco_click(self.filename, self.pic_file, '系统消息', 'BACK')
        keyevent("BACK")


if __name__ == '__main__':
    # unittest.main()
    # pytest.main()
    ti = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    test_report = REPORT_DIR + '/xml-' + ti
    # pytest.main(['-s', '-q', './test_case_my.py'])
    pytest.main(['-s', '-q', './test_case_my.py', '--alluredir', test_report])
    # os.system('/Users/ninghaidan/Documents/allure-2.15.0/bin ' 'generate ' './report/xml ' '-o ' './report/html')
    '''
/Users/ninghaidan/Downloads/allure-2.15.0/bin/allure generate ./fuli_ui/test_case/report/xml -o ./fuli_ui/test_case/report/html
allure generate ./fuli_ui/test_case/report/xml -o ./fuli_ui/test_case/report/html --clean
    '''