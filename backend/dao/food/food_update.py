import pymysql
from settings import ip


# 修改菜品名称、简介、图片、价格、推荐函数

# 根据id更改菜品名称
def updatename(id, name, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "select * from food where food_name = '%s' and food_valid = 1" % (name)
        cnt = cursor.execute(sql)
        if cnt == 0:
            sql = "update food set food_name='%s' where food_id = %d" % (name, id)
            cursor.execute(sql)
            db.commit()
        cursor.close()
        db.close()
    except:
        cursor.close()
        db.close()
        return False
    return True


# 根据id更改简介
def updateinfo(id, info, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update food set food_info='%s' where food_id = %d" % (info, id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    except:
        cursor.close()
        db.close()
        return False


# 根据id更改图片
def updateimg(id, img, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update food set food_img='%s' where food_id = %d" % (img, id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    except:
        cursor.close()
        db.close()
        return False


# 根据id更改价格
def updateprice(id, price, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update food set food_price=%f where food_id = %d" % (price, id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    except:
        cursor.close()
        db.close()
        return False


# 根据id更改推荐情况
def updatermd(id, rmd, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "update food set food_rmd= %d where food_id = %d" % (rmd, id)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
    except:
        cursor.close()
        db.close()
        return False
# ip = '124.70.200.142'
