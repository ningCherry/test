from Website.test_case.pageObject.base_page import BasePage
from Website.test_case.modle.function import *
from Website.orm.mysql_datebase import *
from selenium.webdriver.common.by import By
from driver.driver import browser
from selenium.webdriver.common.action_chains import ActionChains
from Website.test_case.pageObject.login_page import LoginPage
from time import sleep

class Goods_list_page(BasePage):
    first_list_name=(By.LINK_TEXT,'电脑')
    second_list_name=(By.LINK_TEXT,'显示器')

    def get_goods_list_driver(self):
        #初始化页面
        driver.get("https://list.jd.com/list.html?cat=670,671,672")
        logger.info('点击电脑-笔记本')
        # a=self.find_element(*self.first_list_name)
        # ActionChains(driver).move_to_element(a).perform()
        # sleep(2)
        # self.find_element(*self.second_list_name).click()
        # change_handle(driver)


    def get_selector_page(self):
        logger.info('点击-价格-评论')
        selector_condition_list=[]
        list1=(By.ID, "brand-11518")
        list2=(By.LINK_TEXT, "7000以上")
        list3=(By.LINK_TEXT, "评论数")
        list4=(By.XPATH, '//*[@id="plist"]/ul/li[1]/div/div[1]/a/img')

        selector_condition_list.append(list1)
        selector_condition_list.append(list2)
        selector_condition_list.append(list3)
        selector_condition_list.append(list4)

        for ele in selector_condition_list:
            self.find_element(*ele).click()
            sleep(1)
            change_handle(driver)

    def save_product_info(self):
        sleep(10)
        # js='window.ScrollTo(0,1000)'
        # driver.execute_script(js)
        js='window.scrollTo(0,1000)'
        driver.execute_script(js)

        sleep(6)
        loc=(By.XPATH,'//*[@id="detail"]/div[1]/ul/li[2]')
        self.find_element(*loc).click()

        logger.info('获取规格数据页截图')
        get_screen_shot(driver,'获取规格数据页截图.png')

        total_list = []
        total_loc=(By.CLASS_NAME,'Ptable-item')
        elements=driver.find_elements(*total_loc)
        for info_element in elements:
            info_element_dict = self.get_info_element_dict(info_element)
            total_list.append(info_element_dict)

        self.save_info_to_mysql(total_list)

    def save_info_to_mysql(self,total_list):
        goods=Good()
        logger.info('将文本存储至数据库')
        for info in total_list:
            for key,value in info.items():
                goods.insert(["computer_part","computer_info"],[str(key),str(value)])

    def get_info_element_dict(self,info_element):
        #第一列的值
        list1=(By.TAG_NAME,'h3')
        list1_info=self.find_element(*list1,element=info_element)

        #第二列的值
        list2=(By.TAG_NAME,'dt')
        list2_info=self.find_elements(*list2,element=info_element)
        # print(list2_info)

        #第三列的值
        list3=(By.XPATH,"dl//dd[not(contains(@class,'Ptable-tips'))]")
        list3_info=self.find_elements(*list3,element=info_element)
        # print(list3_info)

        logger.debug("获取到了所有的规格与包装信息")

        list_info={}
        parts_dict = {}
        for i in range(len(list2_info)):
            list_info[list2_info[i].text]=list3_info[i].text
        parts_dict[list1_info.text]=list_info

        return parts_dict

if __name__ == '__main__':
    driver=browser()
    driver.maximize_window()
    a=BasePage(driver)
    # a.open()
    LoginPage(a).check_login_status(driver,'','')
    Goods_list_page(a).get_goods_list_driver()
    Goods_list_page(a).get_selector_page()
    Goods_list_page(a).save_product_info()

