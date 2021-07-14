import pymysql
from settings import ip


# 删除用户，并非从表中真正删除该用户，而是将其在职状态user_onduty改为离职状态0
def delete(id, ip=ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = 'select user_position from user where user_id=%d' % (id)
        cursor.execute(sql)
        data = cursor.fetchone()
        # 避免删除管理员
        if data[0] == 1:
            return "admin"
        # 修改用户在职状态
        sql = 'update user set user_onduty=0 where user_id=%d' % (id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    except:
        return False
    return True

# ip = '124.70.200.142'
# print(delete(28,ip))
