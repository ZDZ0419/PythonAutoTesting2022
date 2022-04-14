from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Chrome()
path1='C:/Users/Administrator/Desktop/selenium%E7%BB%83%E4%B9%A0%E6%9D%90%E6%96%99/%E4%B8%8B%E6%8B%89%E6%A1%86/%E4%B8%8B%E6%8B%89%E6%A1%86.html'
driver.get(path1)
#判断select元素是否出现
WebDriverWait(driver,3).until(EC.visibility_of_element_located((By.NAME,'anjing')))
#定位select元素
select = driver.find_element(By.NAME,'anjing')
#实例化并使用"索引"定位下拉框值
Select(select).select_by_index(2)
sleep(2)
#实例化并使用"value"值定位下拉框值
Select(select).select_by_value('attention')
sleep(2)
#实例化并使用"文字"信息定位下拉框值
Select(select).select_by_visible_text('今天学习了吗？')
sleep(2)
a=driver.find_element(By.XPATH,"//*[@value='study']")
WebDriverWait(driver,3).until(EC.element_to_be_selected(a))
sleep(2)
driver.quit()
