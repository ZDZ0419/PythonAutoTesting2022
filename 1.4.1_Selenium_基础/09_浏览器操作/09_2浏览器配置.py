from selenium import webdriver
path = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default'
options = webdriver.ChromeOptions()
# 增加个人浏览器地址
options.add_argument('--user-data-dir='+path)
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://mail.163.com/')