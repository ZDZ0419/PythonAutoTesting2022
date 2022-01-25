
#函数+yield==生成器
def function():
    for i in range(5):
        print("before:{}",i)
        #return i   #return 函数调用结果与次数无关，均为0(第一次调用的结果)
        yield i #生成器，类似于return+暂停+记录上一次的运行位置，与fixture结合使用时，
                # 会激活yield后面的操作(如：teardown()方法)
        print("after:{}",i)
p=function()
print(next(p))
print(next(p))
print(next(p))
