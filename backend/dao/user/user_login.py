import pymysql
from settings import ip


# 输入为用户工号和密码
# 登录成功 返回“登录成功”，用户id,  用户职位(1管理员 2服务员	3后厨)
# 登录失败 返回错误提示, -1, -1
def login(number, pwd, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 根据用户工号索引在职(user_onduty=1)的用户
    sql = "select * from user where user_number='%s' and user_onduty=1;" % (number)
    match_num = cursor.execute(sql)
    # 若未索引到数据则表示用户不存在
    if match_num == 0:
        cursor.close()
        db.close()
        return '用户名错误', -1, -1
    else:
        # data = user_id,user_number,user_pwd,user_name,user_position,user_img,user_gender,user_state,user_onduty
        data = cursor.fetchone()
        # 若user_state为1，则表示用户已登录
        if data[7] == 1:
            cursor.close()
            db.close()
            return '用户已登录', -1, -1
        # 若用户密码与输入不匹配，则表示密码错误
        if data[2] != pwd:
            cursor.close()
            db.close()
            return '密码错误', -1, -1
        # 排除所有登录错误的情况则登录成功，修改用户登录状态为1
        else:
            sql = "update user set user_state=1 where user_number='%s';" % (number)
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return '登陆成功', data[0], data[4]

# ip = '124.70.200.142'
# id = '20192242'
# pwd = '123456'
# print(login(ip, id, pwd))
