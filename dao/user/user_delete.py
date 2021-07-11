import pymysql
from settings import ip

def delete(id):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = 'select user_position from user where user_id=%d'   %(id)
        cursor.execute(sql)
        data=cursor.fetchone()
        if data[0]==1:
            return "admin"
        sql = 'delete from user where user_id = %d and user_position <> 1'  %(id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    except:
        return False
    return True

# ip = '124.70.200.142'
# print(delete(ip,1))
