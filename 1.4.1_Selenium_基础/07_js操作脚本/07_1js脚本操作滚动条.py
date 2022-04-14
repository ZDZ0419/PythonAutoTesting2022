'''场景：
打开https://blog.csdn.net/guiyin1150/article/details/108467577
定位元素：评论按钮
可视区域显示评论按钮
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
path1 = 'https://www.baidu.com'
driver.get(path1)
driver.set_window_size(960, 550)

driver.find_element(By.ID,'kw').send_keys('selenium使用js实现任意位置的滚动')
driver.find_element(By.ID,'su').click()
sleep(3)

# js =
driver.execute_script("scrollTo(500,500)")
sleep(5)

# element = driver.find_element(By.CSS_SELECTOR, '.n')
# js = "arguments[0].scrollIntoView()"
# driver.execute_script(js, element)
# sleep(5)
# element.click()
# sleep(5)
# element = driver.find_element(By.CSS_SELECTOR, '.n')
# js = "arguments[0].scrollIntoView()"
# driver.execute_script(js, element)
# sleep(10)
#
# driver.quit()
