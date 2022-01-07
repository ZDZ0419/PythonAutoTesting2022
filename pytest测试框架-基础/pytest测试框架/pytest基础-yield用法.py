import pytest

@pytest.fixture(scope="module")    #yield 使用时其scope为module,在模块之前与之后执行
def open():
    print('打开浏览器')
    yield   #可对后置操作进行定义，所在方法中yield后的操作将作为模块程序执行最后的后置操作进行执行

    print('执行teardown操作')
    print('最后关闭浏览器')

def test_case1(open):
    print('开始执行 test_case1 方法  要登录')
    pass

def test_case2(open):
    print('开始执行 test_case2 方法  不要登录')
    pass

def test_case3(open):
    print('开始执行 test_case3 方法  要登录')
    pass

if __name__ == '__main__':
    pytest.main()
    # pytest.main("-v -x Testdemo")   #带参数调用方式1
    # pytest.main(['-v','-x','Testdemo'])  #带参数调用方式2
