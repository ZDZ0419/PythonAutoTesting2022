'''
创建类：可定义某个类的对象具有的属性(变量)和方法(函数)
    Page.定义类名
    2.编写类的属性
    3.编写类的方法
'''
#创建猫类
Class Cat:
    #初始化方法
    def __init__(self,nick,color,age):
        #定义类的属性
        self.nick=nick   #昵称
        self.color=color  #颜色
        self.age=age    #年龄

     #自定义函数/方法时，函数名/方法名后必须有self
    def eat(self):
        print('猫在吃鱼！！！')

    def sleep(self):
        print('猫在睡觉！！！')

'''
创建对象
    对象名=类名(属性1,属性2,属性3)
'''
cat1=Cat('小黑','黑色',2)
cat2=Cat('大白','白色',8)

'''
获取某一对象的属性：
    对象名.属性名
调用类方法：
    对象名.方法名()
'''
# 获取某个对象的属性值
print(cat1.nick)
print(cat2.color)

#通过对象调用类方法
cat2.sleep()

#self关键字和初始化方法