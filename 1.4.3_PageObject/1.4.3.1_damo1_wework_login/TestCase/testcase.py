import pytest

from index import Index


class TestRegiter:

    def setup(self):
        self.index = Index()


    def testRegiter1(self):
        # 方法1：首页直接点击“立即注册”
        self.index.goto_register().register()

    def testRegiter2(self):
        # 方法2：首页点击登录，进入登录页面再点击“立即注册”
        self.index.goto_login().goto_register().register()

if __name__ == '__main__':
    pytest.main()