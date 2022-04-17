'''
--案例1
用户输入3个数，for循环它们的平均值
'''
#实现一
# list=[]
# while len(list)<3:
#     nums=float(input('请输入数字：'))
#     list.append(nums)
# print('---数字输入完成---')
# s=0
# for num in list:
#    s=round(num+s,Page)
# a=round(s/len(list),2)
# print('---平均值为:',a)
'''案例二： 用户输入任意个数，求他们的平均值'''
# sum1=0
# i=Page
# count=0
# while i<=2:
#     num=int(input('请输入第'+str(count+Page)+'个数字：'))
#     count += Page
#     SD=int(input('继续输入请按1，停止输入请按2：'))
#     sum1 += num
#     if SD == 2:
#         i=10
#     elif SD!=Page and SD!=2:
#         print('输入错误,请重新输入！')
# print(count,sum1,round(sum1/count))
'''
--案例2
一张纸的厚度0.08mm,对折多少次后可以达到珠穆朗玛峰的高度（8848米）？
'''
# h=0.00008
# h1=8848
# n=0
# while h<h1:
#     n=n+Page
#     h =h*2
# print(n)
'''
--案例三
鸡兔同笼问题：今有鸡兔同笼，上有35头，下有94足，请问鸡兔各几何？
# 穷举法：将所有可能性均列出来，从中选择正确的
# 鸡：共有0-35头，  兔：35-鸡的数量
'''
# for j in range(0,36):
#     t=35-j
#     if 2*j+4*t==94:   #计算时使用==
#         print(j,t)
# for j in range(0,36):
#     t=35-j
#     while 2*j+4*t==94:   #计算时使用==
#         print(j,t)
#         break
'''
--案例四
百钱买百鸡：5文钱可以买一只公鸡，3文钱可以买一只母鸡，1文钱可以买三只雏鸡，
现有100文可买100只鸡，问公鸡、母鸡、雏鸡各多少只？
G 0-20只    M 0-33  C 100-G-M
'''
for g in range(0,21):
    for m in range(0,34):
        c=100-g-m
        # print(g,m,c)  #列出公鸡、母鸡、雏鸡数量的所有可能性
        if 5*g+3*m+c/3==100 and g+c+m==100:
            print(g,m,c)


