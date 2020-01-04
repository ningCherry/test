import smtplib
from email.mime.text import MIMEText
from email.header import Header

def test_result(first,second):
    if first==second:
        result=True
    else:
        result=False
    return result

def send_mail(content):
    smtpserver='smtp.163.com'

    user='15801801915'
    password=''

    sender='15801801915@163.com'
    recives=['834121195@qq.com', '']

    msg=MIMEText(content,'html','utf-8')
    msg['Subject']=Header('接口测试结果统计','utf-8')
    msg['From']=sender
    msg['To']=','.join(recives)

    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user,password)
    smtp.sendmail(sender,recives,msg.as_string())
    smtp.quit()

def send_main(pass_list,fail_list):
    pass_num=len(pass_list)
    fail_num=len(fail_list)
    total_count=pass_num+fail_num

    # pass_lv='{}%'.format(float((pass_num/total_count)*100))
    # fail_lv='{}%'.format(float((fail_num/total_count)*100))
    pass_lv='%.2f'%(float((pass_num/total_count)*100))+'%'
    fail_lv='%.2f'%(float((fail_num/total_count)*100))+'%'

    content='测试结果为：总共执行了{}条，成功{}条，失败{}条。成功率为{}，失败率为{}'.format(total_count,pass_num,fail_num,pass_lv,fail_lv)
    send_mail(content)


if __name__ == '__main__':
    # def a():
    #     list1=[1,2,3,4,5]
    #     list2=[7,8,9,0]
    #     return list1,list2
    # print(a()[1])

    pass_lv = '%.2f'%(((2 / 3) * 100))+'%'
    print(pass_lv)
