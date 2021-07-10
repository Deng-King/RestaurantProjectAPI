import pymysql


def show(ip, id):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select user_id, user_number, user_name, user_position, user_img, user_gender from user where user_id=%d " % (
        id)
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    db.close()
    return data

# ip = '124.70.200.142'
# print(show(ip,1))
