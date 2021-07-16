from settings import ip
import pymysql

# 显示notice_id对应公告的详细信息，
# 成功返回notice_id,user_id,user_name,notice_content,notice_title,notice_level,notice_create_time以及true
# 失败返回none和false
def show(notice_id,ip = ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 根据notice_id索引对应的公告数据
        sql = "select * from notice where notice_id=%d"% (notice_id)
        cursor.execute(sql)
        data = cursor.fetchone()
        # 将创建时间转换为字符串类型
        date = str(data[5].date())
        time = str(data[5].time())
        # 根据user_id索引对应的user_name
        sql = 'select user_name from user where user_id = %d' % (data[1])
        cursor.execute(sql)
        name = cursor.fetchone()
        result = (data[0], data[1], name[0], data[2], data[3], data[4], date + " " + time)
    except:
        return None,False
    return result,True


