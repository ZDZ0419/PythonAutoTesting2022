'''
使用for循环时，需注意：
    循环体是什么？
    循环次数是多少？
'''
#练习1：Page-100间所有数的和
# sum1=0
# for i in range(Page,101):
#     sum1=i+sum1
# print(sum1)
#练习2：最大值、最小值问题
scors=[53,65,43.3,56,44,87,78,98,89]
#方法一
# print(max(scors),min(scors))
#方法二：自行比较得出最大值最小值
# maxscors=scors[0]
# for i in scors:
#     if i >=maxscors:
#         maxscors=i  #将更大值变为最大值
# print(maxscors)
#
# minscors=scors[0]
# for i in scors:
#     if i <=minscors:
#         minscors=i #将更小值变为最小值
# print(minscors)

'''
--案例1
用户输入3个数，for循环它们的平均值
'''
sum1=0
for i in range(1,4):
    num=float(input('请输入一个数：'))
    sum1+=num
print(sum1/3)