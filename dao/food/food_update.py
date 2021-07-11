import pymysql
from settings import ip


def updatename(id, name,ip = ip):  # 根据id更改名称
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "update food set food_name='%s' where food_id = %d" % (name, id)
        cursor.execute(sql)
        db.commit()
    except:
        return False
    return '修改名称成功'


def updateinfo(id, info,ip = ip):  # 根据id更改简介
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "update food set food_info='%s' where food_id = %d" % (info, id)
        cursor.execute(sql)
        db.commit()
    except:
        return False
    return '修改简介成功'


def updateimg(id, img,ip = ip):  # 根据id更改图片
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "update food set food_img='%s' where food_id = %d" % (img, id)
        cursor.execute(sql)
        db.commit()
    except:
        return False
    return '修改图片成功'


def updateprice(id, price,ip = ip):  # 根据id更改价格
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "update food set food_price=%f where food_id = %d" % (price, id)
        cursor.execute(sql)
        db.commit()
    except:
        return False
    return '修改价格成功'


def updatermd(id, rmd,ip = ip):  # 根据id更改推荐情况
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update food set food_rmd= %d where food_id = %d" % (rmd, id)
    cursor.execute(sql)
    db.commit()
    return '修改推荐情况成功'

# ip = '124.70.200.142'

