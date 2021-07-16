import pymysql
from settings import ip


# 展示所有菜品，返回菜品数据
# food_id, food_name, food_price, food_rmd, food_img
def show(ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 选择有效的菜品数据返回
        sql = "select food_id,food_name,food_price,food_rmd,food_img from food where food_valid = 1"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.close()
    except:
        cursor.close()
        db.close()
        return None, False
    return data, True

