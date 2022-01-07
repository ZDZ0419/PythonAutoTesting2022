from selenium import webdriver

import requests
url="http://www.baidu.com"
res_1=requests.get(url)
print(res_1.status_code)
print(res_1.text)
print(res_1.headers)


