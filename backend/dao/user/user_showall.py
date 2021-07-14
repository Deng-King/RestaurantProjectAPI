import pymysql
from settings import ip


# 展示用户列表，成功则返回除了管理员以外的所有在职员工数据和true，失败则返回none和false
# 数据顺序为：user_id, user_number, user_name, user_position, user_img, user_gender, user_state
def show(ip=ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 管理员数据不能返回，即user_postion <>1
        # 离职员工数据不能返回，即user_onduty=1
        sql = "select user_id, user_number, user_name, user_position, user_img, user_gender, user_state from user where " \
              "user_position <>1 and user_onduty=1"
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.close()
    except:
        return None, False
    return data, True
