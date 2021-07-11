import pymysql
from settings import ip

def create(order_table, order_total, user_id, food_info, ip = ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = 'select table_state from tableinfo where table_id=%d' % (order_table)
    cursor.execute(sql)
    data = cursor.fetchone()
    if data[0] == 1:
        cursor.close()
        db.close()
        return '桌子被占用'
    else:
        sql = 'update tableinfo set table_state=1 where table_id = %d' % (order_table)
        cursor.execute(sql)
        db.commit()

    sql = "insert into orderlist(order_table, order_total, user_id) values(%d,%f,%d)" % (
        order_table, order_total, user_id)
    cursor.execute(sql)
    db.commit()

    sql = "select max(order_id) from orderlist"
    cursor.execute(sql)
    order_id = cursor.fetchone()
    # print(order_id)
    for foodinfo in food_info:
        sql = 'insert into orderinfo(order_id,food_id,food_num) values(%d,%d,%d)' % (order_id[0], foodinfo[0], foodinfo[1])
        cursor.execute(sql)
        db.commit()

    cursor.close()
    db.close()
    return '创建成功'


# ip = '124.70.200.142'
# order_table = 1
# order_total = 100
# user_id = 1
# food_info = [[1, 2], [2, 1], [3, 5]]
# print(create(ip, order_table, order_total, user_id, food_info))
