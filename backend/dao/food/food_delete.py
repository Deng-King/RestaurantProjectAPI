import pymysql
from settings import ip


# 删除菜品，将food_valid改为0，删除成功返回true，失败返回false
def delete(id, ip=ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 根据food_id删除对应菜品，并非真正的删除，而是将food_valid置为0,
        sql = "update food set food_valid=0 where food_id=%d" % (id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    except:
        return False
    return True
