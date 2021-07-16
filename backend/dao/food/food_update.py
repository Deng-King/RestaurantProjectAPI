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
        # 判断修改后的菜品名称是否与之前有效的菜品重名（排除自身）
        sql = "select * from food where food_name = '%s' and food_valid = 1 and food_id <>%d" % (name,id)
        cnt = cursor.execute(sql)
        # 如果不重名则更新信息
        if cnt == 0:
            sql = "update food set food_name='%s' where food_id = %d" % (name, id)
            cursor.execute(sql)
            db.commit()
        # 重名则返回已存在
        else:
            cursor.close()
            db.close()
            return "菜品名已存在"
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
