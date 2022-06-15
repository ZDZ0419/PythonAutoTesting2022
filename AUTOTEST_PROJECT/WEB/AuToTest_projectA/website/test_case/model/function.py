from selenium import webdriver
import os
import time

# 截图
def insert_img(driver,filname):
    func_path=os.path.dirname(__file__)
    print(func_path)

    base_dir=os.path.dirname(func_path)
    print(base_dir)

    base_dir=str(base_dir)
    base_dir=base_dir.replace("\\","/")
    print(base_dir)

    base=base_dir.split("/website")[0]
    print(base)

    filepath=base+'/website/test_report/screenshot/'+ time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) +"-"+filname
    driver.get_screenshot_as_file(filepath)

#  查找最新报告
def latest_report(report_dir):
    lists=os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))

    print("The latest report is "+lists[-2])

    file=os.path.join(report_dir,lists[-2])
    return file


#  邮件发送


if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get("http://www.sogou.com")
    insert_img(driver,"A.png")
    driver.quit()