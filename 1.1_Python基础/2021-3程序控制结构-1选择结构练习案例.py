'''
--案例1--
为一家超市开发一个简易的收银系统（以三到五种商品为例）：
使用变量保存  商品价格、商品编号、商品名称

Page、提示用户输入编号和数量，然后显示总价是多少
2、提示用户输入付款金额，然后显示找零金额
'''
SP1={'商品名称':'商品1','商品编号':'001','商品价格':7.9}
SP2={'商品名称':'商品2','商品编号':'002','商品价格':2.9}
SP3={'商品名称':'商品3','商品编号':'003','商品价格':9.9}
# SPbh1='001'
# SPjg1=56
# SPname1='商品1'
# SPbh2='002'
# SPjg2=2.9
# SPname2='商品2'
# SPbh3='003'
# SPjg3=5
# SPname3='商品3'
AA=input('请输入商品编号：')
#声明变量
price=0
name=''
if AA==SP1['商品编号']:
    price=SP1['商品价格']
    name=SP1['商品名称']
elif AA==SP2['商品编号']:
    price=SP2['商品价格']
    name=SP2['商品名称']
elif AA==SP3['商品编号']:
    price=SP3['商品价格']
    name=SP3['商品名称']
else:
    print('商品信息不存在！')
    price=0
if price!=0:
    BB = int(input('请输入商品数量：'))
    CC=round(price*BB,1)  #round()减少小数转换为二进制后的误差，可以保留小数位
    print('您的购买的商品信息：商品名称:{},商品单价:{},商品数量:{},商品总价:{}'.format(name,price,BB,CC))
    price_YF=float(input('请输入付款金额：'))
    DD=round(price_YF-CC)
    if price_YF>=CC:
        print('应付金额：{}，已付金额：{}，找零金额：{}'.format(CC,price_YF,DD))
    elif price_YF<CC:
        print('您付款的余额不足！')


