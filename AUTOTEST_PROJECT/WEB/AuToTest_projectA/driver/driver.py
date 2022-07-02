from selenium import webdriver

def browser():
    driver = webdriver.Chrome()
    # driver = webdriver.Firefox()
    # driver = webdriver.Ie()

    # # 测试网址是否可正常打开
    # driver.get("http://www.baidu.com/")

    return driver

if __name__ == '__main__':
    browser()