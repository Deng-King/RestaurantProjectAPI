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
    try:
        print("type:",type(id),"id =",id)
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select user_id, user_number, user_name, user_position, user_img, user_gender, user_pwd, user_state from user where user_id=%d " % (id)
        cnt = cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        db.close()
        print("data =",data)
        if cnt == 0:
            return None,"not found"
        else:
            return data,True
    except:
        return None, False
    return data,True
        # 数据库失败则返回空元组和false
    # 成功则返回数据和True

# ip = '124.70.200.142'
# print(show(1))
