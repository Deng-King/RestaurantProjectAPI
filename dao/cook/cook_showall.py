import pymysql
from settings import ip

def show(ip = ip):   # return food_name,food_num,order_id,order_table,food_state
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select a.food_name,b.food_num,c.order_id,c.order_table,b.food_state from food a, orderinfo b, orderlist c " \
            "where a.food_id=b.food_id and c.order_id=b.order_id and c.order_state=0 and b.food_state =0 "
        try:
            cursor.execute(sql)
            result=cursor.fetchall()
        except:
            db.rollback()
        cursor.close()
        db.close()
    except:
        return None,False
    return result,True

# ip = '124.70.200.142'
# print(show(ip))
