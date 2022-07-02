from base_page import *
from selenium.webdriver.common.by import By

# 创建登录页面类
class LoginPage(Page):
    # url='/'
    url = '/List.aspx?cid=390'

    # 创建相关登录元素定位器
    submit_loc = (By.LINK_TEXT, "登录/注册")
    link_loc = (By.XPATH, "//div[@class='mode mt-10 text-c']/a[@class='checked']")
    username_loc = (By.NAME, "loginStr")
    password_loc = (By.NAME, "pwd")
    submit_loc_1 = (By.CSS_SELECTOR, ".btn.radius.size-L.btn-danger")
    # 断言登录是否成功定位器
    # assert_loc = (By.CSS_SELECTOR, "div.user.pos-r>span.text-overflow.mr-5")

    # 对登录页面的元素类进行封装
    def type_submit_A(self):
        self.find_element(*self.submit_loc).click()

    def type_link(self):
        self.find_element(*self.link_loc).click()

    def type_username(self, username):
        self.find_element(*self.username_loc).click()
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).click()
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit_B(self):
        self.find_element(*self.submit_loc_1).click()

    # 封装登录操作-功能模块的封装
    def LogIn_action(self, username, password):
        self.open()
        self.type_submit_A()
        self.type_link()
        self.type_username(username)
        self.type_password(password)
        self.type_submit_B()


    # 登录断言操作--定位器
    loginPass_loc=(By.CSS_SELECTOR,"div.user.pos-r>span.text-overflow.mr-5")
    # loginFalse1_loc=(By.CSS_SELECTOR,".msgText.error")
    loginFalse2_loc=(By.CSS_SELECTOR,"#loginStr-error")

    #对断言的元素类进行封装
    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text

    # def type_loginFlase1_hint(self):
    #     return self.find_element(*self.loginFalse1_loc).text

    def type_loginFlase2_hint(self):
        return self.find_element(*self.loginFalse2_loc).text
