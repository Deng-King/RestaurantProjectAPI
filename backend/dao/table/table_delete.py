import pymysql
from settings import ip

# 删除最后一个桌子
def delete(ip = ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select max(table_id) from tableinfo"
    cursor.execute(sql)
    max_id = cursor.fetchone()
    sql = "delete from tableinfo where table_id = %d and table_state = 0" %(max_id[0])
    cnt = cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    if cnt:
        return True
    else:
        return False

# ip = '124.70.200.142'
# print(delete(ip))
