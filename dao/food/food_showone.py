import pymysql
from settings import ip

def show(id):
    # 打开数据库连接
    try:
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # sql = "select food_id,food_name,food_price,food_rmd,food_img from food"
        sql = "select * from food where food_id=%d" % (id)
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        db.close()
    except:
        return None,False
    return data,True


# ip = '192.168.137.164'
# print(show(ip, 2))
