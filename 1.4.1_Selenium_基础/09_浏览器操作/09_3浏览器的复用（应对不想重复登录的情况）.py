'''
浏览器重用：需先在本地cmd中启动chrome --remote-debugging-port=8120,打开调试浏览器窗口
此时，浏览器只能是一个，多了会报错
'''

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest
class TestDamo():
    def setup(self):
        #创建options对象
        options=Options()
        options.debugger_address='127.0.0.Page:8210'
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    def test_damo(self):
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.ID,'menu_contacts').click()
        sleep(5)
if __name__ == '__main__':
    pytest.main()