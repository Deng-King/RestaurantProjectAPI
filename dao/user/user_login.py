import pymysql
from settings import ip


def login(number, pwd, ip = ip):      # 返回   登录信息， 用户id,  用户职位(1管理员	2服务员	3后厨)
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select * from user where user_number='%s';" % (number)
    login1 = cursor.execute(sql)
    if login1 == 0:
        cursor.close()
        db.close()
        return '用户名错误', -1, -1
    else:
        data = cursor.fetchone()
        # print(data)
        if data[7] == 1:
            cursor.close()
            db.close()
            return '用户已登录', -1, -1
        if data[2]!=pwd:
            cursor.close()
            db.close()
            return '密码错误', -1, -1
        else:
            sql="update user set user_state=1 where user_number='%s';" % (number)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return '登陆成功', data[0], data[4]     # 返回   登录信息， 用户id, 用户职位






# ip = '124.70.200.142'
# id = '20192242'
# pwd = '123456'
# print(login(ip, id, pwd))