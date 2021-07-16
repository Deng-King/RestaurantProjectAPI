import pymysql
from settings import ip


# 展示某菜品的详细信息，输入food_id，返回菜品数据
# 数据：food_id,food_name,food_info,food_price,food_rmd,food_img
def show(id, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 根据food_id索引菜品数据，且此菜品必须为有效的
        sql = "select * from food where food_id=%d and food_valid = 1" % (id)
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        db.close()
    except:
        return None, False
    return data, True
