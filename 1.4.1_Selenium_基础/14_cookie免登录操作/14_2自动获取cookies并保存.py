import shelve  #小型存储空间，类似于数据库
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

class TestDamo():
    def setup(self):
        options = Options()
        options.debugger_address = '127.0.0.Page:8888'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_damo(self):

        # 浏览器复用：在已登录的状态下保存cookies信息
        db = shelve.open("cookies")
        #cookie获取完成后，需将此行注销，并取消浏览器复用
        # db['cookie'] = self.driver.get_cookies()

        # # 访问企业微信首页
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        cookies = db['cookie']
        # 获取的cookies存在有效期
        for cookie in cookies:
            #如果获取到的cookies包含“expiry”,则删除其key和value值，避免其为小数时报错
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        #刷新页面
        self.driver.refresh()
        sleep(3)
        #点击“通讯录”标签
        self.driver.find_element(By.ID, 'menu_contacts').click()
        sleep(5)
        db.close()

if __name__ == '__main__':
    pytest.main()