import pymysql
from settings import ip


# 展示用户列表中某用户的详细信息，该用户可能为除了管理员以外的所有在职员工
# 失败则返回空元组和false
# 成功则返回数据和True
# 数据顺序：user_id, user_number, user_name, user_position, user_img, user_gender, user_pwd, user_state
def show(id, ip=ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "select user_id, user_number, user_name, user_position, user_img, user_gender, user_pwd, user_state from user where user_id=%d " % (
            id)
        cnt = cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        db.close()
        # 若未匹配到数据则失败
        if cnt == 0:
            return None, "not found"
        else:
            return data, True
    except:
        cursor.close()
        db.close()
        return None, False

# ip = '124.70.200.142'
# print(show(1))
