from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
#driver=webdriver.Firefox()
#driver=webdriver.Ie()
driver.get("http://www.51zxw.net")
print(driver.title + "_1")
sleep(3)

driver.get("http://www.baidu.com")
print(driver.title + "_2")
sleep(3)

driver.quit()

