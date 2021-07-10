import pymysql
from settings import ip

def show(id):
    # 返回
    # user_id,[0]
    # user_number,[1]
    # user_name,[2]
    # user_position,[3]
    # user_img,[4]
    # user_gender,[5]
    # 打开数据库连接
    data = ()
    try:
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select user_id, user_number, user_name, user_position, user_img, user_gender from user where user_id=%d " % (id)
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        db.close()
        print("运行了这里")
    except:
        return (),False
        # 数据库失败则返回空元组和false
    return data,True
    # 成功则返回数据和True

# ip = '124.70.200.142'
# print(show(ip,1))
