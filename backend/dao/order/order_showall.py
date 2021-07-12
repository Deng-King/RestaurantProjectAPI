import pymysql
from settings import ip

def show(ip = ip):
    # order_id
    # order_table
    # order_state
    # order_total
    # order_create_time
    # user_id 服务员id
    result = ()
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select * from orderlist"
        cursor.execute(sql)
        data = cursor.fetchall()
        result=(())
        for i in data:
            d = str(i[4].date())
            t = str(i[4].time())
            re = ((i[0], i[1], i[2], i[3],  d + " " + t, i[5]),)
            result = result + re
            # print(type(i[1]))
        cursor.close()
        db.close()
    except:
        return None,False
    return result,True

# ip = '124.70.200.142'
# print(show(ip))
