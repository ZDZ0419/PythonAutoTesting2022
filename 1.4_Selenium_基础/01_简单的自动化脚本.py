from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

class Testbaidu:
    def setup(self):
        self.driver = webdriver.Chrome()
        #driver=webdriver.Firefox()
        #driver=webdriver.Ie()
        self.driver.get("http://www.baidu.com")
        self.driver.maximize_window()  #窗口最大化
        sleep(3)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.find_element(By.ID,'kw').send_keys('刘德华')
        self.driver.implicitly_wait(5)  #隐式等待5s
        self.driver.find_element(By.ID,'su').click()
        windows_list1 = self.driver.window_handles #获取网页句柄
        print(windows_list1) #打印网页句柄列表
        #显示等待10s，直到元素‘百度百科’加载出来,并点击
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.LINK_TEXT,'百度百科'))).click()
        windows_list2=self.driver.window_handles #获取所有的网页句柄
        print(windows_list2) #打印网页句柄列表
        self.driver.switch_to.window(windows_list2[1]) #切换至新打开的网页
        #显示等待10s，等待元素‘>>>’加载出来
        # element = WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.lemmaWgt-lemmaSummary-more')))

        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.wiki-lemma-icons_down-arrow')))
        element.click()
        sleep(10)


