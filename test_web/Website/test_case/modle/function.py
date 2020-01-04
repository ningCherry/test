import logging.config,logging
import os,csv,json
import smtplib
from email.mime.text import  MIMEText
from email.header import Header
from driver.driver import *
from time import sleep

#日志加载器
def get_logger():
    log_file=r'E:\python练习库\jd_practices全流程\Website\confg\log.conf'
    logging.config.fileConfig(log_file)
    logger=logging.getLogger()
    return logger

logger=get_logger()

#截图方法
def get_screen_shot(driver,filename):
    screen_path=r'E:\python练习库\jd_practices全流程\Website\test_report\screen_shot'
    # file_path=screen_path+'\\'+filename
    file_path=os.path.join(screen_path,filename)
    logger.info('保存截图')
    driver.get_screenshot_as_file(file_path)

#发送邮件
def send_mail(latest_report):
    with open(latest_report,'rb') as f:
        content=f.read()
    f.close()

    smtpserver='smtp.163.com'

    user='15801801915@163.com'
    password=''

    sender='15801801915@163.com'
    recive=['834121195@qq.com', '']

    subject='lc_practies'
    msg=MIMEText(content,'html','utf-8')
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=sender
    msg['To']=','.join(recive)

    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user,password)

    logger.info('发送邮件')
    smtp.sendmail(sender,recive,msg.as_string())
    smtp.quit()

#获取最新报告
def latest_report():
    report_dir=r'E:\python练习库\jd_practices全流程\Website\test_report'
    lists=os.listdir(report_dir)
    lists.sort(key=lambda fn:os.path.getatime(report_dir+'/'+fn))
    logger.info('获取最新报告')
    file=os.path.join(report_dir,lists[-1])
    return file

#读取csv文件
def get_csv_date(csv_file,line):
    with open(csv_file,'r') as f:
        result=csv.reader(f)
        for index,row in enumerate(result):
            if index==line:
                return row

#检测文件夹是否建立
def  check_file(file_name):
    # file_path=os.path.dirname(os.getcwd())
    # file_dir=file_path+'/test_data/'+file_name
    file_dir='E:/python练习库/jd_practices全流程/Website/test_data/'+file_name
    if not os.path.exists(file_dir):
        os.mkdir(file_dir)
    return file_dir

#获取cookies
def get_cookies(driver):
    # 获取cookies的文件位置
    #获取cookies
    cookies=driver.get_cookies()
    file=check_file('cookies')
    with open(file+'/jd.cookies','w') as f:
        json.dump(cookies,f)

#加载cookies
def add_cookies(driver):
    file_path1 = check_file('cookies')
    if os.path.exists(file_path1+'\\jd.cookies'):
        with open(file_path1+'\\jd.cookies','r') as f:
            #读取文件全部内容
            a=f.read()
            #将读取的内容加载成pythona格式
            if a:
                cookies=json.loads(a)
                # 添加cookies
                for cookie in cookies:
                    driver.add_cookie(cookie)
            else:
                pass
    else:
        pass

#判断登录状态
def check_login_status(driver):
    logger.info('检查登录状态')
    login_status = False
    # 先清空所有的cookies
    driver.get("https://www.jd.com")
    driver.delete_all_cookies()
    sleep(1)
    logger.info('加载最新存储的cookies')
    add_cookies(driver)
    sleep(1)
    url='https://order.jd.com/center/list.action'
    driver.get(url)
    get_screen_shot(driver,'检测是否登录成功.png')
    sleep(1)
    current_a=driver.current_url
    sleep(1)
    print(current_a)
    if str(current_a)==url:
        login_status=True
        return login_status
    else:
        return login_status
    # get_logger().info('打开浏览器')

#切换句柄
def change_handle(driver):
    handles=driver.window_handles
    curent_handle=driver.current_window_handle
    for handle in handles:
        if handle!=curent_handle:
            driver.close()
            driver.switch_to.window(handle)

if __name__ == '__main__':
    # driver=browser()
    # driver.get('https://www.jd.com')
    # get_screen_shot(driver,'jd.png')

    # print(get_csv_date(r'E:\python练习库\jd_practices全流程\Website\test_data\smelp.csv',0))
    print(os.path.dirname(os.path.dirname(os.getcwd())))
