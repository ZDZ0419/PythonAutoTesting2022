# from selenium import webdriver
# from time import sleep
#
# driver=webdriver.Chrome()
# # 打开百度首页
# driver.get("http://www.baidu.com")
#
# # 【id和name定位元素】
# driver.find_element_by_id("kw").send_keys("刘德华")      #  id定位
# driver.find_element_by_name("wd").send_keys("周华健")    #  name定位
#
# #【class_name定位元素】
# driver.find_element_by_class_name("s_ipt").send_keys("李子龙")   # class_name定位
# sleep(2)
#
# #【Xpath层级与属性结合定位元素：当找不到元素进行定位时】
# driver.find_element_by_xpath("//form[@id='form']/span/input[1]").send_keys("周卫国")
#
# #【Xpath的逻辑运算组合定位方式：元素属性不唯一】
# driver.find_element_by_xpath("//input[@id='kw' and @name='wd']").send_keys('李云龙')
#
# #【css定位】-- 极力推荐
# #【css使用id属性值进行定位：#id属性值】
# driver.find_element_by_css_selector('#kw').send_keys('林俊杰')
# #【css使用class属性值进行定位: .class属性值】
# driver.find_element_by_css_selector('.s_ipt').send_keys('邓紫棋')
# #【css使用属性进行定位: [属性名='属性值']】使用class属性整体进行定位时，其属性值前不需要加 '.'
# driver.find_element_by_css_selector('[autocomplete="off"]').send_keys('花花')
# driver.find_element_by_css_selector('[class="s_ipt"]').send_keys('花花1')
# #【css使用元素层级来进行定位：标签名#属性值>标签名>元素所在的标签名】
# driver.find_element_by_css_selector('form#form>span>input').send_keys('花花2')
# sleep(5)
# driver.find_element_by_id("su").click()
# sleep(3)
# driver.quit()


# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By      #导入By模块
#
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://www.51zxw.net")

#【link_text定位方式：根据超链接文本进行定位】
#driver.find_element_by_link_text('登录/注册').click()     # 完全匹配定位
##driver.find_element(By.LINK_TEXT,'登录/注册').click()  #使用By模块进行元素定位
#sleep(3)
# driver.find_element_by_partial_link_text('注 册').click()  #  模糊匹配定位
##driver.find_element(By.PARTIAL_LINK_TEXT,'注 册').click()   #使用By模块进行元素定位
# sleep(3)
# driver.find_element_by_id('loginStr').send_keys('12345678911')
# sleep(3)
# driver.find_element_by_tag_name('button').click()
#driver.find_element_by_id("loginStr").send_keys("111111")
#sleep(5)


# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
#
# browse=webdriver.Chrome()
# browse.maximize_window()
# browse.get("http://360.cn")

#【下拉框定位】
# #browse.find_element(By.XPATH,"//div[@id='search-block']/span").click()  #使用Xpath以及by模块进行元素定位
# browse.find_element(By.CSS_SELECTOR,"div#search-block>span").click()  #TURE
# browse.find_element(By.LINK_TEXT,'新闻').click()  #TURE
# sleep(6)

# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By         #导入By模块
# from selenium.webdriver.common.action_chains import ActionChains     #导入鼠标操作的库
#
# browse=webdriver.Chrome()
# browse.get("http://www.baidu.com")
# browse.maximize_window()
#
# #定位到输入框
# browse.find_element(By.CSS_SELECTOR,'#kw').send_keys("周华健")
# AA=browse.find_element(By.CSS_SELECTOR,'#kw')
# sleep(3)
#
# #【鼠标双击操作】
# ActionChains(browse).double_click(AA).perform()
# sleep(3)
#
# #【鼠标右击操作】
# ActionChains(browse).context_click(AA).perform()
# sleep(2)
# #【鼠标悬停操作】
# BB=browse.find_element(By.CSS_SELECTOR,'.pf')
# ActionChains(browse).move_to_element(BB).perform()
# sleep(2)

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By         #导入By模块
from selenium.webdriver.common.keys import Keys     #导入键盘操作的库

browse=webdriver.Chrome()
browse.get("http://www.baidu.com")
browse.maximize_window()

browse.find_element(By.CSS_SELECTOR,'#kw').send_keys("周华健")

#【键盘操作：全选】
browse.find_element(By.CSS_SELECTOR,'#kw').send_keys(Keys.CONTROL,'a')
#【键盘操作：复制&剪切】
browse.find_element(By.CSS_SELECTOR,'#kw').send_keys(Keys.CONTROL,'c')
browse.find_element(By.CSS_SELECTOR,'#kw').send_keys(Keys.CONTROL,'x')

# 打开搜狗页面
browse.get("http://www.sogou.com")

#【键盘操作：粘贴】
browse.find_element(By.CSS_SELECTOR,'.sec-input').send_keys(Keys.CONTROL,'v')
sleep(3)
#browse.find_element(By.XPATH,'//input[@type="submit" and @id="stb"]').click()
browse.find_element(By.CSS_SELECTOR,'input[id="stb"]').click()
#browse.find_element(By.CSS_SELECTOR,'[type="submit"]').click()
sleep(3)
browse.quit()