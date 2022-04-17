'''
a = ' pyt hon  '
print(a.strip())
print(a.lstrip())
print(a.rstrip())

user_name=input("请输入用户姓名：")
--a="hello " + user_name + ", would you like to learn some Python today?”"
print(a)

user_name = "wanG mei"
print(user_name.lower())
print(user_name.upper())
print(user_name.title())
'''
'''
cars = ['bmw', 'audi', 'toyota', 'subaru']
#原排列顺序
print(cars)
#按顺序升序进行排列(永久改变)
cars.sort()
print(cars)
#按倒序进行排序(永久改变)
cars.sort(reverse=True)
print(cars)
cars_1 = ['bmw', 'audi', 'toyota', 'subaru']
#按升序进行排序(原列表不变，仅一次)
print(sorted(cars_1))
#查看原列表内容
print(cars_1)
#按降序进行排序(原列表不变，仅一次)
print(sorted(cars_1,reverse = True))
#查看原列表内容
print(cars_1)

cars_2 = ['bmw', 'audi', 'toyota', 'yubaru']
cars_2.reverse()  # 倒着打印列表（可再次执行此语句，使其进行倒转，对列表顺序进行还原）
print(cars_2)
cars_2.reverse()
print(cars_2)

# 确定列表长度
print(len(cars_2))
'''
'''
list=[]
list.append('shanghai')
print(list)
list.insert(0,'nanjing')
print(list)
'''
'''
city=input("请输入您想去的地点：")
list=[]
list.append(city)
print(list)
'''
'''
list=[]
for i in range(0,5):
    i=0
    city = input("请输入您想去的地点：")
    list.append(city)
    i=i+Page
print(list)
'''
'''
list=['beijing', 'nanjing', 'shanghai', 'guilin', 'lijiang']
print(sorted(list))
print(list)
print(sorted(list,reverse=True))
print(list)
list.reverse()
print(list)
list.reverse()
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
'''
'''
# for循环遍历列表
citys=['北京', '南京', '上海', '桂林', '丽江']
for city in citys:
    print(city+',真不错')
    print('希望还能再来'+city+'\n')
print('非常感谢大家的到来！！！')
'''
'''
for vaule in range(Page,5):
    print(vaule)
numbers=list(range(2,5,2))
print(numbers)

#如何创建一个列表，其中包含前10个整数（即1~10）的平方呢？
list=[]
for i in range(Page,11):
    i=i**2
    list.append(i)
    #list.append(i**2)
print(list)

# 列表解析，简化代码行数
list=[i**2 for i in range(Page,11)]
print(list)
'''
'''
# 练习1
for i in range(Page,21):
    print(i)
list=[]
for i in range(Page,1000000):
    list.append(i)
#print(list)
print(min(list))
print(max(list))
print(sum(list))
'''
'''
# 练习2
for i in range(Page,21,2):
    print(i)
    '''
