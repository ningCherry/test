import sys,os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)

from common.myunit import *
import pytest,allure

@allure.severity("normal")  #用例等级-blocker、critical、normal、minor、trivial
@allure.epic("项目名称：发现TAB") #epic描述
# @allure.issue("http://rhjs.techgp.cn/zentao/bug-browse-124-0-openedbyme.html")  #缺陷地址
# @allure.testcase("https://www.cnblogs.com/Zhan-W/p/13141219.html") #测试用例的连接地址
@allure.feature('test-find')  #模块名称
# class Test_find():
class Test_find(Test_find):
# class Test_find(StartEnd):
    # 基本信息
    filename='find_data.xls'  #poco元素定位存放位置
    pic_file='find'  #airtest元素定位存放位置
    #各模块截图文件存放位置
    pic_file_account = pic_file + '/立即开户'
    pic_file_look = pic_file + '/investmentx_school' + '/新手必看'
    pic_file_shares = pic_file + '/investmentx_school' + '/股票百科'
    pic_file_class = pic_file + '/investmentx_school' + '/进阶课堂'
    pic_file_broadcast = pic_file + '/互动直播'
    pic_file_global = pic_file + '/慧投全球'
    pic_file_calendar = pic_file + '/财经日历'
    pic_file_attack= pic_file + '/直击港股'
    pic_file_selector = pic_file + '/选股器'
    pic_file_AI = pic_file + '/AI诊股'
    pic_file_info = pic_file + '/资讯'

    datas=get_yaml()['find'] #获取yaml测试数据

    @allure.story('发现页-立即开户')  #用例名称
    @allure.title('发现页-立即开户')  #用例标题
    def test_immediately_account(self):
        allure.step(">>>>>>>>>>>>>>开始发现页-立即开户模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-立即开户模块测试>>>>>>>>>>>>>>')

        handle_air(self.pic_file, '立即开户')  #airtest元素定位
        # handle_air(self.pic_file, '开户页关闭')
        handle_poco_click(self.filename, self.pic_file_account, '发现页') #poco元素定位


    # @pytest.mark.skip
    @allure.story('发现页-投资学堂')
    @allure.title('发现页-投资学堂')
    def test_investmentx_school(self):
        handle_air(self.pic_file, '投资学堂') #airtest元素定位
        allure.step(">>>>>>>>>>>>>>开始发现页-投资学堂-新手必看模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-投资学堂-新手必看模块测试>>>>>>>>>>>>>>')
        handle_poco_click(self.filename, self.pic_file_look, '新手必看') #poco元素定位
        handle_poco_click(self.filename, self.pic_file_look, '如何开户入金')
        handle_poco_click(self.filename, self.pic_file_look, '香港及境外卡入金', 'BACK')
        handle_poco_click(self.filename, self.pic_file_look, '如何交易港美股')
        handle_poco_click(self.filename, self.pic_file_look, '美股交易规则', 'BACK')
        handle_poco_click(self.filename, self.pic_file_look, '玩转ETF')
        handle_poco_click(self.filename, self.pic_file_look, 'ETF是什么', 'BACK')
        swip_left(self.filename, '玩转ETF') #向左滑动
        handle_poco_click(self.filename, self.pic_file_look, '打新全攻略')
        handle_poco_click(self.filename, self.pic_file_look, '新股申购小贴士：一文详解打新流程', 'BACK')
        swip_left(self.filename, '玩转ETF')
        handle_poco_click(self.filename, self.pic_file_look, '窝轮牛熊证')
        swip_up(self.filename, '影响窝轮价格的因素')  #向上滑动
        handle_poco_click(self.filename, self.pic_file_look, '窝轮与牛熊证的对比', 'BACK')
        keyevent("BACK")

        allure.step(">>>>>>>>>>>>>>开始发现页-投资学堂-股票百科模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-投资学堂-股票百科模块测试>>>>>>>>>>>>>>')
        handle_poco_click(self.filename, self.pic_file_shares, '股票百科')
        handle_poco_click(self.filename, self.pic_file_shares, '基础知识')
        handle_poco_click(self.filename, self.pic_file_shares, '主要经济数据','BACK')
        handle_poco_click(self.filename, self.pic_file_shares, '晨读好书')
        handle_poco_click_down(self.filename, self.pic_file_shares, '晨读好书', 'BACK')
        handle_poco_click(self.filename, self.pic_file_shares, '股票技术指标')
        handle_poco_click_down(self.filename, self.pic_file_shares, '股票技术指标','BACK')
        swip_left(self.filename, '股票技术指标')
        handle_poco_click(self.filename, self.pic_file_shares, '股票行情指标')
        handle_poco_click_down(self.filename, self.pic_file_shares, '股票行情指标', 'BACK')
        swip_left(self.filename, '股票技术指标')
        handle_poco_click(self.filename, self.pic_file_shares, '股票财务指标')
        handle_poco_click_down(self.filename, self.pic_file_shares, '股票财务指标', 'BACK')
        keyevent("BACK")
        swip_up(self.filename, '股票百科')

        allure.step(">>>>>>>>>>>>>>开始发现页-投资学堂-进阶课堂模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-投资学堂-进阶课堂模块测试>>>>>>>>>>>>>>')
        handle_poco_click(self.filename, self.pic_file_class, '进阶课堂')
        handle_poco_click(self.filename, self.pic_file_class, '美股进阶')
        handle_poco_click(self.filename, self.pic_file_class, '什么是TQQQ', 'BACK')
        handle_poco_click(self.filename, self.pic_file_class, '港股进阶')
        handle_poco_click(self.filename, self.pic_file_class, '打新进阶')
        handle_poco_click(self.filename, self.pic_file_class, 'ETF进阶')
        swip_left(self.filename, '打新进阶')
        handle_poco_click(self.filename, self.pic_file_class, '读懂财务报表')
        handle_poco_click(self.filename, self.pic_file_class, '如何读懂财务报表', 'BACK')
        keyevent("BACK")
        keyevent("BACK")


    # @pytest.mark.skip
    @allure.story('发现页-互动直播')
    @allure.title('发现页-互动直播')
    def test_broadcast(self):
        allure.step(">>>>>>>>>>>>>>开始发现页-互动直播模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-互动直播模块测试>>>>>>>>>>>>>>')
        click_resolving(0.5,0.15)  #利用相对坐标点击互动直播
        sleep(1)
        handle_poco_click(self.filename, self.pic_file_broadcast, '直播互动') #poco元素定位
        handle_poco_click(self.filename, self.pic_file_broadcast, '点击精选')
        handle_poco_click(self.filename, self.pic_file_broadcast, '点击全部')
        handle_poco_click(self.filename, self.pic_file_broadcast, '交易计划')
        handle_poco_click(self.filename, self.pic_file_broadcast, '富利研究')
        handle_poco_click(self.filename, self.pic_file_broadcast, '机构看好')
        handle_poco_click_down(self.filename, self.pic_file_broadcast, '机构看好', 'BACK')  # 根据相对坐标来点击元素下方的元素
        handle_poco_click(self.filename, self.pic_file_broadcast, '个股调研')
        handle_poco_click_down(self.filename, self.pic_file_broadcast, '个股调研', 'BACK')
        ele_exists(self.filename, self.pic_file_broadcast, '点击股票', 'BACK') #判断元素是否存在
        handle_poco_click(self.filename, self.pic_file_broadcast, '富利研选')
        handle_poco_click_down(self.filename, self.pic_file_broadcast, '富利研选', 'BACK')
        handle_poco_click(self.filename, self.pic_file_broadcast, '点击分享图标')
        handle_poco_click(self.filename, self.pic_file_broadcast, '微信好友')
        handle_air(self.pic_file, '微信分享')  #airtest元素定位
        handle_poco_click(self.filename, self.pic_file_broadcast, '点击分享')
        handle_poco_click(self.filename, self.pic_file_broadcast, '返回富利港美股')
        keyevent("BACK")


    # @pytest.mark.skip
    @allure.story('发现页-慧投全球')
    @allure.title('发现页-慧投全球')
    def test_global(self):
        allure.step(">>>>>>>>>>>>>>开始发现页-慧投全球模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-慧投全球模块测试>>>>>>>>>>>>>>')
        handle_air(self.pic_file, '慧投全球')  #airtest元素定位
        handle_poco_click(self.filename, self.pic_file_global, '美股ETF','BACK')
        handle_poco_click(self.filename, self.pic_file_global, '港股ETF','BACK')
        handle_poco_click(self.filename, self.pic_file_global, '全球ETF')
        handle_poco_click(self.filename, self.pic_file_global, 'ACWI','BACK')
        asser_ele_in(self.filename,'ACWI','ACWI')  #断言元素是否存在
        handle_poco_click(self.filename, self.pic_file_global, 'BKF','BACK')
        swip_up(self.filename,'BKF')  #向上滑动
        handle_poco_click(self.filename, self.pic_file_global, 'EWZ','BACK')
        swip_down(self.filename, 'EWZ')  # 向下滑动
        handle_poco_click(self.filename, self.pic_file_global, '行业ETF')
        handle_poco_click(self.filename, self.pic_file_global, 'VNQ','BACK')
        asser_ele_in(self.filename, 'VNQ', 'VNQ') #断言元素是否存在
        handle_poco_click(self.filename, self.pic_file_global, '其他ETF')
        handle_poco_click(self.filename, self.pic_file_global, 'TLT','BACK')
        # handle_poco_click(self.filename, self.pic_file_global, 'GLD','BACK')
        swip_down(self.filename, '行业ETF')  #向下滑动
        handle_air(self.pic_file, '港股市场')
        handle_poco_click(self.filename, self.pic_file_global, '03092','BACK')
        handle_poco_click(self.filename, self.pic_file_global, '03020','BACK')
        handle_poco_click(self.filename, self.pic_file_global, '行业ETF')
        handle_poco_click(self.filename, self.pic_file_global, '03121','BACK')
        asser_ele_in(self.filename, '03121', '03121')
        handle_poco_click(self.filename, self.pic_file_global, '02806','BACK')
        handle_poco_click(self.filename, self.pic_file_global, '其他ETF')
        handle_poco_click(self.filename, self.pic_file_global, '02840','BACK')
        swip_up(self.filename, '全球ETF')
        swip_up(self.filename, 'DIA')
        handle_poco_click(self.filename, self.pic_file_global, 'DIA','BACK')
        handle_poco_click(self.filename, self.pic_file_global, 'UDOW','BACK')
        handle_poco_click(self.filename, self.pic_file_global, 'DOG','BACK')
        asser_ele_in(self.filename, 'DOG', 'DOG')
        handle_poco_click(self.filename, self.pic_file_global, 'DXD','BACK')
        handle_poco_click(self.filename, self.pic_file_global, 'SDOW','BACK')
        handle_poco_click(self.filename, self.pic_file_global, '港股市场')
        handle_poco_click(self.filename, self.pic_file_global, '07261','BACK')
        handle_poco_click(self.filename, self.pic_file_global, '02833','BACK')
        asser_ele_in(self.filename, '02833', '02833')
        handle_poco_click(self.filename, self.pic_file_global, '07500','BACK')
        handle_poco_click(self.filename, self.pic_file_global, '07522','BACK')
        keyevent("BACK")


    # @pytest.mark.skip
    @allure.story('发现页-财经日历')
    @allure.title('发现页-财经日历')
    def test_calendar(self):
        allure.step(">>>>>>>>>>>>>>开始发现页-财经日历模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-财经日历模块测试>>>>>>>>>>>>>>')
        handle_air(self.pic_file, '财经日历')
        handle_poco_click(self.filename, self.pic_file_calendar, '今天')
        click_resolving(0.5, 0.25)  # 利用相对坐标点击文章
        ti = time.strftime("%Y-%m-%d", time.localtime())
        asser_ele_in(self.filename,'公布时间',ti) #断言公布时间是否是今天
        keyevent("BACK")
        handle_poco_click(self.filename, self.pic_file_calendar, '点击日历控件')
        handle_poco_click(self.filename, self.pic_file_calendar, '点击确定')
        handle_poco_click(self.filename, self.pic_file_calendar, '事件','BACK')


    # @pytest.mark.skip
    @allure.story('发现页-直击港股')
    @allure.title('发现页-直击港股')
    def test_attack(self):
        allure.step(">>>>>>>>>>>>>>开始发现页-直击港股模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-直击港股模块测试>>>>>>>>>>>>>>')
        handle_air(self.pic_file, '直击港股')
        handle_poco_click(self.filename, self.pic_file_attack, '人气评分', 'BACK')
        click_resolving(0.5, 0.7,"BACK")  # 利用相对坐标点击股票
        handle_poco_click(self.filename, self.pic_file_attack, '最新价')
        handle_poco_click(self.filename, self.pic_file_attack, '涨跌幅')
        swip_up(self.filename,'五日人气')
        handle_poco_click(self.filename, self.pic_file_attack, '月度人气')
        swip_down(self.filename, '月度人气')
        click_resolving(0.5, 0.7,"BACK")
        handle_poco_click(self.filename, self.pic_file_attack, '最新价')
        handle_poco_click(self.filename, self.pic_file_attack, '涨跌幅')
        keyevent("BACK")


    # @pytest.mark.skip
    @allure.story('发现页-新股中心')
    @allure.title('发现页-新股中心')
    def test_IPO(self):
        allure.step(">>>>>>>>>>>>>>开始发现页-新股中心模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-新股中心模块测试>>>>>>>>>>>>>>')
        handle_air(self.pic_file, '新股中心')
        asser_ele_in(self.filename,'新股日历','新股日历') #断言是否进入新股中心
        keyevent("BACK")


    # @pytest.mark.skip
    @allure.story('发现页-选股器')
    @allure.title('发现页-选股器')
    @pytest.mark.parametrize("selector_name",datas["selector_name"])  #测试数据驱动
    def test_selector(self,selector_name):
        allure.step(">>>>>>>>>>>>>>开始发现页-选股器模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-选股器模块测试>>>>>>>>>>>>>>')
        handle_air(self.pic_file, '选股器')
        handle_air(self.pic_file, '选股器添加')
        handle_poco_click(self.filename, self.pic_file_selector, '行情指标')
        handle_poco_click(self.filename, self.pic_file_selector, '成交量')
        handle_poco_click(self.filename, self.pic_file_selector, '100万股-500万股')
        handle_poco_click(self.filename, self.pic_file_selector, '确定')
        handle_poco_click(self.filename, self.pic_file_selector, '保存')
        handle_poco_click(self.filename, self.pic_file_selector, '选股器名称')
        handle_poco(self.filename,'选股器名称').set_text(selector_name)  #输入选股器名称
        handle_poco_click(self.filename, self.pic_file_selector, '提交指标')
        handle_poco_click(self.filename, self.pic_file_selector, '范围')
        asser_ele_in(self.filename, '搜索结果', '搜索结果')  # 断言是否进入搜索结果页
        keyevent("BACK")
        handle_air(self.pic_file, '选股器修改')
        handle_poco_click(self.filename, self.pic_file_selector, '删除指标','BACK')


    # @pytest.mark.skip
    @allure.story('发现页-AI诊股')
    @allure.title('发现页-AI诊股')
    @pytest.mark.parametrize("stock_name", datas["stock_name"])  # 测试数据驱动
    def test_AI(self, stock_name):
        allure.step(">>>>>>>>>>>>>>开始发现页-AI诊股模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-AI诊股模块测试>>>>>>>>>>>>>>')
        handle_air(self.pic_file, 'AI诊股')
        handle_poco_click(self.filename, self.pic_file_AI, '查看详情')
        handle_poco_click(self.filename, self.pic_file_AI, '点击问号')
        handle_poco_click(self.filename, self.pic_file_AI, '我知道了')
        swip_up(self.filename, '支撑/阻力')
        handle_poco_click(self.filename, self.pic_file_AI, '资金流向')
        swip_up(self.filename, '主力净资金流向(万元)')
        handle_poco_click(self.filename, self.pic_file_AI, '舆情分析')
        handle_poco_click(self.filename, self.pic_file_AI, '基本面')
        swip_up(self.filename, '现金流')
        keyevent("BACK")
        click_resolving(0.5, 0.8,"BACK")   # 利用相对坐标点击股票
        handle_poco_click(self.filename, self.pic_file_AI, '开始诊断')
        handle_poco_click(self.filename, self.pic_file_AI, '输入股票名')
        handle_poco(self.filename, '输入股票名').set_text(stock_name)  # 输入股票名
        handle_poco_click(self.filename, self.pic_file_AI, '小米集团-W','BACK')
        keyevent("BACK")
        keyevent("BACK")


    @allure.story('发现页-帮助中心')
    @allure.title('发现页-帮助中心')
    def test_help(self):
        allure.step(">>>>>>>>>>>>>>开始发现页-帮助中心模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-帮助中心模块测试>>>>>>>>>>>>>>')
        handle_air(self.pic_file, '帮助中心')
        asser_ele_in(self.filename, '帮助中心', '帮助中心')  # 断言是否进入帮助中心页
        keyevent("BACK")


    # @pytest.mark.skip
    @allure.story('发现页-资讯')
    @allure.title('发现页-资讯')
    def test_info(self):
        allure.step(">>>>>>>>>>>>>>开始发现页-资讯模块测试>>>>>>>>>>>>>>")
        logging.info('>>>>>>>>>>>>>>开始发现页-资讯模块测试>>>>>>>>>>>>>>')
        handle_poco_click(self.filename, self.pic_file_info, '看点')
        click_resolving(0.5, 0.5, "BACK")  # 利用相对坐标点击文章
        click_resolving(0.5, 0.8, "BACK")
        handle_poco_click(self.filename, self.pic_file_info, '新股')
        click_resolving(0.5, 0.5, "BACK")
        handle_poco_click(self.filename, self.pic_file_info, '动态')
        handle_poco_click(self.filename, self.pic_file_info, '异动')
        handle_poco_click(self.filename, self.pic_file_info, '市场')
        handle_poco_click(self.filename, self.pic_file_info, '全部')
        swip_left(self.filename, '全部')
        handle_poco_click(self.filename, self.pic_file_info, '要闻')
        handle_poco_click(self.filename, self.pic_file_info, '公告')
        handle_poco_click(self.filename, self.pic_file_info, '研报')
        handle_poco_click(self.filename, self.pic_file_info, '港股')
        click_resolving(0.5, 0.5, "BACK")
        handle_poco_click(self.filename, self.pic_file_info, '美股')
        click_resolving(0.5, 0.5, "BACK")
        handle_poco_click(self.filename, self.pic_file_info, '专栏')
        handle_poco_click(self.filename, self.pic_file_info, '实时资讯')
        handle_poco_click(self.filename, self.pic_file_info, '一图看懂')
        click_resolving(0.5, 0.8, "BACK")
        handle_poco_click(self.filename, self.pic_file_info, '打新入门')
        handle_poco_click(self.filename, self.pic_file_info, '必读')
        click_resolving(0.5, 0.5, "BACK")
        handle_poco_click(self.filename, self.pic_file_info, '研究')
        click_resolving(0.5, 0.5, "BACK")
        handle_poco_click(self.filename, self.pic_file_info, '自选')
        click_resolving(0.5, 0.5, "BACK")
        handle_poco_click(self.filename, self.pic_file_info, '编辑更多')
        handle_air(self.pic_file, '自选')
        handle_air(self.pic_file, '完成')
        handle_poco_click(self.filename, self.pic_file_info, '编辑更多')
        handle_air(self.pic_file, '自选')
        handle_air(self.pic_file, '完成')



if __name__ == '__main__':
    # pytest.main(['-s', '-q', '-k','test_info','./test_case_find.py'])
    ti = time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())
    test_report = REPORT_DIR + '/xml-' + ti
    pytest.main(['-s', '-q', './test_case_find.py', '--alluredir', test_report])
    # pytest.main(['-s', '-q', './test_case_find.py'])
    # pytest.main(['-s', '-q', './test_case_find.py::Test_find::test_info'])
