# 工具类，包括截图、最新报告查找、邮件发送
from selenium import webdriver
import os
import time
# 最新报告查找、邮件发送
import smtplib                           # 发送邮件模块
from email.mime.text import MIMEText    # 定义邮件内容
from email.header import Header         # 定义邮件标题

# 封装 截图 方法
def insert_img(driver,filname):
    # 获取截图方法所在的当前路径model
    func_path = os.path.dirname(__file__)
    print(func_path)
    # 获取截图方法所在的上层目录test_case
    base_dir = os.path.dirname(func_path)
    print(base_dir)
    # 将获取的路径转为字符串形式
    base_dir = str(base_dir)
    # 将字符串中的\\转换为/，因\\在字符串中表示转义
    base_dir = base_dir.replace("\\", "/")
    print(base_dir)
    # 对路径进行拆分，以获取AuToTest_projectA层级的路径，拆分后结果为列表
    base = base_dir.split("/website")[0]
    print(base)
    # 定义截图自动保存路径
    filepath = base+'/website/test_report/screenshot/' + time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) + "-" + filname
    driver.get_screenshot_as_file(filepath)

#  封装 查找最新报告 方法【report_dir在run_test.py中指定】
def latest_report(report_dir):
    # os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
    lists = os.listdir(report_dir)
    print(lists)
    # 按时间顺序对该目录文件夹下面的文件进行排序
    # lambda 是匿名函数，冒号左边的是入口函数，冒号右边的是函数体
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    print("The new report is "+lists[-2])
    # 输出最新报告的路径
    file = os.path.join(report_dir, lists[-2])
    print(file)
    return file

#  封装 邮件发送 方法
def send_mail(latest_report):

    # 以二进制方式读取测试报告，并将文件内容赋给mail_content
    f = open(latest_report, 'rb')   # 二进制方式读取测试报告
    mail_content = f.read()         # 读取结果赋给mail_content
    f.close()                       # 关闭，操作文件的最后一步，必须有

    # 定义邮件服务器地址
    smtpserver = 'smtp.163.com'

    # 发送邮箱的用户名密码(用户授权码)
    user = 'z843395332@163.com'  # 发送方用户名
    password = 'JLMRPOLERKOWTARU'   # 邮箱的用户授权码

    # 发送和接收邮箱
    sender = 'z843395332@163.com'   # 发送人邮箱地址
    receives = ['943631615@qq.com', '843395332@qq.com']  # 接收人邮箱地址

    # 发送邮件的主题和内容
        # 邮件的标题
    subject = 'Web Selenium 自动化测试报告'
        # HTML邮件正文
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件标题
    msg['From'] = sender                       # 发送人
    msg['To'] = ','.join(receives)             # 接收人

    smtp = smtplib.SMTP_SSL(smtpserver, 465)

    # HELO 向服务器标识用户身份
    smtp.helo(smtpserver)
    # 服务器返回结果确认
    smtp.ehlo(smtpserver)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    print("Start send Email...")
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()
    print("Send Email end!")

if __name__ == '__main__':
    # 单元测试-截图保存功能
    driver = webdriver.Chrome()
    driver.get("http://www.sogou.com")
    insert_img(driver,"A.png")
    driver.quit()

    # 单元测试-最新报告路径获取
    # report_dir = '../../test_report'
    # latest_report(report_dir)

    # 单元测试-获取最新测试报告，并通过邮件发送报告
    # latest_report = latest_report(report_dir)
    # send_mail(latest_report)