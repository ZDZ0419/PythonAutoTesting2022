import unittest
from model import function, myunit
from page_Object.login_page import *
from time import *

class Login_Test(myunit.StartEnd):
    def test_login1(self):
        '''账号密码正确'''
        print('test1_start')
        po = LoginPage(self.driver)
        po.LogIn_action('Test0123456', '123456')
        sleep(2)

        self.assertEqual(po.type_loginPass_hint(), 'Test0123456')
        function.insert_img(self.driver, '账号密码正确login_1.jpg')
        print('test1_END')

    def test_login2(self):
        '''账号正确，密码不正确'''
        print('test2_start')
        po = LoginPage(self.driver)
        po.LogIn_action('Test0123456', '1123456')
        sleep(2)

        #获取网页源码
        html = self.driver.page_source
        #断言：内容是否在网页源码中存在
        self.assertIn("登录失败，请检查登录信息是否有误", html)
        # self.assertEqual(po.type_loginFlase1_hint(),'登录失败，请检查登录信息是否有误')
        function.insert_img(self.driver, '账号正确密码不正确login_2.jpg')
        print('test2_END')

    def test_login3(self):
        '''账号密码为空'''
        print('test3_start')
        po = LoginPage(self.driver)
        po.LogIn_action('', '')
        sleep(2)

        self.assertEqual(po.type_loginFlase2_hint(), '请输入账号信息')
        function.insert_img(self.driver, '账号密码为空login_3.jpg')
        print('test3_END')


if __name__ == '__main__':
    unittest.main()