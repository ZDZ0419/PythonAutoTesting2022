from time import sleep

from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.taobao.taobao'
desired_caps['appActivity'] = 'com.taobao.tao.TBMainActivity'
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
sleep(10)
driver.quit()

