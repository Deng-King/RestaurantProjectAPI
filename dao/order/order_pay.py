import pymysql


def update(ip, order_id, opcode):  # opcode为1是支付，2是免单.   管理员处理订单
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update orderlist set order_state=%d where order_id = %d and order_state=1" % (opcode+1,order_id)
    try:
        cursor.execute(sql)
        db.commit()
        sql="select order_table from orderlist where order_id=%d" %(order_id)
        cursor.execute(sql)
        table_id=cursor.fetchone()
        # print(table_id)
        sql="update tableinfo set table_state=0 where table_id=%d" %(table_id[0])
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


ip = '124.70.200.142'
print(update(ip, 3, 2))
