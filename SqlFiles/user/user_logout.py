import pymysql


def login(ip, id):  # 根据id登出
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update user set user_state=0 where user_id = %d" % (id)
    cursor.execute(sql)
    db.commit()
    return '登出成功'


# ip = '124.70.200.142'
# id = 1
# print(login(ip, id))
