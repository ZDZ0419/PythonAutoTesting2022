import requests

base_ur = "http://httpbin.org"

r = requests.get(base_ur+"/get")
print(r.status_code)
# r=requests.post(base_ur+'/post')
# print(r.status_code)
# r=requests.put(base_ur+'/put')
# print(r.status_code)
# r=requests.delete(base_ur+'/delete')
# print(r.status_code)

## url参数传递
# param_data={'user':'zxw','password':'6666'}
# r=requests.get(base_ur+'/get',param_data)
# print(r.url)
# print(r.status_code)

# body参数传递
# form_data={'user':'zxw','password':'6666'}
# r=requests.post(base_ur+'/post',data=form_data)
# print(r.text)

# 请求头定制
# form_data={'user':'zxw','password':'6666'}
# header={'user-agent':'Mozilla/5.0'}
# r=requests.post(base_ur+'/post',data=form_data,headers=header)
# print(r.text)
# # 获取json内容
# print(r.json())

# header={'user-agent':'Mozilla/5.0 (Windows NT 6.Page) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
# r=requests.get('https://www.zhihu.com/explore',headers=header)
# # 打印响应文本
# print(r.text)
# # 打印状态码
# print(r.status_code)
# # 打印响应头信息
# print(r.headers)


#设置cookie
# cookie={'user':'51zxw'}
# r=requests.get(base_ur+'/cookies',cookies=cookie)
# print(r.text)

# #获取cookies
# r=requests.get('http://www.baidu.com')
# print(type(r.cookies))
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+':'+value)
#
# # 超时timeout
# cookie={'user':'51zxw'}
# r=requests.get(base_ur+'/cookies',cookies=cookie,timeout=0.5)
# print(r.text)

# 文件上传(可绝对路径也可相对路径)
# file={'file':open('16.jpg','rb')}
# r=requests.post(base_ur+'/post',files=file)
# print(r.text)

# # session 会话对象
# s=requests.session()
# r=s.get(base_ur+'/cookies/set/user/51zxw')
# print(r.text)
#
# r=s.get(base_ur+'/cookies')
# print(r.text)


