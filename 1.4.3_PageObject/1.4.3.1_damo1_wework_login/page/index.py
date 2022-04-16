from selenium import webdriver
from selenium.webdriver.common.by import By

from page.login import Login
from page.register import Register

class Index:

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.maximize_window()
        self._driver.get('https://work.weixin.qq.com/')

    def goto_login(self):
        # click_login
        # .index_top_operation_loginBtn
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        return Login(self._driver)

    def goto_register(self):
        # click_register
        self._driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return Register(self._driver)