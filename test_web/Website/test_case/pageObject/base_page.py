from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():
    def __init__(self,driver):
        self.driver=driver
        self.timeout=5

    def open(self):
        url='https://www.jd.com'
        self.driver.get(url)

    def find_element(self,*loc,timeout=None,element=None,wait_type='visibility',when_failed_close_browser=True):
        if element is not None:
            return self.init_wait(timeout).until(EC.visibility_of(element.find_element(*loc)))
        # return self.init_wait(timeout).until(EC.presence_of_element_located(loc))
        return self.driver.find_element(*loc)

        # try:
        #     if wait_type=='visibility':
        #         return self.init_wait(timeout).until(EC.visibility_of_element_located(loc))
        #     else:
        #         return self.init_wait(timeout).until(EC.presence_of_element_located(loc))
        # except NoSuchElementException:
        #     if when_failed_close_browser:
        #         self.driver.quit()
        #     raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(loc))
        # except TimeoutException:
        #     if when_failed_close_browser:
        #         self.driver.quit()
        #     raise TimeoutException(msg="定位元素失败,定位方式是:{}".format(loc))

    def find_elements(self, *loc, timeout=None, element=None, wait_type='visibility', when_failed_close_browser=True):
        if element is not None:
            return element.find_elements(*loc)

        try:
            if wait_type == 'visibility':
                return self.init_wait(timeout).until(EC.visibility_of_all_elements_located(loc))
            else:
                return self.init_wait(timeout).until(EC.presence_of_all_elements_located(loc))
        except NoSuchElementException:
            if when_failed_close_browser:
                self.driver.quit()
            raise NoSuchElementException(msg="定位元素失败,定位方式是:{}".format(loc))
        except TimeoutException:
            if when_failed_close_browser:
                self.driver.quit()
            raise TimeoutException(msg="定位元素失败,定位方式是:{}".format(loc))

    def init_wait(self,timeout):
        if timeout is None:
            return WebDriverWait(self.driver,timeout=self.timeout)
        else:
            return WebDriverWait(self.driver,timeout=timeout)

if __name__ == '__main__':
    from driver.driver import *
    driver=browser()
    b = BasePage(driver)
    b.open()
    loc=(By.LINK_TEXT,'电脑')
    b.find_element(*loc).click()