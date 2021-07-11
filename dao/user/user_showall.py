import pymysql
from settings import ip

def show(ip = ip):
      try:
            # 打开数据库连接
            db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()
            sql = "select user_id, user_number, user_name, user_position, user_img, user_gender, user_state from user where " \
                  "user_position <>1 "
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            db.close()
      except:
            return None,False
      return data,True

