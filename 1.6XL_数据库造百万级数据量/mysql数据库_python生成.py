import pymysql
import time
import gevent
import random

class MyPyMysql:

    # 初始化连接参数
    def __init__(self,host,port,username,password,db,charset='utf8'):
        self.host=host    #主机地址
        self.port=port    #端口号
        self.username=username #用户名
        self.password=password #密码
        self.db=db              #数据库名
        self.charset=charset    #使用的字符编码，默认utf8

        # __init__初始化后，执行的函数----连接mysql数据库
        self.pymysql_connect()

    # 连接 mysql 数据库
    def pymysql_connect(self):
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.username,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset
                                    )
    # 连接 mysql 数据库后执行的函数：--
        self.asynchronous()

    def run(self,nmin,nmax):
        #创建游标
        self.cur=self.conn.cursor()

        #定义sql语句，插入数据DID DNAME DPHONE
        sql='insert into AA_TESTA.DEPARTMENT(DID,DNAME,DPHONE) values(%s,%s,%s)'

        #定义总插入行数为一个空列表
        data_list=[]
        #rand=random.randint()
        for i in range(nmin,nmax):
            #添加所有任务到总的任务列表
            #result=(i,'测试部'+str(i),'182'+str(i))
            result = (i,'测试部' + str(random.randint(1,9999999)),'182' + str(random.randint(10000000,99999999)))
            data_list.append(result)

        #执行多行插入，executemany(sql语句，数据(需要一个元组类型))
        content= self.cur.executemany(sql,data_list)
        if content:
            print('成功插入第{}条数据'.format(nmax-1))
        #执行完成后务必提交数据
            self.conn.commit()


    # 定义 异步 操作函数
    def asynchronous(self):
        #g_l任务列表
        #定义了异步的函数：用到了gevent.spawn方法
        max_line =10000  #定义每次最大插入行数
        g_l=[gevent.spawn(self.run,i,i+max_line) for i in range(1,3000001,max_line)]

        #gevent.joinall 等待所有操作都执行完毕
        gevent.joinall(g_l)
        self.cur.close()  # 关闭游标
        self.conn.close()  #关闭数据库连接

if __name__ == '__main__':
    start_time =time.time() #程序开始时间

    #实例化类，传参
    st = MyPyMysql('192.168.43.11',3306,'tester','123456','mysql')
    print('程序耗时{:.2f}s'.format(time.time() -start_time)) #计算总耗时