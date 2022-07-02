from time import sleep

'''创建一个公共的页面类【page类】'''
class Page():

    # 封装一个浏览器页面初始化方法
    def __init__(self, driver):
        self.base_url = 'https://www.51zxw.net'
        self.driver = driver
        self.timeout = 10

    # 封装 可以打开不同子页面 的私有方法
    def _open(self, url):
        url_ = self.base_url + url
        print(">>>>>>>>>>>>>>Test page is:%s<<<<<<<<<<<<<<<<<<<" %url_)
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)
        # 对当前页面的url与要访问的子页面的url进行断言
        assert self.driver.current_url == url_, 'Did not land on %s' %url_

    # 定义一个可以调用私有方法_open()的公共方法
    def open(self):
        self._open(self.url)

    # 封装元素定位方法
    def find_element(self, *loc):
        return self.driver.find_element(*loc)