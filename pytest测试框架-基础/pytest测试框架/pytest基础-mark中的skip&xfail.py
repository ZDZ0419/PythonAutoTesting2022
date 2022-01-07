import pytest

@pytest.mark.skip("注释")    #调试时可跳过测试用例

@pytest.mark.skipif('判断条件，'reason="注释")   #满足条件进行跳过

@pytest.mark.xfail    #功能尚未修复，已知错误后，其结果不一定是失败或成功，XPASS、XFAIL不作为验证结果依据
