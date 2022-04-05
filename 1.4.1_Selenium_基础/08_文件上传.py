from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_load():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
# 文件上传时，和正常的input输入框类似，区别在于传入的值为上传文件所在路径
    def test_upload(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.CSS_SELECTOR, ".soutu-btn").click()
        sleep(5)
        #使用XPATH方式定位上传文件按钮
        # self.driver.find_element(By.XPATH, "//*[@id='form']/div/div[2]/div[2]/input").send_keys(
        #     "E:/Python自动化基础2022/1.4.1_Selenium_基础/image/1.jpg")
        # 使用CSS_SELECTOR方式定位上传文件按钮
        self.driver.find_element(By.CSS_SELECTOR, ".upload-pic").send_keys(
            "E:/Python自动化基础2022/1.4.1_Selenium_基础/image/1.jpg")
        sleep(10)