from appium import webdriver
from appium_practices.common.common_func import *
import os
import logging.config

filename = os.path.dirname(os.path.dirname(__file__))
log_filename = os.path.join(filename, 'confg', 'log.conf')
logging.config.fileConfig(log_filename)
logging=logging.getLogger()

data=get_yaml()

def appium_desired():
    desired_caps={}

    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    filename=os.path.dirname(os.path.dirname(__file__))
    app_filename=os.path.join(filename,'app',data['appname'])
    desired_caps['app']=app_filename
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']
    desired_caps['unicodeKeyboard']=data['unicodeKeyboard']
    desired_caps['resetKeyboard']=data['resetKeyboard']

    logging.info('启动app')
    driver=webdriver.Remote('http://{}:{}/wd/hub'.format(data['ip'],data['port']),desired_caps)
    
    return driver


if __name__ == '__main__':
    appium_desired()