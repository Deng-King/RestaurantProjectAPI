import pymysql
from settings import ip


# 添加新菜品
# 图片缺省值设置为默认图片地址，成功返回food_id和true，失败返回none和false
def create(name: str, info: str, price: float, rmd=0,
           img='http://124.70.200.142:8080/img/food/food_default.jpg',):
    #try:
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 索引是否已有菜品是否与新增菜品重名
    sql = "select * from food where food_name = '%s' and food_valid = 1" % (name)
    cnt = cursor.execute(sql)
    # 若不重名则添加新菜品
    if cnt == 0:
        # 在food表中插入对应数据，img缺省值为菜品默认图片地址
        sql = "insert into food(food_name,food_info,food_price,food_rmd,food_img) values('%s','%s',%f,%d,'%s')" % (
            name, info, price, rmd, img)
        cursor.execute(sql)
        db.commit()
        # 由于food_id为主键自增，因此新增加的菜品的food_id必为最大值，故索引最大的food_id并返回
        sql = 'select max(food_id) from food'
        cursor.execute(sql)
        id = cursor.fetchone()[0]
        # 关闭游标和数据库并返回数据
        cursor.close()
        db.close()
        return id, True
    else:
        return None, False


"""except:
        cursor.close()
        db.close()
        return None, False"""