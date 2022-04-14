from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver=webdriver.Chrome()
driver.get('http://www.baidu.com')

driver.find_element(By.ID,'kw').clear()
driver.find_element(By.ID,'kw').send_keys('测试-安静')
driver.find_element(By.ID,'su').click()
handle=driver.current_window_handle #获取当前窗口的句柄
print('获取窗口1的句柄:',handle)
sleep(20)
handle_all=driver.window_handles  #获取所有窗口句柄
print('获取所有窗口句柄2:',handle_all)
driver.find_element(By.XPATH,"//*[contains(text(),' - 博客园')]").click()
# driver.find_element_by_xpath("//*[contains(text(),' - 博客园')]").click()

#判断是否有新窗口出现【传入的是句柄列表】
WebDriverWait(driver,10).until(EC.new_window_is_opened(handle_all))

handle_all=driver.window_handles  #获取所有窗口句柄
print('获取所有窗口句柄2:',handle_all)
handle1=driver.current_window_handle #获取当前窗口句柄
print('获取当前窗口句柄：',handle1)
sleep(5)
driver.switch_to.window(handle_all[0]) #切到第一个窗口
handle3=driver.current_window_handle
print('获取窗口1的句柄：',handle3)
sleep(5)
driver.switch_to.window(handle_all[-1]) #切到最新窗口
handle2=driver.current_window_handle #获取当前窗口句柄
print('获取窗口2的句柄：',handle2)
sleep(5)
driver.quit()


