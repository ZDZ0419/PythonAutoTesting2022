from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://work.weixin.qq.com/')

driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
sleep(3)

driver.find_element(By.ID,'corp_name').send_keys('Hello111')
sleep(3)
driver.find_element(By.CSS_SELECTOR,'.qui_btn.ww_btn.ww_btn_Big.ww_btn_Block.ww_btn_Dropdown.js_corp_industry_bt').click()
sleep(3)
driver.execute_script(document.getElementsByClassName("qui_dropdownMenu ww_dropdownMenu js_corp_industry_ul register_corp_industry_ul").removeAttribute('display: block;'))
driver.find_element(By.XPATH,'//*[@data-value="1001"]').click()
sleep(10)