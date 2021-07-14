import pymysql
from settings import ip


# 管理员删除新公告，输入要删除的公告的编号，返回成功或失败
def delete(notice_id, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 将notice表中对应notice_id的行删除
    sql = "delete from notice where notice_id = %d " %(notice_id)
    try:
        cnt = cursor.execute(sql)
        if cnt == 0:
            return "未找到此公告"
        db.commit()
        cursor.close()
        db.close()
    except:
        db.rollback()
        cursor.close()
        db.close()
        return False
    return True