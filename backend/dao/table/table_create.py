import pymysql
from settings import ip


# 创建指定数量(number)的桌子，返回true或false
def create(number, ip=ip):
    try:
        # 打开数据库连接
        db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        # 先找到最大的桌号
        sql = "select max(table_id) from tableinfo"
        cursor.execute(sql)
        num = cursor.fetchone()
        # 如果桌数为0，则num为none，调整桌号从1开始
        if num[0] == None:
            max_id = 0
        else:
            max_id = num[0]
        # 从最大的桌号开始添加桌子，保证桌号的连续性
        for i in range(0, number):
            sql = "insert into tableinfo(table_id,table_state) values(%d, 0)" % (max_id + i + 1)
            cursor.execute(sql)
            db.commit()
        cursor.close()
        db.close()
    except:
        return False
    return True

# ip = '124.70.200.142'
# print(create(2,ip))