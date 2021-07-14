import pymysql
from settings import ip


# 查看所有订单的详细信息，成功返回订单数据和true，失败返回none和false
# 单个订单的数据： order_id, food_id, food_num, food_state
def show(ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 索引所有订单的菜品列表
        sql = "select * from orderinfo"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.close()
    except:
        return None, False
    return data, True

# ip = '124.70.200.142'
# print(show())
