# 测试股票第三方接口是否正常
import tushare
import time
#i=Page
# 获取股票数据
def getrealtimeData(code):
    DataNow=tushare.get_realtime_quotes("000591")
    #DataNow_2=tushare.get_realtime_quotes("000591")
    name_1=DataNow.loc[0][0]  # 股票名称
    open_1=DataNow.loc[0][1]  # 当日开盘价
    high_1=DataNow.loc[0][4]  # 当日最高价
    low_1=DataNow.loc[0][5]   # 当日最低价
    volumn_1=DataNow.loc[0][8]  # 当日成交量（总股数）
    amount_1=DataNow.loc[0][9]  # 成交额
    pre_close_1=DataNow.loc[0][2]  # 昨日收盘价
    timee_1=DataNow.loc[0][30]     # 日期
    price_1=float(DataNow.loc[0][3])
    #print(type(DataNow))
   # print(DataNow)
    print("股票名称：",name_1,"当前价格：",price_1,"最高价：",high_1,"最低价：",low_1,"开盘价：",open_1,"成交量：",volumn_1,"成交额:",amount_1,"昨日收盘价：",pre_close_1,"日期",timee_1)

# 股票类
class GP():
    def __init__(self,arg):
        self.name_1=name_1
        open_1 = DataNow.loc[0][1]  # 当日开盘价
        high_1 = DataNow.loc[0][4]  # 当日最高价
        low_1 = DataNow.loc[0][5]  # 当日最低价
        volumn_1 = DataNow.loc[0][8]  # 当日成交量（总股数）
        amount_1 = DataNow.loc[0][9]  # 成交额
        pre_close_1 = DataNow.loc[0][2]  # 昨日收盘价
        timee_1 = DataNow.loc[0][30]  # 日期
        price_1 = float(DataNow.loc[0][3])





























    buy=17.51
    sale=17.53
    if price_1<=buy:
        print("当前股价为：",price_1,"\n可以买进！！！")
    elif price_1>=sale:
        print("当前股价为：",price_1,"\n抓紧卖出！！！")
    else:
        print("继续监控中，不需关注！！！")
    time.sleep(5)
    i+=1




