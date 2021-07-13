import pymysql
from settings import ip

# 创建number数量个桌子
def create(number,ip = ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select max(table_id) from tableinfo"
        cursor.execute(sql)
        max_id = cursor.fetchone()
        for i in range(0,number):
            sql = "insert into tableinfo(table_id,table_state) values(%d, 0)" %(max_id[0]+i+1)
            cursor.execute(sql)
            db.commit()
        cursor.close()
        db.close()
    except:
        return False
    return True

# ip = '124.70.200.142'
# print(create(ip,2))
