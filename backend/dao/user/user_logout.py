import pymysql
from settings import ip


# 账号登出，输入为user_id，返回true或false
def login(id, ip=ip):
    # 打开数据库连接
    try:
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 根据user_id索引用户并修改对应的登录状态为0
        sql = "update user set user_state=0 where user_id = %d" % (id)
        cursor.execute(sql)
        db.commit()
    except:
        return False
    return True

# ip = '124.70.200.142'
# id = 1
# print(login(ip, id))
