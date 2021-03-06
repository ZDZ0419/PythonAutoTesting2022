'''
案例：模拟银行ATM存取款
Page. 模拟3张银行卡，1001 1002 1003，分别设置密码和余额（使用列表嵌套字典的方式保存信息）；
2. 提示用户输入银行卡号、密码，遍历每张卡的信息是否验证成功；
3.如果用户输入正确，提示用户选择取款、存款、退出，并显示余额多少；
    输入错误，提示重新输入
        选择取款：提示输入取款金额，超过余额，提示余额不足，否则余额减去取款金额
        选择存款：提示输入存款金额，余额增加存款金额，并提示余额
        选择退出，重新登录
4. 设置3次输入账号后，提示密码被锁定，程序结束
'''
card1={'卡号':'1001','姓名':'张三','密码':'123','余额':1001}
card2={'卡号':'1002','姓名':'李四','密码':'123','余额':1002}
card3={'卡号':'1003','姓名':'王五','密码':'123','余额':1003}
card4={'卡号':'1004','姓名':'赵六','密码':'123','余额':1004}
cardlist=[card1,card2,card3,card4]
count=0 #定义输入的错误次数变量
while 1==1:
    KH=input('请输入您的卡号：')
    passwd=input('请输入您的密码：')
    msg=0  #记录登录状态 0表示登录失败，1表示登录成功   for循环遍历中不要用else
    for C in cardlist:
        if KH==C['卡号'] and passwd==C['密码']:
            msg=1
            count=0
            print('登录成功')
            print('您的当前余额为：'+str(C['余额'])+'元')
            while 2==2:
                YW=int(input('请选择业务类型：（取款 Page、存款 2、退出 3）'))
                if YW==1:
                    QK=int(input('请输入取款金额：'))
                    if QK<=C['余额']:
                        C['余额']=C['余额']-QK
                        print('取款成功，目前您的余额为：'+str(C['余额'])+'元')
                    elif QK>C['余额']:
                        print('余额不足,请重新输入！')
                        continue
                    else:
                        print('输入内容错误，请重新输入')
                        continue
                elif YW==2:
                    CK=int(input('请输入存款金额：'))
                    C['余额']=C['余额']+CK
                    print('存款成功，目前您的余额为：'+str(C['余额'])+'元')
                elif YW==3:
                    print('退出成功，请重新登录！')
                    break
                else:
                    print('您的输入内容错误，请重新输入!')
                    continue
    if msg==0:
        count+=1
        if count==3:
            print('您已连续输入错误3次，账号被锁定！')
            break
        else:
            print('卡号或密码错误，请重新输入！')
            continue