import pymysql
from settings import ip

# 展示所有桌子的状态
def show(ip = ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select * from tableinfo"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.close()
    except:
        return None,False
    return data,True

# ip = '124.70.200.142'
# print(show(ip))
