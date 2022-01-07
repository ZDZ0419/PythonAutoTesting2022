import requests
from urllib import parse

# 手机号正确
data={'mobileCode':'13213226607','userID':''}
#cityId=parse.urlencode(data).encode('utf-8')
#proxies={'http':'http://111.155.116.227:80'}
url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo'

r=requests.get(url,params=data)
print(r.text)
