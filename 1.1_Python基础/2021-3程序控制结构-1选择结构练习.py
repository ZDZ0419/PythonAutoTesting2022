'''
---练习1---
星期一特价菜：水煮鱼
星期二特价菜：烧排骨
星期三、四特价菜：宫爆鸡丁
星期五、六特价菜：清蒸鲈鱼
其它：老干妈土豆丝
要求：根据用户输入星期几，输出特价菜是什么？
'''
# data = input('请输入星期信息：')
# if data == '星期一':
#     print('今天的特价菜是：{}'.format('水煮鱼'))
# elif data == '星期二':
#     print('今天的特价菜是：{}'.format('烧排骨'))
# elif data == '星期三' or data=='星期四':
#     print('今天的特价菜是：{}'.format('宫爆鸡丁'))
# elif data == '星期五' or data == '星期六':
#     print('今天的特价菜是：{}'.format('清蒸鲈鱼'))
# else:
#     print('今天的特价菜是：{}'.format('老干妈土豆丝'))

'''
---练习2---
根据输入判断学生的成绩等级：
如果成绩>=90,输出“优秀”；
如果成绩>=80,输出“良好”；
如果成绩>=60,输出“中等”；
否则，输出“差”。
'''
# score = float(input('请输入学生成绩：'))
# a = '优秀'
# b='良好'
# c='中等'
# d='差'
# if score>=90.0:
#     print(a)
# elif score>=80.0 and score<90.0:
#     print(b)
# elif score>=60.0 and score<80.0:
#     print(c)
# else:
#     print(d)
'''
---练习3---
现在有一个银行保险柜，有两道密码，想拿到里面的钱必须两次输入的密码都正确。
如果第一道不正确，直接拦截在外面
如果第一道正确，才能输入第二道密码
只有第二道密码也正确是，才能拿到钱
'''
# passwd1=123456
# passwd2=654321
# password1=int(input('请输入您的第一道密码:'))
# if password1==passwd1:
#     print('第一道密码输入正确！')
#     password2 = int(input('请输入您的第二道密码:'))
#     if password2==passwd2:
#         print('密码2输入正确，密码箱已打开！')
#     else:
#         print('密码2输入错误！')
# else:
#     print('密码1输入错误！')
'''
---练习4---
开发一个计算器，用户输入一个数、加减乘除、第二个数，控制台显示计算结果。
'''
print('--欢迎使用ZZ计算器！--')
num1 = float(input('请输入第一个数num1：'))
AA = input('请输入运算符(+、-、*、/)：')
num2 = float(input('请输入第二个数num2：'))
result = 0  # 用来保存计算结果
msg = 1  # 记录是否有结果，1有结果  0 无结果
if AA == '+':
    result = num1+num2
elif AA == '-':
    result = num1-num2
elif AA == '*':
    result = num1*num2
elif AA == '/':
    result = num1/num2
else:
    print('无此计算方式！')
    msg = 0
if msg == 1:
    print('计算结果：', result)
