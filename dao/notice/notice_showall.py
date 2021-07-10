import datetime
import pymysql


# 图像路径缺省未设置
def show(ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select * from notice"
    cursor.execute(sql)
    data = cursor.fetchall()
    result = (())
    for i in data:
        d = str(i[5].date())
        t = str(i[5].time())
        sql = 'select user_name from user where user_id = %d' % (i[1])
        cursor.execute(sql)
        name = cursor.fetchone()
        re = ((i[0], name[0], i[2], i[3], i[4], d + " " + t),)
        result = result + re
        # print(type(i[1]))
    return result

# ip = '124.70.200.142'
# user_id = 1
# content = '111'
# title = '1111'
# notice_level = 1
# print(show(ip))
