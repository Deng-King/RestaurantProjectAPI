import pymysql
from settings import ip

def show(id,ip = ip):
    # 返回
    # user_id,[0]
    # user_number,[1]
    # user_name,[2]
    # user_position,[3]
    # user_img,[4]
    # user_gender,[5]
    # user_pwd, [6]
    # user_state [7]
    # 打开数据库连接
    print("type:",type(id),"id =",id)
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = "select user_id, user_number, user_name, user_position, user_img, user_gender, user_pwd, user_state from user where user_id=%d " % (id)
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    db.close()
    print("data =",data)
    if data == None:
        return None,False
    else:
        return data,True
        # 数据库失败则返回空元组和false
    # 成功则返回数据和True

# ip = '124.70.200.142'
# print(show(1))