'''
# 打印包含 3~30 内能被 3 整除的数字的列表
list=[]
for num in range(3,31):
    if num%3==0:
        list.append(num)
print(list)

list_1=[]
for i in range(Page,11):
    i=i**3
    list_1.append(i)
print(list_1)

list_2=[i**3 for i in range(Page,11)]
print(list_2)
# 列表切片
print(list_2[Page:4])
# 遍历切片
for i in list_2[Page:4]:
    print(i)
list_3=list_2[:]
print(list_3)
list_2.insert(0,3)
list_3.append(3)
print(list_2)
print(list_3)
'''
'''
# 元组
citys=('上海','北京','桂林')
#for city in citys:
    #print(city)
citys=('上海','广州','桂林')
print(citys)
'''
'''
a='shanghai'
b='Beiijng'
c='Shanghai'
print(a==b)
print(a!=b)
print(a==c.lower())
list=['shanghai','Beiijng','Shanghai']
a='nanjing'
if a in list:
    print(a+'在列表中')
else:
    print(a + '不在列表中')
'''
'''
alien_color='green'
if alien_color=='red':
    print('成功射杀一人，获取5个点')
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
'''
'''
user_no=['AA','BB','CC']
USER=[]
while user_no:
    user_1=user_no.pop()
    print('待注册用户'+ user_1)
    USER.append(user_1)
print('已注册用户:')
for user in USER:
    print(user)
#print(user_no)

# 使用while循环删除列表中重复的值
user_no=['AA','BB','CC','AA','AA','AA']
while 'AA' in user_no:
    user_no.remove('aa')
print(user_no)
'''
'''
#   使用用户输入来填充字典
user={}
active=True
while active:
    user_input=input('输入用户姓名：')
    user_age=input('输入用户年龄：')

# 定义函数
def user(name):
    print('Hello world' + '\t'+name)
# 调用函数
user('张华')
user('张慧')
# 编写一个名为 display_message()的函数，它打印一个句子，指出你在本
# 章学的是什么。调用这个函数，确认显示的消息正确无误。
def display_message():
    print('本章主要学习了函数的定义及调用')
display_message()

# 实参与形参的使用
# 编写一个名为 favorite_book()的函数，其中包含一个名为 title
# 的形参。这个函数打印一条消息，如 One of my favorite books is Alice in Wonderland。
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title,page):
    print('One of my favorite books is Alice in Wonderland：' + title + '\t总计'+ page + '页')
favorite_book('西游记','54')
favorite_book(page='45',title='西游记')

# 定义函数添加默认值时，带默认值的形参放在形参位置的最后位
def favorite_book(page,title='西游记'):
    print('One of my favorite books is Alice in Wonderland：' + title + '\t总计'+ page + '页')
favorite_book(page='32')

# 编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到 T 恤上
# 的字样。这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。
# 使用位置实参调用这个函数来制作一件 T 恤；再使用关键字实参来调用这个函数。
def make_shirt(size,ZY):
    print('T恤的尺码为：' + size + '\n\t 字样为：' + ZY)
make_shirt('xl','我爱中国')
def make_shirt(size,ZY='I love Python'):
    print('T恤的尺码为：' + size + '\n\t 字样为：' + ZY)
make_shirt('xxl')
make_shirt('xl')
make_shirt('xxxl',ZY='我爱中国')
'''
'''
# 函数返回值的使用
def make_shirt(country,ZY):
    mas=country + ',' + ZY + '!!!'
    return mas
tt=make_shirt('中国','我爱你')
print(tt)
'''
'''
# 默认值设置为空，则可以进行形参与实参数量不符时保证代码正常运行（实参的内容必须包含在形参下）
def make_shirt(country,ZY=''):
    mas=country + ',' + ZY + '!!!'
    return mas
tt=make_shirt('中国')
print(tt)
'''
'''
# 定义函数，返回字典(返回的字典是无序的)
def name(xing,ming,age=''):    # 新增一个可选形参age
    user_name={'姓':xing,'名':ming}
    if age:     # 判断age的实参是否为True
        user_name['年龄']=age      #  指定age的key ：'年龄'
    return user_name
user=name('张','云溪',age=18)
print(user)
'''
'''
# 定义函数与while循环的使用--字符串的使用
def name(xing,ming):
    user_name=xing + ' '+ ming
    return user_name
while True:
    #print('请输入姓名：')
    print('【输入"q"回车即可退出输入状态】')
    user_1 = input('输入姓：')
    user_2 = input('输入名：')
    user_3=input('是否退出y/n:')
    if user_3=='y':
        break
    elif user_3=='n':
        continue
user=name(user_1,user_2)
print(user)
'''
def name(xing,ming):
    user_name=[{'姓':xing,'名':ming}]
    return user_name
while True:
    #print('请输入姓名：')
    print('【输入"q"回车即可退出输入状态】')
    user_1 = input('输入姓：')
    user_2 = input('输入名：')
    user_3=input('是否退出y/n:')
    if user_3=='y':
        break
    elif user_3=='n':
        continue
user=name(user_1,user_2)
print(user)



