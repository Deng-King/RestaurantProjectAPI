import pymysql

def update(ip, food_id,order_id):   # 厨师将食物状态改变为准备上菜，输入是food_id和order_id
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = 'update orderinfo set food_state=1 where order_id=%d and food_id=%d and food_state=0' % (order_id,food_id)
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
# food_id=3
# order_id=17
# print(update(ip, food_id,order_id))
