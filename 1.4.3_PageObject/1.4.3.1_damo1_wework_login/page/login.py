from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page.register import Register

class Login:
    #传入driver,使初始化浏览器的代码可以复用，
    # ：WebDriver 可以增加输入时的提示信息，将driver的方法带过来，不加也不影响
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def scanf_login(self):
        pass

    def goto_register(self):
        # click register
        # .login_registerBar_link
        # 快速定位到指定元素位置，并显示元素所在区域
        ele = self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').location_once_scrolled_into_view
        self._driver.find_element(By.CSS_SELECTOR, '.login_registerBar_link').click()
        return Register(self._driver)