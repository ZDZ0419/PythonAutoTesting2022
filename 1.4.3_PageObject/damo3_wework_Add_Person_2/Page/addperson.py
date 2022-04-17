from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class AddPerson:

    def __init__(self, driver: WebDriver):
        # 复用浏览器
        self._driver = driver

    def add_person_page(self):
        # 定位并输入信息，点击保存
        sleep(5)
        self._driver.find_element(By.ID, 'username').send_keys('张华天')
        self._driver.find_element(By.ID, 'memberAdd_acctid').send_keys('10001')
        self._driver.find_element(By.ID, 'memberAdd_phone').send_keys('13213226607')
        self._driver.find_element(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click()
        # return True

    def get_person(self):
        sleep(5)
        elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        list = []
        for element in elements:
            list.append(element.get_attribute('title'))
        return list
