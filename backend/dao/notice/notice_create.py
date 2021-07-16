import pymysql
from settings import ip


# 管理员创建新公告，输入公告相应内容，返回成功或失败
def create(user_id, content, title, notice_level, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 将相应数据插入到notice表中
    sql = "insert into notice(user_id,notice_content,notice_title,notice_level) values(%d,'%s','%s',%d)" % (
        user_id, content, title, notice_level)
    try:
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return True
    except:
        db.rollback()
        cursor.close()
        db.close()
        return False
