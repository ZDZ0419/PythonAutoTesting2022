import unittest
import  requests
from urllib import parse
from time import sleep

class phoneTest(unittest.TestCase):
    def setUp(self):
        self.url='http://ws.webxml.com.cn/WebServices/MobileCodeWS.asmx/getMobileCodeInfo'

    def test_weather_1(self):
        data={'mobileCode':'13213226607','userID':''}
        r=requests.get(self.url,params=data)
        r1=
        self.assertIn(r1,'13213226607：河南 郑州 河南联通GSM卡')

if __name__ == '__main__':
        unittest.main()
