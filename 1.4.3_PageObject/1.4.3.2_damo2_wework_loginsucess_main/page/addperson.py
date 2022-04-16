from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Addperson:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def AddpersionPage(self):
        sleep(5)
        self._driver.find_element(By.ID, 'username').send_keys('张华天')
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys('10000001')
        self._driver.find_element(By.ID, 'memberAdd_biz_mail').send_keys('100000')
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys('13213226607')
        sleep(3)
        ele = self._driver.find_element(By.NAME, 'sendInvite').location_once_scrolled_into_view
        self._driver.find_element(By.NAME, 'sendInvite').click()
        sleep(3)
        self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        # return True

    def assert_result(self):
        sleep(3)
        eles = self._driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        list = []
        for ele in eles:
            list.append(ele.get_attribute("title"))
        return list

