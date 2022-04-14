from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


class TestDamo():
    def setup(self):
        # options = Options()
        # options.debugger_address = '127.0.0.1:8888'
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_damo(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False,
             'value': 'true'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688854631364577'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970326538975885'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688854631364577'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '34120057432836567'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': '988bg2AW5qPGWVeCVutb6LxkjZn_l_S_fDGqR-RJoLbiNYyLbSFY2ApDXyhcpcSX'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1680791347, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a3223064'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'DrMZNyhQFDfUri1fqIe5feF1xMZspcznzsKWX3FPTBXs4ZFrNyrI6K3-33_KAcAePc_KJJfSXU0v1UrCzmK2M-O6GGdH7fkQgs9PTpvhnvic-iti3eq0_a3WO9_gpLUz8GWAGL_r_ocqeQr_xzJ_2rVeWipP1fZrE1bWHSQdgEc3QPbQ7_QiJtpGIaHnT3Z_7aOpM4FHiGPg_Q67ZBIlFJoPJ0j4oOh6e8jcteApNf2ZFGg8rWn8H_V_PhG531pd4mTFkA8t4agyJVEqx3pvEA'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1652525475, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]
        # 在已登录的状态下打印cookies信息
        # print(self.driver.get_cookies())
        # 访问企业微信首页
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # 获取的cookies存在有效期
        for cookie in cookies:
            #如果获取到的cookies包含“expiry”,则删除其key和value值，避免其为小数时报错
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        #刷新页面
        self.driver.refresh()
        sleep(3)
        #点击“通讯录”标签
        self.driver.find_element(By.ID, 'menu_contacts').click()
        sleep(5)

if __name__ == '__main__':
    pytest.main()
