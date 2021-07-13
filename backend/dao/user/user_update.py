import pymysql
from settings import ip

def updateimg(id, img, ip = ip):  # 根据id更改头像
    # 打开数据库连接
    try:
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "update user set user_img='%s' where user_id = %d" % (img, id)
        cursor.execute(sql)
        db.commit()
    except:
        return False
    return True


def updatepwd(id, pwd, ip = ip):  # 根据id更改密码
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update user set user_pwd='%s' where user_id = %d" % (pwd, id)
    cursor.execute(sql)
    db.commit()
    return True


def updatepos(id, position, ip = ip):  # 根据id更改职位
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update user set user_position=%d where user_id = %d" % (position, id)
    cursor.execute(sql)
    db.commit()
    return '修改职位成功'


# ip = '124.70.200.142'
# id = 1
# img = 'tupian'
# pwd = '666321'
# position = 1
# print(updateimg(ip, id, img))
# print(updatepwd(ip, id, pwd))
# print(updatepos(ip, id, position))