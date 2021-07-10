import pymysql


def create(ip, name, info, price, rmd, img):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "insert into food(food_name,food_info,food_price,food_rmd,food_img) values('%s','%s',%f,%d,'%s')" % (
    name, info, price, rmd, img)
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return '创建成功'
    except:
        cursor.close()
        db.close()
        return '菜品已存在'

# ip = '192.168.137.164'
# name = '谭星'
# info = 'tanxing'
# price = 99
# rmd = 1
# img = '1111'
# print(create(ip, name, info, price, rmd, img))
