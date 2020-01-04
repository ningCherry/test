from appium_practices.basicView.basicView import BaseView
from appium_practices.common.common_func import *
from appium_practices.common.desired_caps import appium_desired
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import logging

class RecordPage(BaseView):
    #点击开始随手记
    start_record_button=(By.ID,'com.mymoney:id/begin_btn')
    '''记录流水'''
    #记一笔
    one_running=(By.ID,'com.mymoney:id/add_expense_quickly_btn')
    #输入金额
    one=(By.ID,'com.mymoney:id/one')
    two=(By.ID,'com.mymoney:id/two')
    zero=(By.ID,'com.mymoney:id/zero')
    ok=(By.ID,'com.mymoney:id/ok')
    #选择分类和账户
    ele_one=(By.ID,'com.mymoney:id/category_item_ly')
    ele_two=(By.ID,'com.mymoney:id/account_item_ly')
    ele1='com.mymoney:id/first_level_wv'
    ele2='com.mymoney:id/second_level_wv'

    #点击备注
    remarks=(By.ID,'com.mymoney:id/memo_ly')
    #填写备注
    remarks_value=(By.ID,'com.mymoney:id/memo_et')
    #点击保存
    save_button=(By.ID,'com.mymoney:id/save_btn')

    '''检查流水'''
    #点击今天
    today="今天"
    #检查分类和金额、备注
    type=(By.ID,'com.mymoney:id/title_tv')
    num=(By.ID,'com.mymoney:id/cost_tv')
    memo=(By.ID,'com.mymoney:id/memo_tv')

    #开始随手记
    def getin_record(self,driver):
        logging.info('进入随手记app')
        #等待下一步元素出现
        WebDriverWait(driver,20).until(lambda x:x.find_element_by_id("com.mymoney:id/next_btn"))

        #向右滑动两次
        for i in range(2):
            swip_left(driver)
            sleep(2)

        self.find_element(*self.start_record_button).click()
        sleep(1)
        get_screen(driver,'随手记')

    #记一笔流水
    def record_running(self,driver,content):
        logging.info('记录流水')
        self.find_element(*self.one_running).click()
        #输入金额
        self.find_element(*self.one).click()
        self.find_element(*self.two).click()
        self.find_element(*self.zero).click()
        self.find_element(*self.ok).click()
        sleep(3)
        self.find_element(*self.ele_one).click()
        sleep(1)
        #选择分类
        for i in range(3):
            swipe_up(driver,self.ele1)
            sleep(1)

        for i in range(2):
            swipe_up(driver,self.ele2)
            sleep(1)

        self.find_element(*self.ele_two).click()
        #选择账户
        for i in range(3):
            swipe_up(driver,self.ele1)
            sleep(1)

        for i in range(2):
            swipe_up(driver,self.ele2)
            sleep(1)

        self.find_element(*self.remarks).click()
        self.find_element(*self.remarks_value).send_keys(content)
        sleep(1)
        get_screen(driver,'记录流水')
        sleep(1)
        self.find_element(*self.save_button).click()
        sleep(3)

    #检查是否纪录成功
    def check_recordStatus(self,driver):
        logging.info('检查是否纪录成功')
        driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(self.today)).click()
        sleep(1)
        type_value = self.find_element(*self.type).text
        num_value = self.find_element(*self.num).text
        memo_value = self.find_element(*self.memo).text
        print(type_value,num_value,memo_value)
        sleep(1)
        get_screen(driver, '记录')
        if type_value=='私家车费用' and num_value=='120.00' and memo_value=='记录一下':
            logging.info('纪录成功')
            return True
        else:
            logging.info('记录失败')
            return False

    def record_all(self,driver,content):
        self.getin_record(driver)
        self.record_running(driver,content)
        # self.check_recordStatus(driver)

if __name__ == '__main__':
    driver=appium_desired()
    l=BaseView(driver)
    RecordPage(l).record_all(driver,'记录一下')


