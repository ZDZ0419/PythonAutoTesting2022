"""
实践一：
访问百度，输入“selinium测试”，搜索，页面滚动到最下方，
点击“下一页”，停留5s，页面滚动到最下方，关闭浏览器。
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestJs():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
    @pytest.mark.skip
    def test_search(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("selenium测试")
        #self.driver.find_element(By.CSS_SELECTOR, "su").click()
        element_search = self.driver.execute_script("return document.getElementById('su')")
        element_search.click()
        sleep(5)

        self.driver.execute_script("document.documentElement.scrollTop = 10000")
        sleep(6)
        element_page = self.driver.find_element(By.XPATH, "//*[@id='page']//a[last()]")
        element_page.click()
        sleep(10)
        self.driver.execute_script("document.documentElement.scrollTop = 10000")
        sleep(5)
        #打印页面title，及性能数据
        for code in [
            "return document.title","return JSON.stringify(performance.timing)"
        ]:
            print(self.driver.execute_script(code))



