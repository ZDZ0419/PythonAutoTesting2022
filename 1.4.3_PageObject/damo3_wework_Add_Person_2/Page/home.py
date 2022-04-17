from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from addperson import AddPerson


class Home:

    def __init__(self):
        # 浏览器复用并访问企业微信
        options = Options()
        options.debugger_address = '127.0.0.1:8888'
        self._driver = webdriver.Chrome(options=options)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')

    def HomePage(self):
        # 点击通讯录，点击添加成员
        sleep(4)
        self._driver.find_element(By.ID, 'menu_contacts').click()
        sleep(3)
        self._driver.find_element(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) .js_add_member').click()
        return AddPerson(self._driver)