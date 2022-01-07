import pytest

@pytest.fixture(scope='function')
# 也可将@pytest.fixture(scope=function)及需要执行的公共操作放到conftest.py中
# 会自动在测试用例同级的文件中找conftest.py文件中的login方法
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
