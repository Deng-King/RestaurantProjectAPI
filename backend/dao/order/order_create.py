import pymysql
from settings import ip


# 创建新订单，输入订单信息，返回创建成功或桌子被占用或创建失败
def create(order_table, order_total, user_id, food_info, ip=ip):
    # 打开数据库连接
    db = pymysql.connect(host=ip, user="root", password="00000000", database="ordersys")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    try:
        # 根据桌号索引桌子状态
        sql = 'select table_state from tableinfo where table_id=%d' % (order_table)
        cursor.execute(sql)
        data = cursor.fetchone()
        # 桌子状态为1则表示桌子被占用
        if data[0] == 1:
            cursor.close()
            db.close()
            return '桌子被占用'
        # 否则修改桌子状态为占用状态
        else:
            sql = 'update tableinfo set table_state=1 where table_id = %d' % (order_table)
            cursor.execute(sql)
            db.commit()

        # 将订单信息插入到orderlist表中
        sql = "insert into orderlist(order_table, order_total, user_id) values(%d,%f,%d)" % (
            order_table, order_total, user_id)
        cursor.execute(sql)
        db.commit()

        # order_id为主键自增，因此新增订单的order_id必为最大值
        sql = "select max(order_id) from orderlist"
        cursor.execute(sql)
        order_id = cursor.fetchone()
        # print(order_id)
        # 根据得到的order_id将订单详细信息插入到orderinfo表中
        for foodinfo in food_info:
            sql = 'insert into orderinfo(order_id,food_id,food_num) values(%d,%d,%d)' % (
            order_id[0], foodinfo[0], foodinfo[1])
            cursor.execute(sql)
            db.commit()
        cursor.close()
        db.close()
        return '创建成功'
    except:
        cursor.close()
        db.close()
        return '创建失败'

