from time import sleep

from selenium.webdriver.common.by import By

from BasePage import Base_Page

class AddPerson(Base_Page):

    def add_person_page(self):
        # 定位并输入信息，点击保存
        self.wait_f((By.ID, 'username'))
        self.find(By.ID, 'username').send_keys('张华天')
        self.find(By.ID, 'memberAdd_acctid').send_keys('10001')
        self.find(By.ID, 'memberAdd_phone').send_keys('13213226607')
        self.find(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click()

    def get_person(self):

        # 等待勾选框元素出现，并且可被点击，以此判断文本加载成功
        self.wait_f((By.CSS_SELECTOR, '.ww_checkbox'))
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        # elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        list = []
        for element in elements:
            list.append(element.get_attribute('title'))
        return list
