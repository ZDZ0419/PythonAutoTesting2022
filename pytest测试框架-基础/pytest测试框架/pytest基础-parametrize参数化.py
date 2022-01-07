import pytest
# import sys
#可以是string、list、tuple
#可用于组合查询
# @pytest.mark.parametrize("a,b",[('5+2',7),('6+7',11),('2+2',4)])
# def test_eval(a,b):
#     #eval 将字符串当成有效的表达式求值，并返回结果
#     assert eval(a) == b

#参数组合
# @pytest.mark.parametrize("a",[2,4])
# @pytest.mark.parametrize("b",[4,5,6])
# def test_eval(a,b):
#     print('组合后的数据x:'+ str(a) +','+ 'y:'+ str(b))

#方法名作为参数
# test_data=['Tom','jerry']
# @pytest.fixture(scope="module")
# def login_r(request):
#     #接收并传入的参数
#     user=request.param
#     print(format("打开登录页面，用户名：" + user))
#     return user
#
# #indirect=True 可以把传过来的参数当函数来执行
# @pytest.mark.parametrize("login_r",test_data,indirect=True)
# def test_login(login_r):
#     a = login_r
#     print(format("测试用例中的login的返回值：" + a ))
#     assert a != ""

 #参数化
class TestData:
    @pytest.mark.parametrize("a,b",[(5,7),(8,11),(6,4)])
    def test_eval(self,a,b):
        print(a+b)

