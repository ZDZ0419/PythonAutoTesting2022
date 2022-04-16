'''
1.使用浏览器复用先进行登录企业微信
2.点击添加成员功能
3.添加成员页面输入信息，点击保存
'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from addperson import Addperson


class Main:

    def __init__(self):
        options = Options()
        options.debugger_address = '127.0.0.1:8012'
        self._driver = webdriver.Chrome(options=options)
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # self._driver.maximize_window()

    def goto_AddPersonPage(self):

        # 定位添加成员，其是父元素的第一个子元素【.index_service_cnt_itemWrap:nth-child(1)】
        sleep(4)
        self._driver.find_element(By.CSS_SELECTOR,'.index_service_cnt_itemWrap:nth-child(1)').click()
        return Addperson(self._driver)