from LoginPage import *
from selenium import webdriver

driver=webdriver.Chrome()

username='Test0123456'
password='123456'

#调用方法
test_user_Login(driver,username,password)
sleep(3)
driver.quit()
print(">>>>>>>>>>>>>>>>>>>>测试结束！！！！<<<<<<<<<<<<<<<<<<<<<<<<<")


