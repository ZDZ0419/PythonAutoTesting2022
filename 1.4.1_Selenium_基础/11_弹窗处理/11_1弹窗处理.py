from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# alert弹窗
driver=webdriver.Chrome()
path1='C:/Users/Administrator/Desktop/selenium%E7%BB%83%E4%B9%A0%E6%9D%90%E6%96%99/%E5%BC%B9%E7%AA%97/alert.html'
driver.get(path1)
#定位需要点击的元素并点击
driver.find_element(By.ID,'anjing').click()
#判断弹窗是否出现
WebDriverWait(driver,3).until(EC.alert_is_present())
# 切入alert弹窗
a = driver.switch_to_alert()
sleep(3)
a.accept()
sleep(3)

#confirm弹窗
# driver=webdriver.Chrome()
path2='file:///C:/Users/Administrator/Desktop/selenium%E7%BB%83%E4%B9%A0%E6%9D%90%E6%96%99/%E5%BC%B9%E7%AA%97/confirm.html'
driver.get(path2)
#定位需要点击的元素并点击
driver.find_element(By.ID,'anjing').click()
#切入confirm弹窗
b=driver.switch_to.alert
sleep(2)
b.accept()
sleep(2)
b.accept()
#定位需要点击的元素并点击
driver.find_element(By.ID,'anjing').click()
#切入confirm弹窗
b=driver.switch_to.alert
sleep(2)
b.dismiss()
sleep(2)
b.accept()

#prompt弹窗
path3='C:/Users/Administrator/Desktop/selenium%E7%BB%83%E4%B9%A0%E6%9D%90%E6%96%99/%E5%BC%B9%E7%AA%97/prompt.html'
driver.get(path3)
#定位需要点击的元素并点击
driver.find_element(By.XPATH,"//input[@value='点我，点我有惊喜']").click()
#切入prompt弹窗
c=driver.switch_to.alert
sleep(2)
c.send_keys('abc')  #传值失败，不能正常传入
sleep(2)
c.accept()
sleep(3)
driver.refresh()
sleep(2)
#定位需要点击的元素并点击
driver.find_element(By.XPATH,"//input[@value='点我，点我有惊喜']").click()
#切入prompt弹窗
c=driver.switch_to_alert()
sleep(2)
c.dismiss()
driver.quit()

