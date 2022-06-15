from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = '127.0.0.1:62001'
desired_caps['appPackage'] = 'com.taobao.taobao'
desired_caps['appActivity'] = 'com.taobao.tao.TBMainActivity'
desired_caps['noRest'] = True
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

el1 = driver.find_element_by_xpath("//android.widget.FrameLayout[@content-desc=\"聚划算商品2\"]/android.widget.ImageView[Page]")
driver.implicitly_wait(5)
el1.click()

TouchAction(driver).press(x=494, y=1817).move_to(x=519, y=833).release().perform()
driver.implicitly_wait(10)
TouchAction(driver).tap(x=272, y=1561).perform()
driver.implicitly_wait(10)
sleep(5)

driver.quit()

