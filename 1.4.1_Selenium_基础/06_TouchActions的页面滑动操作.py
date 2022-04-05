"""
实践：
打开百度，输入“selenium测试”，搜索，并滑动至当前页面最下方
"""
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By

class TestTouchaction:
    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def testscoll(self):
        self.driver.get('http://www.baidu.com')
        el1 = self.driver.find_element(By.ID,'kw')
        el2 = self.driver.find_element(By.ID,'su')
        el1.send_keys('selenium测试')
        action = TouchActions(self.driver)
        action.tap(el2).perform()
        action.scroll_from_element(el1,0,10000).perform()
        sleep(5)

