import pymysql


def updatename(ip, id, name):  # 根据id更改名称
    # 打开数据库连接
    db = pymysql.connect(host=ip, food="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update food set food_name='%s' where food_id = %d" % (name, id)
    cursor.execute(sql)
    db.commit()
    return '修改名称成功'


def updateinfo(ip, id, info):  # 根据id更改简介
    # 打开数据库连接
    db = pymysql.connect(host=ip, food="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update food set food_info='%s' where food_id = %d" % (info, id)
    cursor.execute(sql)
    db.commit()
    return '修改简介成功'


def updateimg(ip, id, img):  # 根据id更改图片
    # 打开数据库连接
    db = pymysql.connect(host=ip, food="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update food set food_img='%s' where food_id = %d" % (img, id)
    cursor.execute(sql)
    db.commit()
    return '修改图片成功'


def updateprice(ip, id, price):  # 根据id更改价格
    # 打开数据库连接
    db = pymysql.connect(host=ip, food="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update food set food_price=%f where food_id = %d" % (price, id)
    cursor.execute(sql)
    db.commit()
    return '修改价格成功'


def updatermd(ip, id, rmd):  # 根据id更改推荐情况
    # 打开数据库连接
    db = pymysql.connect(host=ip, food="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "update food set food_rmd= %d where food_id = %d" % (rmd, id)
    cursor.execute(sql)
    db.commit()
    return '修改推荐情况成功'

# ip = '124.70.200.142'

