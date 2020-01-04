from appium import webdriver
from appium_practices.common.common_func import *
import os
import logging.config

filename = os.path.dirname(os.path.dirname(__file__))
log_filename = os.path.join(filename, 'confg', 'log.conf')
logging.config.fileConfig(log_filename)
logging = logging.getLogger()

data = get_yaml()

device_list=['127.0.0.1:62001','127.0.0.1:62025']

def appium_desired(udid,port):
    desired_caps = {}

    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    desired_caps['udid'] = udid     #需要加上这个udid用来定义设备列表
    filename = os.path.dirname(os.path.dirname(__file__))
    app_filename = os.path.join(filename, 'app', data['appname'])
    desired_caps['app'] = app_filename
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    desired_caps['noReset'] = data['noReset']
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']

    logging.info('启动app')
    driver = webdriver.Remote('http://{}:{}/wd/hub'.format(data['ip'], port), desired_caps)
    return driver

if __name__ == '__main__':
    appium_desired(device_list[0],4723)
    appium_desired(device_list[1],4725)