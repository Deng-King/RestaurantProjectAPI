import datetime
from settings import ip
import pymysql


# 图像路径缺省未设置
def show(notice_id,ip = ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select * from notice"
        cursor.execute(sql)
        data = cursor.fetchone()
        d = str(data[5].date())
        t = str(data[5].time())
        sql = 'select user_name from user where user_id = %d' % (data[1])
        cursor.execute(sql)
        name = cursor.fetchone()
        result = (data[0], name[0], data[2], data[3], data[4], d + " " + t)
    except:
        return None,False
    return result,True


# ip = '124.70.200.142'
# user_id = 1
# content = '111'
# title = '1111'
# notice_level = 1
# print(show(ip))
