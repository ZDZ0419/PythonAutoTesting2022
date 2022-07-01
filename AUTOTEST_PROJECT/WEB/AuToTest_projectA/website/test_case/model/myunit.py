import unittest
from driver import *

# 封装用例执行前、执行后的操作
class StartEnd(unittest.TestCase):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()