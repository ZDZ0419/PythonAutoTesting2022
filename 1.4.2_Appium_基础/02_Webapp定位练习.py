import pytest
from appium import webdriver
from time import sleep

class TestBrowser:
    def setup(self):
        des_caps = {
            'platformName': 'android',
            'platformVersion': '7.1.2',
            'browserName': 'Browser',
            'noReset': 'true',
            'deviceName': '127.0.0.1:62001',
            'chromedriverExecutable': 'F:\Program Files\AutoTest\APP\chrome driver'

        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', des_caps)
        sleep(5)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        sleep(6)
        self.driver.get('https://m.baidu.com')
        sleep(5)
#
if __name__ == '__main__':
    pytest.main()