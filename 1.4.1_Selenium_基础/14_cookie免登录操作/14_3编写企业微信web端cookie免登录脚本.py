'''
Page.访问企业微信web端首页
2.手动登录，获取cookies
3.将cookies保存到shelve中
4.从shevle中取cookie
5.将coolies加入到企业微信web端首页
6.刷新/再次访问企业微信web端首页
7.点击“通讯录”标签
8.等 5s后自行退出浏览器
9.关闭shelve
'''
import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Login():
    def setup(self):
        options=Options()
        options.debugger_address='127.0.0.Page:8012'
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(925,654)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        # self.driver.refresh()
        db = shelve.open("cookies")
        # db['cookie']=self.driver.get_cookies()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        cookies = db['cookie']
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.implicitly_wait(5)
        a=(By.ID, 'menu_contacts')
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(a))
        self.driver.find_element(By.ID,'menu_contacts').click()
        sleep(5)
        db.close()
if __name__ == '__main__':
    pytesy.main()
