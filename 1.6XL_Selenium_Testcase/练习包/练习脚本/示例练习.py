'''
a="{0:b}".format(12345)
print(a)

print(5+3)
print(13-5)
print(int(16/2))
print(4*2)

a=str(8)
a='最喜欢的数字为：' + a
print(a)

bicycles = ['trek ', 'cannondale', 'redline', 'specialized','123']
massage='My first bicycle was a ' + bicycles[-1].title().rstrip() + ' !!!'
massage_1='My first bicycle was a ' + bicycles[1].title().rstrip() + ' !!!'
print(bicycles[3])
print(bicycles[-1])
print(bicycles[0].title())
print(bicycles[0].rstrip())
print(massage)
print(massage_1)

names=['王璐','丽娜','华龙','周星星','花语嫣',' lonergevn ']
#print(names[-1].strip())
#print(names[2].strip()+','+'欢迎您 !!!')

#for i in range(0,6):
 #   print(names[i].strip()+','+'欢迎您 !!!')
# 修改列表元素
names[-1]='周宇文'
#print(names)
# 增加列表元素_自动将其补到列表的最后一位
names.append('ducati')
print(names)
# 指定位置插入元素
names.insert(6,'周正宇')
print(names)
# 删除列表元素
del names[6]
print(names)
'''
'''
# 删除列表末尾元素后，并接着使用它  [ pop()的括号中可以接索引，可以弹出任意位置的值]
names_2=['王璐','丽娜','华龙','周星星','花语嫣',' lonergevn ']
print(names_2)
names_3=names_2.pop()
#print(names_2)
print(names_3)
'''
'''
# 根据值删除元素,删除后的值还可复用，默认删除匹配出的第一个值
names_2=['王璐','丽娜','华龙','周星星','花语嫣',' lonergevn ','王璐']
AA='王璐'
names_4=names_2.remove(AA)
print(AA)
print(names_2)
print(AA.title() + '退学了')

#  思考：如果删除的值在列表中存在多次时，如何进行删除
'''
'''
names_2=['a王璐','b丽娜','n华龙','d周星星','g花语嫣',' lonergevn ','c王璐']
names_2.sort()
print(names_2)
names_2.sort(reverse=True)
print(names_2)
print(sorted(names_2))
print(names_2)
'''
name_YH = ['李阳','王璐','翔宇','李想']
for i in range(0,4):
    print(name_YH[i] +',欢迎到来！！！')

print('\t“'+ name_YH[2] + '”' +'因有事无法准时赴约')

name_YH[2]='宇文成都'
for i in range(0,4):
    print('\t\t'+ name_YH[i] +',欢迎到来！！！')

print('\t\t\t'+ '注意，请大家现在调整至包间就坐')

name_YH.insert(0,'萧阳')
print(name_YH)

name_YH.insert(3,'王林')
name_YH.append('戊辰')
print(name_YH)

for i in name_YH:
    print('\t\t\t' + i + ',欢迎到来！！！')

#for i in range(0,7,3):
#    print('\t\t\t\t' + name_YH[i] + ',欢迎到来！！！')
print('sorry,因新餐桌没有正常到达，故目前只能允许两人参加宴会')
for i in range(2,7):
    name_YH1 = name_YH.pop(2)
    print('\t\t\t\t' + name_YH1+ ',因餐桌未能正常到达，无法邀请您来共进晚餐，在此表示歉意。')



