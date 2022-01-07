# python的必备语法
#标识符:
        # 1.由字母、数字、下划线组成，且不能以数字开头
        # 2.不能包含关键字
import keyword
print(keyword.kwlist)
        # 3.包含（项目名、模块名、包名、类名、函数名、变量名）
    #变量名
# y=x+3  x:自变量   y:因变量
    #   变量在引用前，必须进行定义并赋值
# sex='boy'
# print(sex)
# 行和缩进
    # 行：每一行代表的都是新的代码，新的语句，换行表示本行代码结束
    # 缩进：用来控制层级
age=int(input('请输入年龄：'))
if age>18:
    print('年龄大于18岁！A')
#elif age=18:
    #print('年龄等于18岁！B')
else:
    print('年龄小于18岁！C')


