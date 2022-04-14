from selenium import webdriver
from time import sleep
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
'''
frame框架：分为frameset/frame/iframe,其中frameset使用正常方式定位即可，frame、iframe需切frame框架进行定位
切入框架：switch_to.frame("属性值= ")   
    分为id切入、name切入、webelement对象切入（需先定位frame框架，得到框架对象，使用对象切入）、
    索引切入，当frame框架存在嵌套时，里层的frame框架需层层切入
返回上层框架：switch_to.parent_frame()
切出最顶层的frame框架：switch_to.default_content()  括号中不添加参数
同级frame框架之间切换时，需先切出原框架再切入目标框架
'''
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.implicitly_wait(3)

dengl_1=driver.find_element(By.LINK_TEXT,"登录").click()
sleep(5)
#dengl_2=driver.find_element(By.CSS_SELECTOR,".tang-pass-footerBarULogin.pass-link").click()
dengl_2=driver.find_element(By.PARTIAL_LINK_TEXT,"用户名登录").click()
#dengl_2=driver.find_element(By.ID,"TANGRAM__PSP_11__footerULoginBtn" ).click()
sleep(2)
dengl_3=driver.find_element(By.ID,"TANGRAM__PSP_11__userName").send_keys("crqok")
sleep(3)
#driver.switch_to.frame()

'''
多窗口操作：
通过窗口句柄操作网页
获得当前网页的窗口句柄：driver.current_windows_handle
获得打开的所有网页的窗口句柄(会得到一个句柄列表，索引根据网页的打开顺序从0开始递增)：
    window_lists=driver.window_handles
网页切换：driver.switch_to.window(window_list)
关闭网页：driver.close()
网页最大化/最小化：driver.maxsize_window()  / driver.minsize_window()
网页大小设置(设置网页分辨率)：driver.set_window_size(1920,1080)
网页刷新：driver.refresh()
网页前进/后退：driver.forward() 、driver.back()
获取网页上的url：driver.current_url()
获取网页上的标题：driver.title()
获取网页上的文本：需先定位元素，再获取文本 .text

'''
'''
告警窗口操作：
切入告警窗口：switch_to.alert
获取告警对象：alert_element=switch_to.alert
确定：alert_element.accept()
取消：alert_element.dismiss()
获取告警窗文本：alert_element.text
输入内容：alert_element.send_keys("要输入的内容")

'''
