import os

#项目根目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

#日志文件
LOG_DIR=os.path.join(BASE_DIR,'logs')

#截图文件
SCRE_DIR=os.path.join(BASE_DIR,'screenshot')

#配置文件
CONF_DIR=os.path.join(BASE_DIR,'config')

#测试数据文件
DATA_DIR=os.path.join(BASE_DIR,'test_data')

#测试图片文件
PIC_DIR=os.path.join(DATA_DIR,'air_picture')

#测试案例文件
TEST_DIR=os.path.join(BASE_DIR,'test_case')

#测试报告文件
REPORT_DIR=os.path.join(BASE_DIR,'test_report/xml')

# print(BASE_DIR)