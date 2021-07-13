import pymysql
from settings import ip

# 图像路径缺省未设置
def create(number, name, position, pwd="123456",img='', gender=0, ip = ip):
    # 打开数据库连接
    # try:
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql = "insert into user(user_number,user_pwd,user_name,user_position,user_img,user_gender) values('%s','%s','%s'," \
            "%d,'%s',%d)" % ( number, pwd, name, position, img, gender)
        try:
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return '创建成功'
        except:
            cursor.close()
            db.close()
            return '用户已存在'
    # except:
    #     return "数据库错误"

# ip = '124.70.200.142'
# number = '20192242'
# pwd = '123456'
# name = 'wei'
# position = 1
# img = 'tupian'
# gender = 0
# print(create(ip, number, pwd, name, position, img, gender))
