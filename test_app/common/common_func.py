import logging.config
# import logging
import os,yaml
from selenium.common.exceptions import NoSuchElementException

#获取yaml日志
def get_yaml():
    with open(r'E:\python\envname\Scripts\imooc\appium_practices\confg\kyb_caps.yaml','r') as file:
        data=yaml.load(file,Loader=yaml.FullLoader)
    return data

#日志加载
# def get_logger():
#     filename=os.path.dirname(os.path.dirname(__file__))
#     log_filename=os.path.join(filename,'confg','log.conf')
#
#     logging.config.fileConfig(log_filename)
#     return logging.getLogger()

#截图
def get_screen(driver,filename):
    filepath=r'E:\python\envname\Scripts\imooc\appium_practices\screenshot'
    file_name=filepath+'/'+filename+'.png'
    driver.get_screenshot_as_file(file_name)

# 获取屏幕长宽
def get_size(driver):
    x=driver.get_window_size()['width']
    y=driver.get_window_size()['height']
    return x,y

#向左滑动操作
def swip_left(driver):
    l=get_size(driver)
    x1=int(l[0]*0.8)
    x2=int(l[0]*0.2)
    y1=int(l[1]*0.5)
    return driver.swipe(x1,y1,x2,y1,1000)

#向上滑动
def swipe_up(driver, element):
    # 通过resoure-id知道view
    ele = driver.find_element_by_id(element)
    # 获取到view的宽和高
    w = ele.size['width']
    h = ele.size['height']
    # 获取到view的起始纵坐标----977，其实横坐标为0
    x = ele.location['x']
    y = ele.location['y']
    x1 = int(w / 2 + x)
    y1 = int(h / 5 * 4 + y)
    y2 = int(h / 5 * 3 + y)
    return driver.swipe(x1, y1, x1, y2, 1000)

if __name__ == '__main__':
    filename=os.path.dirname(os.path.dirname(__file__))
    log_filename=os.path.join(filename,'confg','log.conf')
    print(log_filename)
