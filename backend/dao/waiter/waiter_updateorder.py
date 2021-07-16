import pymysql
from settings import ip


# 服务员更高订单状态，从未付款改为准备付款
# 成功返回true，失败返回false
def update(order_id, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 判断当前订单中的菜品是否均上齐，未上齐则无法更新订单状态
        sql = "select food_state from orderinfo where order_id = %d" % (order_id)
        cursor.execute(sql)
        food_state = cursor.fetchall()
        # 判断是否有菜品未上桌
        for i in food_state:
            if i[0] < 2:
                cursor.close()
                db.close()
                return "有菜品未上桌"
        # 根据订单编号将对应的未付款订单状态改为准备付款
        sql = "update orderlist set order_state=1 where order_id = %d and order_state=0" % (order_id)
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

