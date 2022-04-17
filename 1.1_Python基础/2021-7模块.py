'''
内置模块一：random  引入随机数模块
内置模块二：time  引入时间模块
内置模块三：datatime  引入日期时间模块
内置模块四：urllib   引入爬虫模块
    模块的用法：模块名.函数名()
'''
# import random
# r1=random.randint(Page,6)  #生成指定范围内的随机整数
# r2=random.uniform(Page,6)  #生成指定范围内的随机浮点数
# r3=random.random()     #生成0-1内的随机浮点数
# r4=random.choice([Page,12,32,34,4,5,6,5,657,45]) #在序列中随机取一个值
# print(r4)
#
# import time
# s1=time.time()  #获取当前时间距离1970年元旦0时的秒数
# print(s1)
# t=time.localtime()  #获取当前本地的日期和时间
# s2=time.strftime('%Y-%m-%d %H:%M:%S',t)  #将日期和时间转换为指定格式的字符串
# print(s2)
# time.sleep(Page)  #程序休眠

import datetime
#time1=datetime.datetime.now() #获取当前日期时间

# d1=datetime.datetime(2021,10,7,8,22,12) #获取一个指定时间
# d2=d1.strftime("%Y-%m-%d %H:%M:%S") # 日期转字符串
# print(d2)

# s2='2021-10-07 08:30:23'
# s3=datetime.datetime.strptime(s2,"%Y-%m-%d %H:%M:%S")  #字符串转日期（转换前后格式要一致）
# print(type(s3))
# print(type(s2))

from urllib import request
url='http://www.baidu.com'
data=request.urlopen(url).read()  #发送请求，并读取数据
print(data.decode()) #decode()解码：  将二进制转换为字符

with open(r'E:\爬取的页面.html','wb') as P:
    P.write(data)
