import pytest
class Testdemo():
    def test_one(self):
        print('开始执行 test_one 方法')
        x = 'this'
        assert 'h' in x

    def test_two(self):
        print('开始执行 test_two 方法')
        x = 'hello'
        assert 'e' in x

    def test_three(self):
        print('开始执行 test_three 方法')
        a = 'hello'
        b = 'hello world'
        assert a in b

if __name__ == '__main__':
    pytest.main()
    # pytest.main("-v -x Testdemo")   #带参数调用方式1
    # pytest.main(['-v','-x','Testdemo'])  #带参数调用方式2
