from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_Page:
    # 定义类变量
    _driver = None
    _base_url = ""

    # 初始化方法封装
    def __init__(self, driver: WebDriver = None):
        if driver is None:
            # 浏览器复用并访问企业微信
            options = Options()
            options.debugger_address = '127.0.0.1:8888'
            self._driver = webdriver.Chrome(options=options)
        else:
            self._driver = driver

        # 对url进行封装
        if self._base_url != "":
            self._driver.get(self._base_url)

    # 对find_element方法进行封装
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    # 对find_elements方法进行封装
    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    # 显示等待方法封装,等待元素出现并判断元素是否可被点击
    def wait_f(self, locator, time=10):
        return WebDriverWait(self._driver, time).until(EC.element_to_be_clickable(locator))
