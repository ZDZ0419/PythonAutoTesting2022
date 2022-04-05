from selenium import webdriver
from time import sleep
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(3)

dengl_1=driver.find_element(By.LINK_TEXT,"登录").click()
sleep(5)
#dengl_2=driver.find_element(By.CSS_SELECTOR,".tang-pass-footerBarULogin.pass-link").click()
dengl_2=driver.find_element(By.PARTIAL_LINK_TEXT,"用户名登录").click()
#dengl_2=driver.find_element(By.ID,"TANGRAM__PSP_11__footerULoginBtn" ).click()
sleep(2)
dengl_3=driver.find_element(By.ID,"TANGRAM__PSP_11__userName").send_keys("crqok")
sleep(3)
#driver.switch_to.frame()
