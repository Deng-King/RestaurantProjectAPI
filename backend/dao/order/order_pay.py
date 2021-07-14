import pymysql
from settings import ip


# 输入订单号和操作码，修改订单的付款状态
# 管理员处理订单，opcode为1是支付，2是免单
def update(order_id, opcode, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 根据订单编号来索引准备结账的订单，并修改其状态为已支付或免单
        sql = "update orderlist set order_state=%d where order_id = %d and order_state=1" % (opcode + 1, order_id)
        cursor.execute(sql)
        db.commit()
        # 索引订单的桌号
        sql = "select order_table from orderlist where order_id=%d" % (order_id)
        cursor.execute(sql)
        table_id = cursor.fetchone()
        # print(table_id)
        # 订单结账后将对应的桌子改为空闲状态
        sql = "update tableinfo set table_state=0 where table_id=%d" % (table_id[0])
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
# print(update(ip, 3, 2))
