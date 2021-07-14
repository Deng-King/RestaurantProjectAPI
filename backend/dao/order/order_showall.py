import pymysql
from settings import ip


# 展现订单列表，成功返回所有订单数据和true，失败返回none和false
# 数据： order_id, order_table, order_state, order_total, order_create_time, user_id(服务员id)
def show(ip=ip):
    result = (())
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 检索订单列表中的所有数据
        sql = "select * from orderlist"
        cursor.execute(sql)
        data = cursor.fetchall()
        # 将订单创建时间从timestamp转换为string类型
        for i in data:
            date = str(i[4].date())
            time = str(i[4].time())
            re = ((i[0], i[1], i[2], i[3], date + " " + time, i[5]),)
            result = result + re
            # print(type(i[1]))
        cursor.close()
        db.close()
    except:
        cursor.close()
        db.close()
        return None, False
    return result, True

# ip = '124.70.200.142'
# print(show(ip))
