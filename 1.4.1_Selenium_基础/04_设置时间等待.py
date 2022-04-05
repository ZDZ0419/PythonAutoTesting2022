# # 1. 隐式等待：
# from selenium import webdriver
# from time import sleep,ctime
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.baidu.com")


# #【隐式等待时间设置3s】
# driver.implicitly_wait(3)
#
# # 检测元素是否存在
# try:
#     print(ctime())
#     driver.find_element_by_css_selector("#kw2").send_keys("python")
#     driver.find_element(By.CSS_SELECTOR,"#su").click()
# except NoSuchElementException as msg:
#     print(msg)
# finally:
#     print(ctime())
# sleep(3)
# driver.quit()

# 2.显示等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait   #显示等待
from selenium.webdriver.support import  expected_conditions as EC
from time import sleep,ctime

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element(By.CSS_SELECTOR,"#kw").send_keys("周华强")

#显示等待，判断搜索按钮是否存在
element=WebDriverWait(driver,4,0.5).until(EC.presence_of_element_located((By.ID,"su")))
print(ctime())
element.click()
sleep(2)
#driver.quit()

# 3.强制等待  sleep()