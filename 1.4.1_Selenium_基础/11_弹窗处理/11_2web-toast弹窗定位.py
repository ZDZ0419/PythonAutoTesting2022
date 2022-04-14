from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
path1='file:///C:/Users/Administrator/Desktop/selenium%E7%BB%83%E4%B9%A0%E6%9D%90%E6%96%99/toast%E5%BC%B9%E7%AA%97%E5%AE%9A%E4%BD%8D.html'
driver.get(path1)

driver.find_element(By.ID,'anjing').click()

ele=(By.XPATH,'/html/body/div')
WebDriverWait(driver,3).until(EC.presence_of_element_located(ele))
elem=driver.find_element(By.XPATH,'/html/body/div').text
print(elem)