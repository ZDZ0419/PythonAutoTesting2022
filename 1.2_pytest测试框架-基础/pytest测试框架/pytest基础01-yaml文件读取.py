import pytest
import yaml

#可以是列表、字典,也可相互嵌套
class TestData:
    @pytest.mark.parametrize(("a","b"), yaml.safe_load(open("data.yml")))
    def test_data(self,a,b):
        print(a + b)
@pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./data1.yml",encoding="UTF-8")))
#对于yaml读取文件时，文件编码格式不正确问题，可在读取文件时指定编码格式
def test_data(a,b):
    print(a + b)

# @pytest.mark.parametrize(("a","b"),[(10,20),(3,9)])
# def test_ymldata(a,b):
#     print(a+b)

