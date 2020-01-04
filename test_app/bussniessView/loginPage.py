from appium_practices.basicView.basicView import BaseView
from appium_practices.common.common_func import *
from appium_practices.common.desired_caps import appium_desired
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Login_page(BaseView):
    # 首先检查取消、跳过、是否登录过
    cancelButton=(By.ID,'android:id/button2')
    skipButton=(By.ID,'com.tal.kaoyan:id/tv_skip')
    mybutton=(By.ID,'com.tal.kaoyan:id/mainactivity_button_mysefl')
    usercenterBtn=(By.ID,'com.tal.kaoyan:id/activity_usercenter_username')

    #输入用户名、密码、点击登录
    username_type=(By.ID,'com.tal.kaoyan:id/login_email_edittext')
    password_type=(By.ID,'com.tal.kaoyan:id/login_password_edittext')
    loginBtn=(By.ID,'com.tal.kaoyan:id/login_login_btn')

    #登出操作
    RightButton=(By.ID,'com.tal.kaoyan:id/myapptitle_RightButton_textview')
    logout_text=(By.ID,'com.tal.kaoyan:id/setting_logout_text')
    tip_commit=(By.ID,'com.tal.kaoyan:id/tip_commit')

    def login_actin(self,driver,username,password):
        get_logger().info('========开始登录==========')
        #首先检查取消、跳过、是否登录过
        try:
            ele = self.find_element(*self.cancelButton)
        except NoSuchElementException:
            get_logger().info('没有取消按钮')
        else:
            ele.click()

        try:
            ele1 = self.find_element(*self.skipButton)
        except NoSuchElementException:
            get_logger().info('没有跳过按钮')
        else:
            ele1.click()

        try:
            ele2 = self.find_element(*self.mybutton)
        except NoSuchElementException:
            get_logger().info('没有我的按钮')
        else:
            ele2.click()
            self.find_element(*self.usercenterBtn).click()

        #正式进入登录页面
        self.find_element(*self.username_type).clear()
        self.find_element(*self.username_type).send_keys(username)
        self.find_element(*self.password_type).send_keys(password)
        get_screen(driver,'登录')
        self.find_element(*self.loginBtn).click()
        sleep(3)
        get_screen(driver,'登录是否成功')

    def logout(self):
        get_logger().info('开始登出')
        self.find_element(*self.RightButton).click()
        self.find_element(*self.logout_text).click()
        self.find_element(*self.tip_commit).click()

    def check_loginStatus(self):
        try:
            self.find_element(*self.mybutton).click()
            ele3=self.find_element(*self.usercenterBtn)
        except NoSuchElementException:
            get_logger().info('登陆失败')
            return False
        else:
            get_logger().info('登陆成功')
            self.logout()
            return True

if __name__ == '__main__':
    driver=appium_desired()
    l=BaseView(driver)
    Login_page(l).login_actin(driver,'','')
    Login_page(l).check_loginStatus()
