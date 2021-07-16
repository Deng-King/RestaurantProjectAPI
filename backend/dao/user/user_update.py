import pymysql
from settings import ip


# 修改各数据对应的函数，包括修改图像、密码、职位

# 根据id更改头像，成功返回true，失败返回false
def updateimg(id, img, ip=ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "update user set user_img='%s' where user_id = %d" % (img, id)
        cursor.execute(sql)
        db.commit()
    except:
        return False
    return True


# 根据id更改密码，成功返回true，失败返回false
def updatepwd(id, pwd, ip=ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "update user set user_pwd='%s' where user_id = %d" % (pwd, id)
        cursor.execute(sql)
        db.commit()
    except:
        return False
    return True


# 根据id更改职位，成功返回true，失败返回false
def updatepos(id, position, ip=ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "update user set user_position=%d where user_id = %d" % (position, id)
        cursor.execute(sql)
        db.commit()
        print("运行了这里")
    except:
        return False
    return True

