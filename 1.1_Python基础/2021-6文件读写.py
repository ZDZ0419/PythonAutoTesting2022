'''
文本文件：使用r/w/a    w:表示全部覆盖写入    a:表示追加，文件原内容不变
二进制文件：使用rb/wb/ab
方式一：
    file=open(r"文件路径","r/w/a/rb/wb/ab")  打开文件并赋给一个对象
    data=file.read()   文件读取
    file.write()  文件写入
    file.close()  关闭文件
方式二：(不用最后的.close())
with open(r"文件路径","r/w/a/rb/wb/ab") as file:
    data=file.read()
    file.write()
'''
# #查看文件内容：
# file=open(r"C:\Users\Administrator\Desktop\nn.txt",'r')
# data=file.read()
# file.close()
# print(data)
#
# #写入文件内容--覆盖原文
# str='你好，我的家乡'
# file=open(r"C:\Users\Administrator\Desktop\nn.txt",'w')
# file.write(str)
# file.close()
#
# #写入文件内容--追加
# str='\n你好，我的家乡1'
# file=open(r"C:\Users\Administrator\Desktop\nn.txt",'a')
# file.write(str)
# file.close()

#复制文件，相当于先读后写
file1=open(r"C:\Users\Administrator\Desktop\nn.txt",'r')
data=file1.read()
file1.close()

file2=open(r"E:\nn-Page.txt",'w')
file2.write(data)
file2.close()

#with open()使用,多个文件打开可用英文逗号对多个open()操作进行连接
with open(r"C:\Users\Administrator\Desktop\nn.txt",'r') as file3,open(r"E:\nn-a.txt",'w') as file4:
    data1=file3.read()
    file4.write(data1)