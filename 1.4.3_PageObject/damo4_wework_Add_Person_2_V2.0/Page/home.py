
from selenium.webdriver.common.by import By

from BasePage import Base_Page
from addperson import AddPerson

class Home(Base_Page):

    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def HomePage(self):
        # 等待“通讯录”元素出现
        self.wait_f((By.ID, 'menu_contacts'))
        # 点击通讯录
        self.find(By.ID, 'menu_contacts').click()
        # 等待“添加成员”元素出现
        self.wait_f((By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) .js_add_member'))
        # 点击添加成员
        self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1) .js_add_member').click()
        return AddPerson(self._driver)