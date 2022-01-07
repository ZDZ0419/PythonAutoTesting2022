'''
邮箱协议：smtp协议/imap协议/pop协议
'''
import smtplib #smtp协议包
from email.mime.text import MIMEText #用于构建邮箱内容

#设置邮箱参数
msg_from='zzdd666666@126.com' #发件人
passwd='JMGMPRIMZEDXMGOP'   #客户端授权码
msg_to='943631615@qq.com'   #收件人

#构造邮件内容
subject='001_测试邮件' #邮件标题内容
content='这是一个测试邮件' #邮件正文内容
msg=MIMEText(content)  #创建邮件内容对象
msg['Subject']=subject   #Subject/From/To均为固定写法
msg['From']=msg_from
msg['To']=msg_to

#发送邮件
#smtpObj=smtplib.SMTP_SSL('发件人的邮箱服务器地址',地址的端口号)
#smtpObj.login(发件人邮箱地址,密码(邮箱的授权码))
#smtpObj.sendmail(发件人地址,收件人地址,str(构造的邮件内容))
smtpObj=smtplib.SMTP_SSL('smtp.126.com',465)  #smtp对象
smtpObj.login(msg_from,passwd)   #登录
smtpObj.sendmail(msg_from,msg_to,str(msg)) #发送
print('邮件发送成功！！！')
smtpObj.quit()
