from Website.test_case.pageObject.base_page import BasePage
from Website.test_case.modle.function import *
from selenium.webdriver.common.by import By
from driver.driver import browser

logger=get_logger()

class LoginPage(BasePage):
    loc=(By.CLASS_NAME,'link-login')
    select_ele=(By.LINK_TEXT,'账户登录')
    loginname=(By.ID,'loginname')
    pwd=(By.ID,'nloginpwd')
    submit=(By.ID,'loginsubmit')
    #为了准确获取cookies点击
    ex=(By.CLASS_NAME,'nickname')

    #登录动作
    def login_action(self,driver,username,password):
        # driver=self.driver
        logger.info('-----------开始登录----------')
        # self.driver.get("https://www.jd.com")
        self.find_element(*self.loc).click()
        self.find_element(*self.select_ele).click()
        self.find_element(*self.loginname).send_keys(username)
        self.find_element(*self.pwd).send_keys(password)
        self.find_element(*self.submit).click()
        try:
            ele1=self.find_element(*self.ex)
            ele1.click()
        except:
            pass
        get_screen_shot(driver,'登录成功截图.png')
        logger.info('获取cookies')
        get_cookies(driver)

    #检查登录状态
    def check_login_status(self,driver,username,password):
        try:
            while True:
                login_status=check_login_status(driver)
                if login_status==True:
                    break
                else:
                    self.login_action(driver,username,password)
                    break
        finally:
            # driver.quit()
            pass

if __name__ == '__main__':
    driver=browser()
    driver.maximize_window()
    a=BasePage(driver)
    # a.open()
    LoginPage(a).check_login_status(driver,'','')

    # check_login_status(driver)