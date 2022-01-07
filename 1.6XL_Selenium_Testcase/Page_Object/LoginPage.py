from  Base_Page import *
from selenium.webdriver.common.by import By
import unittest
class LoginPage(Page):
    url='/'

    #创建元素定位器
    submit_loc=(By.LINK_TEXT,"登录/注册")
    link_loc=(By.XPATH,"//div[@class='mode mt-10 text-c']/a[@class='checked']")
    username_loc=(By.NAME,"loginStr")
    password_loc=(By.NAME,"pwd")
    submit_loc_1=(By.CSS_SELECTOR,".btn.radius.size-L.btn-danger")
    assert_loc = (By.CSS_SELECTOR, "div.user.pos-r>span.text-overflow.mr-5")


    # 对元素类进行封装

    def type_submit_A(self):
        self.find_element(*self.submit_loc).click()

    def type_link(self):
        self.find_element(*self.link_loc).click()

    def type_username(self,username):
        self.find_element(*self.username_loc).click()
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).click()
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit_B(self):
        self.find_element(*self.submit_loc_1).click()


    def type_assert(self,username):

        try:
            strs = self.find_element(*self.assert_loc).text
            if strs==username:
                print("恭喜您，登录成功")

        except:
            print("对不起，此次登录失败，请检查账号密码是否正确!!!")

# 对登录场景进行封装
def test_user_Login(driver,username,password):
    loginpage=LoginPage(driver)
    loginpage.open()

    loginpage.type_submit_A()
    loginpage.type_link()
    loginpage.type_username(username)
    loginpage.type_password(password)
    loginpage.type_submit_B()
    sleep(3)
    loginpage.type_assert(username)