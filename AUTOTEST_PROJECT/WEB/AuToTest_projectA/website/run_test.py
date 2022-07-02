import unittest
from function import *
from BSTestRunner import BSTestRunner
import time

report_dir = './test_report'
test_dir = './test_case'

print("start run test case...")
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')

now = time.strftime('%Y%m%d%H%M%S')
report_name = report_dir+"/"+now+"result.html"

print("start write report")
# 运行前记得把BSTestRunner.py 120行‘unicode’ 换成‘str’
with open(report_name, 'wb') as f:
    runner = BSTestRunner(stream=f, title="login_report", description="This is login_report")
    runner.run(discover)
f.close()

print("find latest report START")
latest_report = latest_report(report_dir)
print(latest_report)
print("find latest report END")
print("test END")