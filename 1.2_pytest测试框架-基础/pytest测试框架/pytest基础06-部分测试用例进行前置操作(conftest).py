import pytest

#@pytest.fixture(scope=function)
#让部分测试用例执行登录操作，给需要执行登录的用例传入登录的方法名,范围默认是方法
#scope也可指定为class/moudle/package...,指定后其作用域改变为类下、模块下、包下
#也可将@pytest.fixture(scope=function)及需要执行的公共操作放到conftest.py中，
# conftest文件为pytest特有的，文件名不可变更，同级中的conftest.py文件在此处使用
@pytest.fixture(scope="function")    #为function时，可不写scope信息
def login():
    print('这是一个登录操作')

def test_case1(login):
    print('开始执行 test_case1 方法  要登录')
    pass

def test_case2():
    print('开始执行 test_case2 方法  不要登录')
    pass

def test_case3(login):
    print('开始执行 test_case3 方法  要登录')
    pass

if __name__ == '__main__':
    pytest.main()
    # pytest.main("-v -x Testdemo")   #带参数调用方式1
    # pytest.main(['-v','-x','Testdemo'])  #带参数调用方式2
