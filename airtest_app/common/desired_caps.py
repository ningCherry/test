# -*- encoding=utf8 -*-
__author__ = "ninghaidan"

from airtest.core.api import *  #导入所有方法

import logging.config
from config.caps import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# import time,os
# ti=time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())

# from airtest.cli.parser import cli_setup
# if not cli_setup():
#     '''
    # #判断文件夹是否存在
    # file_dir=BASE_DIR+'/log/log-'+ti
    # if not os.path.exists(file_dir):
    #     print(file_dir)
    #     os.mkdir(file_dir)
    # auto_setup(file_dir+'/',logdir=True,devices=["Android:///"])

    # auto_setup('./log/',logdir=True,devices=["Android:///"])
    # '''


log_filename = os.path.join(CONF_DIR, 'log.conf')
logging.config.fileConfig(log_filename)
logging=logging.getLogger()
