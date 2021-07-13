import pymysql
from settings import ip
def delete(id,ip = ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = 'delete from food where food_id = %d' % (id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    except:
        return False
    return True

