import pytest


# 共享配置文件，其中的方法及函数都可在全局进行调用
# conftest文件为pytest特有的，文件名不可变更，且包下须有__init__.py文件
# conftest文件与运行的用例要在同一package下
@pytest.fixture(scope="function")  # 为function时，可不写scope信息
def login():
    print('这是一个登录操作')
