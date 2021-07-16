import pymysql
from settings import ip


# 新建用户，输入用户数据，返回“成功”或“用户已存在”
def create(number, name, position, pwd="e10adc3949ba59abbe56e057f20f883e"\
    , img='', gender=0, ip=ip):
    # 密码是123456的哈希值
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        sql = "select user_number"
        # 根据用户职位选择默认的头像地址
        if position == 1 and img == '':
            img = "http://124.70.200.142:8080/img/person/admin.jpg"
        elif position == 2 and img == '':
            img = "http://124.70.200.142:8080/img/person/waiter.jpg"
        elif position == 3 and img == '':
            img = "http://124.70.200.142:8080/img/person/cook.jpg"
        # 将用户数据插入到user表中
        sql = "insert into user(user_number,user_pwd,user_name,user_position,user_img,user_gender) values('%s','%s','%s'," \
              "%d,'%s',%d)" % (number, pwd, name, position, img, gender)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return '创建成功'
    except:
        # 用户工号重复
        cursor.close()
        db.close()
        return '添加错误'



