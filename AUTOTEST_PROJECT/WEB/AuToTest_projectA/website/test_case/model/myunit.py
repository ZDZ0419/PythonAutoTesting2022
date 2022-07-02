import unittest
from driver import *

# 封装用例执行前、执行后的操作
class StartEnd(unittest.TestCase):

    # 用例执行前：打开浏览器-隐式等待-窗口最大化
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    # 用例执行后：退出浏览器
    def tearDown(self):
        self.driver.quit()