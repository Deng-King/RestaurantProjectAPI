import pymysql
from settings import ip

def update(order_id,ip = ip):  # 根据id更改头像
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update orderlist set order_state=1 where order_id = %d and order_state=0" % (order_id)
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return True
    except:
        db.rollback()
        cursor.close()
        db.close()
        return False


# ip = '124.70.200.142'
# print(update(ip,3))
