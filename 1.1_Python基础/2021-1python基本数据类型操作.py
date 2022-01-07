# '''python 的基本数据类型：
# 数字类型、字符串、布尔型、列表、元组、字典、集合
# '''
# '''字符串操作'''
# s='hello my world'
# print(s*2) #重复打印字符串
# #字符串切片
# print(s[:5])  #取前4个索引对应的字符内容
# print(s[1:5]) # 取1到4索引位置对应的字符内容
# print(s[1:5:2])
# print(s[2:])
# #判断某字符内容是否在字符串中存在
# print('o' in s)
# #拼接字符串1 .join()内置方法
# a='start'
# b='stop'
# c='--'.join([a,b])
# print(c)
# '''返回值：start--stop'''
# #拼接字符串2 .format()
# print('测试{}--{}'.format(a,b))
# '''返回值：测试start--stop'''
# #统计字符个数
# m=s.count('l')
# print(m)
# '''返回值：3'''
# #首字母大写
# print(s.capitalize())
# '''返回值：Hello my world'''
# print(len(s))  #字符串长度
# print(s.center(20,'-'))  #字符串居中  【20：表示居中后字符串的总长度】
# '''返回值：---hello my world---'''
# print(s.ljust(20,'-'))  #字符串居左
# '''返回值：hello my world------'''
# print(s.rjust(20,'-'))  #字符串居右
# '''返回值：------hello my world'''
# print('查看元素的索引：{}'.format(s.find('o'))) # 查看元素的索引
# str0='ad22386nmm'
# print('根据内容向右开始查找元素位置：{}'.format(str0.rfind('2'))) # 返回元素位置，不是返回索引位置
# str='123'
# print('判断字符串是否为整数:{}'.format(str.isdigit())) #方式一 :#判断字符串是否为整数
# print('判断字符串是否为整数:{}'.format(str.isnumeric())) #方式二:#判断字符串是否为整数
# str1='abc123adC'
# print('判断字符串是否是数字+字母:{}'.format(str1.isalnum())) #判断字符串是否是数字+字母
# print('判断是否为字母:{}'.format(str1.isalpha()))  #判断字符串是否为字母
# str2='abc cba'
# print('判断是否为小写:{}'.format(str2.islower()))  #判断是否为小写
# print('判断是否为大写:{}'.format(str2.isupper())) #判断是否为大写
# print('判断每一个单词的首字母是否为大写:{}'.format(str2.istitle())) #判断每一个单词的首字母是否为大写
# print('将字符串中的所有小写变为大写：{}'.format(str2.upper()))
# print('将字符串中的所有首字母变为大写：{}'.format(str2.title()))
# print('将字符串中的所有大写变为小写：{}'.format(str2.lower()))
# print('将字符串中的所有大写变为小写，小写变为大写：{}'.format(str2.swapcase()))
# print('替换字符串中内容：{}'.format(str2.replace('b','G')))
# str3='  aaa  a   '
# print('去除字符串两边的空格：{}'.format(str3.strip()))
# print('去除字符串左边的空格：{}'.format(str3.lstrip()))
# print('去除字符串左边的空格：{}'.format(str3.rstrip()))
# str4='a b c'
# print('字符串转为列表：{}'.format(str4.split()))
# '''列表操作
# 特性：有序、元素可重复、可以存放多种数据类型'''
# list1=['小明','zhanghua','李勇',123,'玛丽','李勇1']
# #查看列表元素
# print('查看列表内容：{}'.format(list1))
# print('查看指定索引的内容：{}'.format(list1[0]))
# print('查看指定索引范围的内容：{}'.format(list1[1:3]))# 切片取，左闭右开
# print('查看指定索引到列表最后元素的内容：{}'.format(list1[1:]))
# print('查看指定索引到列表倒数第二个元素的内容：{}'.format(list1[1:-1]))
# print('查看指定索引到列表最后元素的内容,步长为2：{}'.format(list1[1::2]))#步长有方向{为正，向右取，为负，反向取}
# #增加列表元素
# list1.append('zhuli')
# print('append增加列表元素zhuli：{}'.format(list1)) #默认增加到列表最后
# list1.insert(3,'周虎')
# print('insert增加列表元素''周虎''：{}'.format(list1)) #指定位置添加元素
# #修改列表元素
# list1[0]='xiaoming'
# print('修改列表元素：{}'.format(list1)) #修改单个元素
# list1[1:3]=['zhanghua1','李勇1']
# print('修改列表元素：{}'.format(list1)) #修改多个元素
# #删除元素1 - remove移除
# print('使用remove删除前的列表元素：{}'.format(list1))
# list1.remove('zhuli')  #删除指定内容的值
# print('使用remove删除后的列表元素：{}'.format(list1))
# # #删除元素2 - pop移除
# print('使用pop删除前的列表元素：{}'.format(list1))
# x=list1.pop(-1)    #删除指定位置（索引）的值，可返回删除的元素
# print(x)
# print('使用pop删除后的列表元素：{}'.format(list1))
# #删除元素 - del移除
# print('使用del删除前的列表元素：{}'.format(list1))
# del list1[-2]    #可指定任意一个元素的索引进行删除，也可删除列表对象
# print('使用del删除后的列表元素：{}'.format(list1))
# #统计元素出现的次数
# list2=['zhanghua','zhouli','李勇','王文','李勇']
# print('统计列表中元素出现的次数：{}'.format(list2.count('李勇')))
# #合并列表
# list3=['linan','nikao']
# print('合并列表：{}'.format(list2+list3))
# #列表内容追加--extend
# print('追加前list2列表内容：{}，list3列表内容：{}'.format(list2,list3))
# list2.extend(list3) #将list3内容追加到list2列表的最后，list3不变
# print('extend追加后的list2列表内容：{},list3列表内容：{}'.format(list2,list3))
# print('返回某一列表内容对应的索引值：{}'.format(list2.index('王文')))
# #反转列表内容--从末位到首位显示
# print('反转前的列表内容：{}'.format(list2))
# list2.reverse()
# print('反转后的列表内容：{}'.format(list2))
# #列表排序
# print('排序前的列表内容：{}'.format(list2))
# list2.sort()  # 只能对英文/中文单独排序，不能进行组合排序
# print('排序后的列表内容：{}'.format(list2))
# #判断内容是否存在于列表中
# print('判断列表内容是否存在于列表中:{}'.format('linan' in list2))
# '''元组操作
# 特性：有序、元素可重复、可以存放多种数据类型,元素不可更改、删除'''
# tup1=('小明','zhanghua','李勇',123)
# tup2=('朱华','nanling',321,'')
# #查询元组,元组内容不能修改、删除
# print('查看元组内容:{}'.format(tup1))
# print('查看元组指定内容:{}'.format(tup1[2]))
# print('查看元组指定内容:{}'.format(tup1[1:3])) #元组切片
# #合并元组
# print('合并多个元组:{}'.format(tup1+tup2))
# #删除元组
# del tup2
# '''字典操作--键值对
# 特性：无序、键不可重复、一般使用字符串作为键
# '''
# dict1={'name':'张华','age':18,'sex':'男'}
# #查询字典
# print('使用key查询对应的value：{}'.format(dict1['name']))
# #增加、修改字典
# dict1['name']='周华' #添加/修改字典内容
# print('添加/修改字典内容：{}'.format(dict1))
# # setdefault 默认值的使用，当key存在时，使用字典中对应的值，当不存在时，使用默认值
# dict2={'age':'19','sex':'男','学历':'本科','name':'张华'}
# dict1.setdefault('name','wangwu')  #如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值
# print('查看字典中所有的key:{}'.format(dict1.keys()))
# print('查看字典中所有的key:{}'.format(dict1.values()))
# print('查看字典中所有的key:{}'.format(dict1.items()))
# #更新字典信息
# ##用于更新字典中的键/值对，可以修改存在的键对应的值，也可以添加新的键/值对到字典中
# print('字典初始值:{}'.format(dict1,dict2))
# dict1.update(dict2) #dict2不变，dict1变更为更新后的值
# print('update字典后的值:{}'.format(dict1))
# #删除字典信息  del  clear  pop
# print('del前的字典内容：{}'.format(dict2))
# del dict2['sex']   # del
# print('del后的字典内容：{}'.format(dict2))
# print('pop前的字典内容：{}'.format(dict2))
# dictt=dict2.pop('学历')  #pop：删除字典元素，有返回值
# print(dictt)
# print('pop后的字典内容：{}'.format(dict2))
# print('popitem前的字典内容：{}'.format(dict2))
# dictt=dict2.popitem()  #pop：随机删除字典元素，有返回值
# print(dictt)
# print('popitem后的字典内容：{}'.format(dict2))
# print('clear前的字典内容：{}'.format(dict2))
# dict2.clear()  # clear ：清空字典
# print('clear后的字典内容：{}'.format(dict2))
'''集合操作
特性：无序，元素不重复，集合本质上就是之间键的字典。
用法：去重、集合运算'''
#集合去重
set1={21,31,12,31,33,321,33,12,'李娜'}
print(set1)
#集合运算
set2={1,2,3,4}
set3={4,5,6,7,8}
print('两集合的交集:{}'.format(set2&set3)) #交集
print('两集合的并集:{}'.format(set2|set3)) #并集
print('两集合的差集:{}'.format(set2-set3)) #差集













