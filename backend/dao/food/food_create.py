import pymysql


# 图片缺省值设置   成功返回id，失败返回0
def create(ip, name, info, price, rmd, img='http://124.70.200.142:8080/img/food/food_default.jpg'):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "insert into food(food_name,food_info,food_price,food_rmd,food_img) values('%s','%s',%f,%d,'%s')" % (
        name, info, price, rmd, img)
    try:
        cursor.execute(sql)
        db.commit()
        sql = 'select max(food_id) from food'
        cursor.execute(sql)
        id = cursor.fetchone()[0]
        cursor.close()
        db.close()
        return id
    except:
        cursor.close()
        db.close()
        return 0
