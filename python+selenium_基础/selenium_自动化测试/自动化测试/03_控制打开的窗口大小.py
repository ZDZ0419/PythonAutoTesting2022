from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
#driver=webdriver.Firefox()
#driver=webdriver.Ie()
driver.get("http://www.51zxw.net")    # 访问主页面
driver.maximize_window()                # 窗口最大化
sleep(3)                                # 停留3秒

driver.get("https://www.51zxw.net/List.aspx?cid=35")   # 访问二级页面
driver.set_window_size(300,500)                            #  自定义页面窗口大小
driver.refresh()                                           #  刷新当前页面
sleep(3)

driver.back()                                              # 返回父页面
sleep(3)

driver.forward()                                           #  返回子页面
sleep(5)
driver.quit()