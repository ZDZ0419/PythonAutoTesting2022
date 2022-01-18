# 在pycharm的Terminal中，pytest 运行命令时加入 --alluredir=path，
# 生成测试报告结果数据到文件夹： pytest --alluredir=./myallure
#     结果数据文件夹可直接生成，不用提前创建

# 将测试数据转化为html测试报告文件：allure serve ./myallure

# 将测试报告结果数据生成一个html测试报告到另一个文件report下：
# allure generate ./myallure/ -o ./report/ --clean
# 备注：使用--clean先清空report文件夹，再生成新的测试报告

# 本地浏览器打开测试报告：allure  open  -h 127.0.0.1-p8883./report