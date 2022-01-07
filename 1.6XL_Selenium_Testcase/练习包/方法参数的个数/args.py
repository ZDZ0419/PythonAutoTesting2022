def fun_args1(args):
    print("args is %s" %args)

fun_args1("51zxw")
#fun_args1()
#fun_args1('51zxw','pyhton')

def fun_args2(args1,args2):
    print("args1 is %s,args2 is %s" %(args1,args2))

# fun_args2("51zxw")
#fun_args2()
fun_args2('51zxw','pyhton')

def fun_argsA(*args):
    for value in args:
        print("args:",value)

#fun_argsA("51zxw")
#fun_argsA()
fun_argsA('51zxw','pyhton')

