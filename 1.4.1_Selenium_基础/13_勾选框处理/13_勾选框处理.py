from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
path1='C:/Users/Administrator/Desktop/selenium%E7%BB%83%E4%B9%A0%E6%9D%90%E6%96%99/%E5%8B%BE%E9%80%89%E6%A1%86/%E5%8B%BE%E9%80%89%E6%A1%86.html'
driver.get(path1)

# 全选
a=driver.find_elements(By.NAME,'vehicle')
for i in a:
    i.click()
a[0].click()
a[2].click()
# 取消选中
driver.find_element(By.CSS_SELECTOR,'[value="Bike"]').click()
driver.quit()

