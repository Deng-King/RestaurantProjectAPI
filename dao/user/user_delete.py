import pymysql


def delete(ip, id):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    sql = 'delete from user where user_id = %d' %(id)
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
    return '删除成功'

# ip = '124.70.200.142'
# print(delete(ip,1))
