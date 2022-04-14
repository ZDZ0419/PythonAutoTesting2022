
'''
用于浏览器的兼容性测试
在执行时，需使用pytest命令行方式，且需要先指定浏览器
'''

from selenium import webdriver
import os
class Base():
    def setup(self):
        browser=os.getenv('browser')
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'IE':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


