'''集合操作
特性：无序，元素不重复，集合本质上就是之间键的字典。
用法：去重、集合运算'''
#集合去重
set1={21,31,12,31,33,321,33,12,'李娜'}
print('set1去重后的集合为：{}'.format(set1))
#集合运算
set2={1,2,3,4}
set3={4,5,6,7,8}
print('两集合的交集:{}'.format(set2&set3)) #交集
print('两集合的并集:{}'.format(set2|set3)) #并集
print('两集合的差集:{}'.format(set2-set3)) #差集

lx()