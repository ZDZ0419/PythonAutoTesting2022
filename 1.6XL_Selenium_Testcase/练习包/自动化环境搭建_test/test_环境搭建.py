from selenium import webdriver
from time import sleep
from BSTestRunner import BSTestRunner

browser=webdriver.Chrome()
#browser=webdriver.Firefox()
#browser=webdriver.Ie()
browser.get("http://jwgl.jgxy.wj:8310/")

sleep(6)

            #登录并进入教务系统【id/name方式定位】
button_element=browser.find_element_by_id("details-button").click()
#button_element=browser.find_element_by_css_selector("#details-button").click()
sleep(3)
button1_element=browser.find_element_by_id("proceed-link").click()
sleep(2)
username_element=browser.find_element_by_id("username").send_keys("admin")
password_element=browser.find_element_by_id("password").send_keys("123456")
login_element=browser.find_element_by_name("submit").click()
sleep(2)
#browser.quit()
#browser.find_element_by_id("details-button").click()
#browser.find_element_by_class_name("small-link").click()
#browser.find_element_by_partial_link_text("高级").click()
#browser.find_element_by_css_selector("[class='secondary-button.small-link']").click()
# sleep(3)
# button1_element = browser.find_element_by_id("proceed-link").click()
# sleep(3)