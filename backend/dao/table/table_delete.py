import pymysql
from settings import ip


# 删除最后一个桌子
def delete(ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 索引最大的桌号
    sql = "select max(table_id) from tableinfo"
    cursor.execute(sql)
    max_id = cursor.fetchone()
    # 删除对应的桌子，桌子必须处于未占用状态
    sql = "delete from tableinfo where table_id = %d and table_state = 0" % (max_id[0])
    cnt = cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    # 成功删除返回true，失败返回false
    if cnt:
        return True
    else:
        return False

