import pymysql
from settings import ip


# 服务员更新订单中的菜品状态，从准备上菜(food_state=1)改为已上菜(food_state=2)
# 成功返回true，失败返回false
def update(order_id, food_id, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()

    try:
        # 根据订单编号将准备上菜的菜品的状态改为已上菜
        sql = "update orderinfo set food_state=2 where order_id = %d and food_id = %d and food_state=1" % (
        order_id, food_id)
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
# print(ip,3,1)
